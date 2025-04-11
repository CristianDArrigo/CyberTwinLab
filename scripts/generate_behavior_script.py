import os
from models.network import FullConfig
from pathlib import Path
import yaml


# Immaginiamo di avere già la funzione load_config definita
def load_config(path: str = "config/network_config.yml") -> FullConfig:
    with open(path, "r") as f:
        raw = yaml.safe_load(f)
    return FullConfig(**raw)


# Supponiamo di avere già delle classi Behavior specifiche con un metodo generate_bash()
# Per l'esempio userò una logica fittizia per il behavior "ping"
def generate_behavior_script(device) -> str:
    # Se il dispositivo non ha comportamenti definiti, assegna un default idle
    if not device.behaviors:
        return f"""
while true; do
    logger "[{device.name}] IDLE: nessuna attività configurata, attesa di 60 secondi"
    sleep 60
done &
"""
    # Se sono presenti behavior, concatena gli script generati.
    # Qui mostro un esempio per il comportamento "ping"
    script_parts = []
    for behavior in device.behaviors:
        if behavior.type.lower() == "ping":
            # Genera uno snippet bash per il ping, usando i parametri
            script = f"""
while true; do
    ping -c 1 {behavior.target} > /dev/null 2>&1
    if [ $? -eq 0 ]; then
        logger "[{device.name}] PING {behavior.target} SUCCESS"
    else
        logger "[{device.name}] PING {behavior.target} FAIL"
    fi
    sleep {behavior.interval}
done &
"""
            script_parts.append(script)
        elif behavior.type.lower() == "curl":
            script = f"""
while true; do
    code=$(curl -s -o /dev/null -w "%{{http_code}}" {behavior.url})
    logger "[{device.name}] CURL {behavior.url} -> $code"
    sleep {behavior.interval}
done &
"""
            script_parts.append(script)
        # elif ...
        else:
            # Puoi aggiungere altri comportamenti qui
            script_parts.append(
                f'logger "[{device.name}] Comportamento {behavior.type} non ancora implementato"'
            )
    return "\n".join(script_parts)


def generate_all_behavior_scripts(
    config: FullConfig, output_dir: str = "../output/behavior_scripts"
):
    os.makedirs(output_dir, exist_ok=True)
    for device in config.devices:
        script = generate_behavior_script(device)
        # Salva lo script in un file denominato in base al device, ad es. pc1.sh
        file_path = Path(output_dir) / f"{device.name}.sh"
        file_path.write_text(script)
        print(f"Script per {device.name} generato in {file_path}")


if __name__ == "__main__":
    config = load_config()
    generate_all_behavior_scripts(config)
