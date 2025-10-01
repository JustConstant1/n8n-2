# n8n workspace

Minimal setup for running n8n locally with Docker and a small AutoGen smoke test.

## Prerequisites
- Docker and Docker Compose
- Python 3.10+ (only if you want to run the AutoGen demo in `scripts/`)

## Getting started
1. Copy your environment secrets outside of the repository. Use `docs/SET_OPENAI_KEY.ps1` to set `OPENAI_API_KEY` for the current PowerShell session: `./docs/SET_OPENAI_KEY.ps1 -OpenAIKey "sk-..."`.
2. Launch n8n: `docker compose up -d`. The UI is available at http://localhost:5678.
3. Persisted state and credentials are stored under `n8n-data/` (ignored by Git).

## AutoGen demo
1. Ensure `OPENAI_API_KEY` is set in your environment.
2. Install dependencies for the demo: `pip install autogen-agentchat autogen-ext`.
3. Run `python scripts/autogen_chat.py` to verify the integration.

## SSH template
The file `docs/ssh-connection-template.txt` shows the expected SSH command shape without exposing real hosts or private key paths. Replace the placeholders with your own values when connecting to a server.

## Next steps before pushing
- Verify there are no secrets in tracked files.
- Run `git init`, add a remote on GitHub, and commit the files you want to publish.
- Consider adding workflow documentation or environment provisioning scripts if collaborators need them.
