"""[房玄龄·2026-11-10] Offline data-contract baseline; no cloud API calls."""
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'apps/event-api'))
from contract import ContractError, summarize

if __name__ == '__main__':
    try:
        result = summarize(json.loads(Path(sys.argv[1]).read_text(encoding='utf-8')))
    except (IndexError, OSError, ValueError, ContractError) as exc:
        print(f'replay failed: {exc}', file=sys.stderr)
        raise SystemExit(1)
    print(json.dumps(result, sort_keys=True))
