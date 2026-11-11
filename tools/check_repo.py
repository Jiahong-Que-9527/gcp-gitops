"""[房玄龄·2026-11-10] Check the learning DAG, document links and evidence claims."""
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
catalog = json.loads((ROOT / 'catalog.json').read_text(encoding='utf-8'))['labs']
labs = {x['id']: x for x in catalog}
if len(labs) != len(catalog):
    errors.append('duplicate lab IDs')
valid = {'planned','local-validated','cloud-validated','demonstrated'}
for lab in catalog:
    if not (ROOT / lab['path']).is_file():
        errors.append(f"missing lab guide: {lab['id']}")
    if lab['status'] not in valid:
        errors.append(f"invalid status: {lab['id']}")
    if lab['status'] != 'planned' and not lab['evidence']:
        errors.append(f"status without evidence: {lab['id']}")
    for path in lab['evidence']:
        if not (ROOT / path).is_file():
            errors.append(f'missing evidence: {path}')
    for dep in lab['prerequisites']:
        if dep not in labs:
            errors.append(f"unknown prerequisite: {lab['id']} -> {dep}")
visiting, visited = set(), set()
def visit(ident):
    if ident in visiting:
        errors.append(f'prerequisite cycle at {ident}')
        return
    if ident in visited or ident not in labs:
        return
    visiting.add(ident)
    for dep in labs[ident]['prerequisites']:
        visit(dep)
    visiting.remove(ident)
    visited.add(ident)
for ident in labs:
    visit(ident)
docs = [ROOT / 'README.md', ROOT / 'AGENTS.md']
for folder in ('docs','labs','evidence','infra','gitops','apps','course'):
    docs.extend((ROOT / folder).rglob('*.md'))
for path in docs:
    for link in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
        if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', link) or link.startswith('#'):
            continue
        target = link.split('#',1)[0]
        if not (path.parent / target).exists():
            errors.append(f'{path.relative_to(ROOT)}: broken link {target}')
if errors:
    print('\n'.join(errors), file=sys.stderr)
    raise SystemExit(1)
print(f'OK: {len(catalog)} labs; prerequisite DAG, evidence paths and {len(docs)} Markdown files checked')
