#!/bin/bash
# Script to bootstrap Coolify VPS directories and permissions

echo "Bootstrapping Maestro Agent OS Server Directories..."

# Core Data Dirs
mkdir -p ../data/obsidian_vault/{01-Inbox,02-Projetos,03-Zettelkasten,99-Config}
mkdir -p ../data/openfang_db

# Set basic permissions (adjust user if Coolify runs as specfic non-root)
chmod -R 755 ../data

echo "Pulling local embedding model (nomic-embed-text) into Ollama..."
# We assume Ollama is running or will run via docker compose
# Wait for ollama to be up
sleep 5
docker exec maestro_ollama ollama run nomic-embed-text

echo "Setup Complete!"
