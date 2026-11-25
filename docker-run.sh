#!/usr/bin/env bash
set -euo pipefail

# Build and run the Lahuta Docker container locally.

readonly IMAGE="sghtf/lahuta-ui"
readonly CONTAINER="lahuta-ui"
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
  -e OLLAMA_BASE_URL="${OLLAMA_BASE_URL:-http://host.docker.internal:11434}" \
  --add-host=host.docker.internal:host-gateway \
  -v "lahuta-ui:/app/backend/data" \
  --name "$CONTAINER" \
  --restart always \
  "$IMAGE"

echo "Cleaning up dangling images..."
docker image prune -f

echo "Lahuta is running at http://localhost:${HOST_PORT}"
