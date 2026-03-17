# Maestro Agent OS

Agent Operating System orchestrating `OpenFang` with `OpenViking` Memory Context and `TickTick` for zero-friction productivity.

## Project Structure

- `/infra`: Docker compose and scripts to bootstrap the Bare-Metal instance (Coolify compatible).
- `/agents`: Agent Hand manifests (.toml) defining LLMs, persona and tools.
- `/capabilities`: Native or proxied code bridging external tools (OpenViking API, MCP TickTick API, Gemini CLI for FinOps).
- `/data`: Existent or dynamically generated volume mounts (like the Obsidian Vault).

## Bootstrapping Local

```bash
cd infra
./setup-coolify.sh
docker-compose up -d
```
