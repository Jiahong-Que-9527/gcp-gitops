"""[房玄龄·2026-11-10] Contract for synthetic engineering events, not airport facts."""
from datetime import datetime
import math
import re

FIELDS = {'event_id', 'flight_id', 'event_time', 'airport', 'delay_minutes', 'synthetic'}

class ContractError(ValueError):
    pass

def summarize(events):
    if not isinstance(events, list) or not 1 <= len(events) <= 1000:
        raise ContractError('expected a nonempty array with at most 1000 events')
    seen = set()
    delays = []
    for index, event in enumerate(events):
        if not isinstance(event, dict) or set(event) != FIELDS:
            raise ContractError(f'event {index}: unexpected or missing fields')
        for field in ('event_id', 'flight_id'):
            value = event[field]
            if not isinstance(value, str) or not re.fullmatch(r'[A-Za-z0-9_-]{1,64}', value):
                raise ContractError(f'event {index}: invalid {field}')
        if event['event_id'] in seen:
            raise ContractError(f'event {index}: duplicate event_id in batch')
        seen.add(event['event_id'])
        if event['synthetic'] is not True:
            raise ContractError(f'event {index}: only synthetic events are accepted')
        if not isinstance(event['airport'], str) or not re.fullmatch(r'[A-Z]{3}', event['airport']):
            raise ContractError(f'event {index}: airport must be a three-letter code')
        try:
            value = event['event_time']
            if not isinstance(value, str) or 'T' not in value:
                raise ValueError('not an ISO timestamp')
            timestamp = datetime.fromisoformat(value.replace('Z', '+00:00'))
            if timestamp.tzinfo is None or timestamp.utcoffset() is None:
                raise ValueError('missing timezone')
        except (ValueError, TypeError):
            raise ContractError(f'event {index}: invalid timezone-aware event_time') from None
        delay = event['delay_minutes']
        if type(delay) not in (int, float) or not 0 <= delay <= 1440 or not math.isfinite(delay):
            raise ContractError(f'event {index}: delay_minutes must be finite, between 0 and 1440')
        delays.append(delay)
    return {
        'accepted': len(events),
        'mean_delay_minutes': round(sum(delays) / len(delays), 3),
        'synthetic': True,
    }
