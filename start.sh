#!/bin/bash
set -e  # Termina lo script se c'è un errore

echo "---------------------------------------------------"
echo "[INFO] Avvio di CyberTwinLab: Inizializzazione..."
echo "---------------------------------------------------"

# Rimuovi eventuali vecchi script dei behavior e crea la cartella se non esiste
if [ -d "../output/behavior_scripts" ]; then
    rm -rf ../output/behavior_scripts
fi
mkdir -p ../output/behavior_scripts

# Passaggio 1: Parsing della configurazione YAML e validazione via Pydantic
echo "[INFO] Parsing della configurazione (config/network_config.yml)..."
python3 -m scripts.parse_config

# Passaggio 2: Generazione degli script di behavior per ogni dispositivo
echo "[INFO] Generazione degli script dei behavior..."
python3 -m scripts.generate_behavior_script

# Passaggio 3: Generazione del file docker-compose.yml
echo "[INFO] Generazione del file docker-compose.yml..."
python3 -m scripts.generate_docker_compose

# Passaggio 4: Avvio dell'ambiente Docker
echo "[INFO] Avvio dell'ambiente Docker (docker-compose)..."
docker-compose -f ../output/docker-compose.yml up --build -d

echo "---------------------------------------------------"
echo "[INFO] CyberTwinLab è avviato!"
echo "[INFO] Puoi accedere a Kibana su http://localhost:5601 (se il container ELK è configurato)"
echo "---------------------------------------------------"
