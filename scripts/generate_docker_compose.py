import os
import yaml
from pathlib import Path
from models.network import (
    FullConfig,
)  # Assicurati che la struttura di import sia corretta
from scripts.parse_config import load_config
from models.device import Device

OUTPUT_FILE = "../output/docker-compose.yml"


def generate_service_block(device: Device) -> dict:
    """
    Genera il blocco servizio per il device.
    Per ora assume che il device utilizzi il Dockerfile presente in devices/<type>/
    e che il relativo behavior script sia montato da ./output/behavior_scripts/<device.name>.sh.
    """
    service = {
        device.name: {
            "build": f"../devices/{device.type}",
            "container_name": device.name,
            "networks": {"net1": {"ipv4_address": device.ip}},
            "volumes": [
                f"./output/behavior_scripts/{device.name}.sh:/opt/entrypoint_behavior.sh:ro"
            ],
        }
    }
    return service


def generate_docker_compose(config: FullConfig) -> dict:
    services = {}
    for device in config.devices:
        services.update(generate_service_block(device))

    # Aggiungiamo il servizio ELK per il logging centralizzato
    services["elk"] = {
        "image": "sebp/elk",
        "container_name": "elk",
        "ports": ["5601:5601"],  # Kibana accessibile dall'esterno
        "networks": {"net1": {"ipv4_address": "192.168.100.200"}},
    }

    compose = {
        "version": "3.9",
        "services": services,
        "networks": {
            "net1": {
                "driver": "bridge",
                "ipam": {"config": [{"subnet": config.network.subnet}]},
            }
        },
    }
    return compose


def write_compose_file(compose_dict: dict, output_path: str = OUTPUT_FILE):
    path = Path(output_path)
    # Assicurati che la directory di destinazione esista
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        yaml.dump(compose_dict, f, sort_keys=False)
    print(f"Docker Compose file scritto in: {path.resolve()}")


if __name__ == "__main__":
    # Carica la configurazione dal file YAML usando lo script di parse_config.py
    config = load_config()
    compose_dict = generate_docker_compose(config)
    write_compose_file(compose_dict)
