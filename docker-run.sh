#!/usr/bin/env bash
set -euo pipefail

<<<<<<< Updated upstream
# Build and run the Open WebUI Docker container locally.

readonly IMAGE="open-webui"
readonly CONTAINER="open-webui"
=======
# Build and run the Lahuta Docker container locally.

readonly IMAGE="sghtf/lahuta-ui"
readonly CONTAINER="lahuta-ui"
>>>>>>> Stashed changes
readonly HOST_PORT="${OPEN_WEBUI_PORT:-3000}"
readonly CONTAINER_PORT=8080

echo "Building ${IMAGE} image..."
docker build -t "$IMAGE" .

echo "Stopping any existing ${CONTAINER} container..."
docker stop "$CONTAINER" 2>/dev/null || true
docker rm "$CONTAINER" 2>/dev/null || true

echo "Starting ${CONTAINER}..."
docker run -d \
  -p "${HOST_PORT}:${CONTAINER_PORT}" \
<<<<<<< Updated upstream
  --add-host=host.docker.internal:host-gateway \
  -v "${IMAGE}:/app/backend/data" \
=======
  -e OLLAMA_BASE_URL="${OLLAMA_BASE_URL:-http://host.docker.internal:11434}" \
  --add-host=host.docker.internal:host-gateway \
  -v "lahuta-ui:/app/backend/data" \
>>>>>>> Stashed changes
  --name "$CONTAINER" \
  --restart always \
  "$IMAGE"

echo "Cleaning up dangling images..."
docker image prune -f

<<<<<<< Updated upstream
echo "Open WebUI is running at http://localhost:${HOST_PORT}"
=======
echo "Lahuta is running at http://localhost:${HOST_PORT}"
>>>>>>> Stashed changes
