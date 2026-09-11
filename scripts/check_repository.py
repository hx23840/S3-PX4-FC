#!/usr/bin/env python3
"""Check repository files without requiring hardware release assets."""
import argparse
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit
from privacy_checks import text_findings

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {'.gitignore', '.gitattributes', 'README.md', 'LICENSE.md',
            'NOTICE.md', 'CONTRIBUTING.md', 'CHANGELOG.md'}
EXCLUDED_ROOTS = {'hardware', 'production', 'mechanical', 'preview', 'release-assets',
                  'releases', 'engineering', 'history', 'work', 'outputs', 'output'}
EXCLUDED_PARTS = {'node_modules', 'dist', '.wrangler', '.playwright-cli',
                  '__pycache__', '.git', '.easyeda'}
ARTIFACT_SUFFIXES = {'.epro', '.epro2', '.eprj2', '.epru', '.elibz', '.zip', '.tar',
                     '.gz', '.7z', '.pdf', '.csv', '.step', '.stp', '.stl', '.dxf',
                     '.brep', '.bin', '.gtl', '.gbl', '.g1', '.g2', '.gto', '.gbo',
                     '.gts', '.gbs', '.gtp', '.gbp', '.gko', '.gdl', '.gdd', '.drl'}
LINK = re.compile(r'!?\[[^\]]*\]\(([^)]+)\)')


def check(root=ROOT):
    root = Path(root).resolve()
    result = subprocess.run(
        ['git', '-C', str(root), 'ls-files', '--cached', '--others', '--exclude-standard', '-z'],
        check=True, capture_output=True,
    )
    names = {n.decode('utf-8') for n in result.stdout.split(b'\0') if n}
    problems = []
    if not REQUIRED <= names:
        problems.append(f'Missing repository files: {sorted(REQUIRED - names)}')
    for name in sorted(names):
        rel = Path(name)
        p = root / rel
        if (rel.parts[0] in EXCLUDED_ROOTS or p.suffix.lower() in ARTIFACT_SUFFIXES
                or re.search(r'(?:^|/)[Vv]\d+(?:[._-]\d+)*(?:[-_]R\d+)?(?:[._-]|/)', name)):
            problems.append(f'{name}: release artifact or hardware-stage snapshot in Git')
        if (any(part in EXCLUDED_PARTS for part in rel.parts)
                or p.name in {'.DS_Store', 'PROJECT_STATUS.md'} or p.name.startswith('._')
                or (p.name.startswith('.env') and p.name != '.env.example')
                or p.suffix in {'.log', '.pyc', '.sqlite', '.sqlite-wal', '.sqlite-shm'}):
            problems.append(f'{name}: local/private file in Git')
        if p.is_symlink() or not p.is_file() or not p.resolve().is_relative_to(root):
            problems.append(f'{name}: missing or non-regular repository file')
            continue
        data = p.read_bytes()
        try:
            text = data.decode('utf-8-sig')
        except UnicodeDecodeError:
            problems.append(f'{name}: binary file belongs in release assets')
            continue
        problems.extend(f'{name}: {rule}' for rule in text_findings(text))
        if p.suffix == '.json':
            try:
                json.loads(text)
            except ValueError:
                problems.append(f'{name}: invalid JSON')
        if p.suffix != '.md':
            continue
        if text.count('```') % 2:
            problems.append(f'{name}: unmatched code fence')
        prose = re.sub(r'```.*?```', '', text, flags=re.S)
        for target in LINK.findall(prose):
            target = target.strip().strip('<>')
            parsed = urlsplit(target)
            if parsed.scheme or target.startswith('#'):
                continue
            resolved = (p.parent / unquote(parsed.path)).resolve()
            try:
                wanted = resolved.relative_to(root).as_posix()
            except ValueError:
                problems.append(f'{name}: link outside repository')
                continue
            if wanted not in names:
                problems.append(f'{name}: missing or excluded link: {target}')
    if problems:
        raise ValueError('\n'.join(problems))
    return {'repositoryFiles': len(names), 'result': 'passed',
            'checks': ['release-artifact exclusion', 'local/private-file exclusion',
                       'common credential patterns', 'relative Markdown links'],
            'limits': 'Checks this working tree; does not inspect Git history or hardware release contents.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    args = parser.parse_args()
    try:
        print(json.dumps(check(args.root), ensure_ascii=False, indent=2))
    except (ValueError, OSError, subprocess.CalledProcessError) as exc:
        print(str(exc), file=sys.stderr)
        sys.exit(1)
