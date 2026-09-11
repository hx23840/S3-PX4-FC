# Publishing a hardware version

English | [简体中文](releasing.zh-CN.md)

EDA project history tracks circuit changes. Git tracks repository documentation and reusable code. A GitHub Release distributes an identified hardware snapshot and its outputs.

1. Freeze the design under a hardware revision in EasyEDA. Export the `.epro2`, Gerber, BOM, placement files and relevant drawings from that design.
2. Keep exports in a version folder outside the Git checkout. Keep documentation and reusable tools in Git. Inspect the exported files and reopen the `.epro2`.
3. Update the development history and download index in Git. Review both language versions and run `python3 scripts/check_repository.py`.
4. Tag the reviewed documentation/code revision with the hardware version. Create the matching GitHub Release and attach the project, Gerber, BOM and placement files individually, together with checksums. Keep Gerber layers in their fabrication ZIP; do not create an all-in-one project/documentation bundle.
5. Describe the circuit changes and test/manufacturing status in the release notes. Add its published URL to the download index.

Preserve published attachments for that revision. Changed project or manufacturing files receive a new revision and Release. Private order and account information stays outside public attachments.
