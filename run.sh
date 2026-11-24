#!/bin/bash

image_name="lahuta-ui"
container_name="lahuta-ui"
host_port=3000
container_port=8080

docker build -t "$image_name" .
docker stop "$container_name" &>/dev/null || true
docker rm "$container_name" &>/dev/null || true

docker run -d -p "$host_port":"$container_port" \
    -e OLLAMA_BASE_URL="${OLLAMA_BASE_URL:-http://host.docker.internal:11434}" \
    --add-host=host.docker.internal:host-gateway \
    -v "${image_name}:/app/backend/data" \
    --name "$container_name" \
    --restart always \
    "$image_name"

docker image prune -f
