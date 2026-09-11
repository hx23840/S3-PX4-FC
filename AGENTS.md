# Repository instructions

## Files and scope

- This repository contains S3-PX4-FC documentation and reusable code. The editable hardware is an EasyEDA Pro project distributed through GitHub Releases; see [the download index](docs/releases.md).
- For hardware work, identify the requested release and read its release notes. Verify the live project and board before editing. Never infer the current circuit from an old export or conversation summary.
- Keep EDA projects, Gerber, BOM/CPL, drawings, models, stage-specific scripts and scratch data outside the Git checkout. Publish project and manufacturing outputs as individual release assets. Do not bundle repository documentation or tools into an all-in-one release archive.
- Keep credentials, account/order details and raw session logs out of public files.

## EDA tools

- Use [easyeda-agent](https://github.com/zhoushoujianwork/easyeda-agent) with EasyEDA Pro. Read the installed easyeda-agent Skill before EDA operations and use its supported actions and validation workflow.
- Keep CLI/daemon, Skill and Connector on matching releases. Use the installed release's help for command syntax. Check the connection before writes:

```sh
easyeda update --check --exit-code
easyeda health --project S3-PX4-FC
```

- Local geometry work uses Python with Shapely/NumPy; operation batches may use JavaScript/Node.js. Mechanical solid checks use Python/OCP. Use editor views and computer/browser tools for visual inspection and native dialogs.

## Hardware changes

- Establish intended connectivity from component identities, datasheets, physical pin numbers and net/NC assignments. Verify symbol-to-footprint mapping; GPIO names are not physical pin numbers.
- Read the current design into local data. Plan placement, orientation and routing before applying a bounded change. Include mounting and connector clearance, signal paths and test access.
- Save a recoverable checkpoint before removing existing copper. After applying, read back affected components and pins against the intended connectivity; run the Skill's checks and native DRC.
- Save, reopen and verify the result. Inspect fresh drawings and manufacturing layers relevant to the change. Report unresolved checks separately; DRC alone does not establish manufacturability or hardware operation.
- Export the native project and manufacturing files from the same saved revision. Follow [release publishing](docs/releasing.md); preserve published attachments and assign a new revision to changed hardware.
- On handoff, record the working project, saved revision, completed changes, remaining checks and next action beside the local working files. Verify live state when resuming.

## Documentation and checks

- Keep instructions in this file concise and in English only. Update existing Chinese counterparts of reader-facing documentation when changing their English versions.
- Maintain documentation in Git and record revision-specific manufacturing and test status in release notes. Preserve the license scopes and third-party attribution defined in [LICENSE.md](LICENSE.md) and [NOTICE.md](NOTICE.md).
- After repository changes, run:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_repository.py
```

- This command checks repository file boundaries, common credential patterns and relative links. Hardware checks must be run separately for hardware changes.
