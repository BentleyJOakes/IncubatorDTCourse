# DTaaS Localhost Zip + uv Setup

This quick guide covers:

1. Where and how to download the `dtaas-workspace-on-localhost` zip
2. How to install `uv`

## 1) Download `dtaas-workspace-on-localhost` zip

### Option A: Download from DTaaS GitHub Releases

1. Open the DTaaS releases page:
   - https://github.com/into-cps-association/DTaaS/releases
2. Open the latest release (or the version required by your course/lab).
3. In **Assets**, download:
   - `dtaas-workspace-on-localhost-<version>.zip`

### Option B: Download with `curl`

Replace `<version>` with the release tag (example: `.v10-beta`):

```bash
cd ~/Downloads
curl -fL -o dtaas-workspace-on-localhost-<version>.zip \
  https://github.com/into-cps-association/DTaaS/releases/download/<version>/dtaas-workspace-on-localhost-<version>.zip
```

### Option C: Use the local copy already present in this workspace

If you are working in this lab folder, the zip may already exist at:

- `IncubatorDTCourse/10-DTaaS-FlexCell/dtaas-workspace-on-localhost-v1.0-beta.zip`

## 2) Install `uv`

Official install command (Linux/macOS):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then reload your shell and verify:

```bash
uv --version
```

If `uv` is not found after install, add this to your shell profile (`~/.bashrc` or `~/.zshrc`):

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Then reload and verify again:

```bash
# Reload the shell profile you edited above:
source ~/.bashrc   # if you edited ~/.bashrc
source ~/.zshrc    # if you edited ~/.zshrc
uv --version
```

## Notes

- `uv` is used in this lab to create virtual environments and install Python dependencies quickly.
