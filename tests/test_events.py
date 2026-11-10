"""[房玄龄·2026-11-10] Exercise contract rejection and actual HTTP boundaries."""
from copy import deepcopy
import http.client
from http.server import ThreadingHTTPServer
import json
from pathlib import Path
import sys
import threading
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'apps/event-api'))
from contract import ContractError, summarize
from app import Handler, MAX_BODY

class ContractTests(unittest.TestCase):
    def setUp(self):
        self.events = json.loads((ROOT / 'samples/events.json').read_text())

    def test_aggregate_matches_fixture(self):
        self.assertEqual(summarize(self.events), {'accepted':3,'mean_delay_minutes':5.0,'synthetic':True})

    def test_ndjson_matches_json_fixture(self):
        rows = [json.loads(x) for x in (ROOT / 'samples/events.ndjson').read_text().splitlines()]
        self.assertEqual(rows, self.events)

    def test_duplicate_id_rejected(self):
        with self.assertRaises(ContractError):
            summarize(self.events + [deepcopy(self.events[0])])

    def test_contract_rejects_bad_field_values(self):
        cases = [('synthetic',False), ('synthetic',1), ('event_time','2026-11-10'),
                 ('event_time','2026-11-10T10:00:00'), ('event_time',None),
                 ('delay_minutes',-1), ('delay_minutes',True), ('delay_minutes',float('nan')),
                 ('delay_minutes',float('inf')), ('delay_minutes',1441), ('delay_minutes',10**500),
                 ('airport','fra'), ('airport',None), ('flight_id',''), ('event_id','bad id')]
        for field, value in cases:
            with self.subTest(field=field, value=value):
                events = deepcopy(self.events)
                events[0][field] = value
                with self.assertRaises(ContractError):
                    summarize(events)

    def test_schema_rejects_unknown_and_missing_fields(self):
        for field in ('unexpected','event_time'):
            event = deepcopy(self.events[0])
            if field == 'unexpected':
                event[field] = 'value'
            else:
                del event[field]
            with self.assertRaises(ContractError):
                summarize([event])

    def test_batch_bounds_and_type(self):
        for value in ([], {}, [None], self.events * 1001):
            with self.subTest(value_type=type(value).__name__):
                with self.assertRaises(ContractError):
                    summarize(value)

    def test_offset_timestamp_and_boundary_delays(self):
        self.events[0]['event_time'] = '2026-11-10T11:00:00+01:00'
        self.events[0]['delay_minutes'] = 1440
        self.assertEqual(summarize(self.events)['accepted'], 3)

class HTTPTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def request(self, method, path, body=None, headers=None):
        conn = http.client.HTTPConnection(*self.server.server_address, timeout=3)
        try:
            conn.request(method, path, body=body, headers=headers or {})
            response = conn.getresponse()
            return response.status, json.loads(response.read())
        finally:
            conn.close()

    def test_health(self):
        self.assertEqual(self.request('GET','/healthz'), (200, {'status':'ok'}))

    def test_version(self):
        self.assertIn('version', self.request('GET','/version')[1])

    def test_unknown_path(self):
        self.assertEqual(self.request('GET','/missing')[0], 404)

    def test_valid_batch(self):
        payload = (ROOT / 'samples/events.json').read_bytes()
        status, result = self.request('POST','/validate',payload,{'Content-Type':'application/json'})
        self.assertEqual((status,result['accepted']), (200,3))

    def test_malformed_json(self):
        self.assertEqual(self.request('POST','/validate','{',{'Content-Type':'application/json'})[0],400)

    def test_invalid_contract(self):
        self.assertEqual(self.request('POST','/validate','[]',{'Content-Type':'application/json'})[0],400)

    def test_wrong_media_type(self):
        self.assertEqual(self.request('POST','/validate','[]',{'Content-Type':'text/plain'})[0],415)

    def test_oversize_declared_body(self):
        self.assertEqual(self.request('POST','/validate',None,
            {'Content-Type':'application/json','Content-Length':str(MAX_BODY+1)})[0],413)

    def test_invalid_declared_body(self):
        self.assertEqual(self.request('POST','/validate',None,
            {'Content-Type':'application/json','Content-Length':'invalid'})[0],400)

if __name__ == '__main__':
    unittest.main()
