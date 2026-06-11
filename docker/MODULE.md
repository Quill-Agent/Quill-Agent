# docker

Docker/Podman images and `entrypoint.sh` bootstrap for Quill Agent.

- `entrypoint.sh` — seeds `~/.quill` config into mounted volumes, optional dashboard sidecar, drops privileges via gosu
- Root `Dockerfile` — Python 3.14 image; triggered by `.github/workflows/docker-publish.yml`
- Supports `GROQ_API_KEY`, `OLLAMA_BASE_URL`, and other provider env vars from `.env` at runtime
