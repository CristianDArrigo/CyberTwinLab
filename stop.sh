#!/bin/bash
set -e  # Termina lo script se c'è un errore

echo "---------------------------------------------------"
echo "[INFO] Arresto e rimozione dell'ambiente Docker..."
echo "---------------------------------------------------"

# Arresta ed elimina i container definiti nel docker-compose generato
docker-compose -f ../output/docker-compose.yml down --volumes

echo "---------------------------------------------------"
echo "[INFO] CyberTwinLab è stato arrestato ed eliminato."
echo "---------------------------------------------------"
