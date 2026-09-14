# S3-PX4-FC

[English](README.md) | 简体中文

基于 ESP32-S3 的飞控硬件项目，由 Peter 使用 Codex + GPT-6 Astra 设计。

https://github.com/user-attachments/assets/9a856ec8-94fd-4361-a7dd-2fc33b27a7e5

**[打开在线装配预览](https://s3-px4-assembly.pages.dev/)**

设计包含惯性传感器、气压计、microSD、四路电调控制输出，以及接收机、GNSS 和摄像头接口。目标固件平台为 PX4，板级支持及首板测试尚未完成，PCB 制造已提交。

## 使用 AI 开发

1. 安装嘉立创 EDA 专业版，以及 [easyeda-agent](https://github.com/zhoushoujianwork/easyeda-agent) 配套的 CLI、Skill 和 Connector。
2. 在 Codex 中打开本仓库，将所选硬件版本的 `.epro2` 导入 EDA。
3. 告诉 Codex 工程位置和需要完成的修改。Codex 会从 [AGENTS.md](AGENTS.md) 加载仓库指令。

## 硬件下载

可编辑 `.epro2` 工程、Gerber、BOM 和贴装坐标分别作为 GitHub Release 附件提供。参见[下载与版本内容](docs/releases.zh-CN.md)。

[开发记录](CHANGELOG.zh-CN.md)列出设计改动。

## 仓库内容

- [docs/](docs/README.zh-CN.md)：硬件下载和版本发布说明。
- [scripts/](scripts/README.zh-CN.md)：仓库检查。
- [贡献指南](CONTRIBUTING.zh-CN.md)：报告问题与提出修改。

硬件：**CERN-OHL-P-2.0**；代码：**MIT**；文档：**CC BY 4.0**。参见[许可范围](LICENSE.zh-CN.md)和[第三方说明](NOTICE.zh-CN.md)。
