# Repository checks

English | [简体中文](README.zh-CN.md)

From the repository root, run with Python 3 and Git:

```sh
python3 scripts/check_repository.py
```

Checks Git-visible files for release artifacts, local/private files, common credential patterns and broken relative Markdown links. It does not require an EDA project or a particular hardware version.

Tools tied to a hardware snapshot are distributed with that version's release assets.
