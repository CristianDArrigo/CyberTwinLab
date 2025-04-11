import yaml
from models.network import FullConfig


def load_config(path: str = "config/network_config.yml") -> FullConfig:
    with open(path, "r") as f:
        # Caricamento sicuro del YAML
        raw = yaml.safe_load(f)
    # Creazione dell'oggetto FullConfig con validazione automatica
    config = FullConfig(**raw)
    return config


if __name__ == "__main__":
    # Test rapido per verificare che il parsing funzioni
    config = load_config()
    print(f"Network: {config.network.name} - {config.network.subnet}")
    for device in config.devices:
        behavior_types = [b.type for b in device.behaviors]
        print(f"Device {device.name} ({device.ip}) ha behaviors: {behavior_types}")
