# Udhëzuesi i Zgjidhjes së Problemeve — Lahuta

## Kuptimi i Arkitekturës së Lahuta

Sistemi Lahuta është krijuar për të lehtësuar ndërveprimet midis klientit (shfletuesit tuaj) dhe API-së së Ollama/OpenAI. Në thelb të këtij dizajni është një reverse proxy në prapaskenë (backend), që rrit sigurinë dhe zgjidh problemet e CORS.

- **Si funksionon**: Lahuta ndërvepron me API-në e modeleve përmes rrugëve të sigurta në backend. Kur dërgohet një kërkesë nga ndërfaqja në drejtim të Ollama, kërkesa kalon fillimisht te backend-i i Lahuta përmes rrugës `/ollama`, dhe më pas përcillet te serveri i synuar.

## Lahuta: Gabim Lidhjeje me Serverin (Server Connection Error)

If you're experiencing connection issues, it’s often due to the WebUI docker container not being able to reach the Ollama server at 127.0.0.1:11434 (host.docker.internal:11434) inside the container . Use the `--network=host` flag in your docker command to resolve this. Note that the port changes from 3000 to 8080, resulting in the link: `http://localhost:8080`.

**Example Docker Command**:

```bash
docker run -d --network=host -v open-webui:/app/backend/data -e OLLAMA_BASE_URL=http://127.0.0.1:11434 --name open-webui --restart always ghcr.io/open-webui/open-webui:main
```

### Error on Slow Responses for Ollama

Open WebUI has a default timeout of 5 minutes for Ollama to finish generating the response. If needed, this can be adjusted via the environment variable AIOHTTP_CLIENT_TIMEOUT, which sets the timeout in seconds.

### General Connection Errors

**Ensure Ollama Version is Up-to-Date**: Always start by checking that you have the latest version of Ollama. Visit [Ollama's official site](https://ollama.com/) for the latest updates.

**Troubleshooting Steps**:

1. **Verify Ollama URL Format**:
   - When running the Web UI container, ensure the `OLLAMA_BASE_URL` is correctly set. (e.g., `http://192.168.1.1:11434` for different host setups).
   - In the Open WebUI, navigate to "Settings" > "General".
   - Confirm that the Ollama Server URL is correctly set to `[OLLAMA URL]` (e.g., `http://localhost:11434`).

By following these enhanced troubleshooting steps, connection issues should be effectively resolved. For further assistance or queries, feel free to reach out to us on our community Discord.
