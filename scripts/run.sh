#!/usr/bin/env bash
set -euo pipefail

echo "Stopping previous containers..."
docker compose down --remove-orphans --volumes

echo "Building and starting services..."
docker compose up -d --build

echo "Running containers:"
docker compose ps
