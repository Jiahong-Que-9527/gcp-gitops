"""[房玄龄·2026-11-10] Check an already-running reference container over HTTP."""
import json
from pathlib import Path
import time
import urllib.error
import urllib.request

base = 'http://127.0.0.1:8080'
for attempt in range(30):
    try:
        with urllib.request.urlopen(base+'/healthz', timeout=2) as response:
            assert json.load(response) == {'status':'ok'}
        break
    except (OSError, AssertionError):
        if attempt == 29:
            raise
        time.sleep(1)
payload=(Path(__file__).resolve().parents[1]/'samples/events.json').read_bytes()
request=urllib.request.Request(base+'/validate',data=payload,headers={'Content-Type':'application/json'})
with urllib.request.urlopen(request,timeout=5) as response:
    result=json.load(response)
    assert result['accepted']==3 and result['mean_delay_minutes']==5.0, result
invalid=urllib.request.Request(base+'/validate',data=b'[]',headers={'Content-Type':'application/json'})
try:
    urllib.request.urlopen(invalid,timeout=5)
except urllib.error.HTTPError as error:
    assert error.code==400, error.code
else:
    raise AssertionError('empty event batch must fail')
print('Container HTTP smoke passed: health, fixture aggregate and invalid-batch rejection')
