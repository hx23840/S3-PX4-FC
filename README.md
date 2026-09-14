# S3-PX4-FC

English | [简体中文](README.zh-CN.md)

An ESP32-S3 flight-controller hardware project, designed by Peter using Codex + GPT-6 Astra.

https://github.com/user-attachments/assets/9a856ec8-94fd-4361-a7dd-2fc33b27a7e5

**[Explore the assembly in 3D](https://s3-px4-assembly.pages.dev/)**

The design includes an IMU, barometer, microSD storage, four ESC control outputs and receiver, GNSS and camera interfaces. PX4 is the intended firmware platform; board support and first-board testing are unfinished. PCB manufacturing has been submitted.

## Develop with AI

1. Install EasyEDA Pro and the matching CLI, Skill and Connector from [easyeda-agent](https://github.com/zhoushoujianwork/easyeda-agent).
2. Open this repository in Codex and import the selected hardware release's `.epro2` into EasyEDA Pro.
3. Give Codex the project location and the change you want to make. Codex loads the repository instructions from [AGENTS.md](AGENTS.md).

## Hardware downloads

Download the editable `.epro2` project, Gerber, BOM and placement files as individual GitHub Release attachments. See [downloads and version contents](docs/releases.md).

[Development history](CHANGELOG.md) lists the design changes.

## Repository

- [docs/](docs/README.md): hardware downloads and release instructions.
- [scripts/](scripts/README.md): repository checks.
- [Contributing](CONTRIBUTING.md): reporting issues and proposing changes.

Hardware: **CERN-OHL-P-2.0**. Code: **MIT**. Documentation: **CC BY 4.0**. See [license scope](LICENSE.md) and [third-party notices](NOTICE.md).
