import textwrap
from devices.behavior.base import BaseBehavior


class IdleBehavior(BaseBehavior):
    def __init__(self, interval: int = 60):
        self.interval = interval

    def init(self, **kwargs):
        super().__init__(**kwargs)
        # Inizializza l'intervallo a 60 secondi se non fornito
        self.interval = kwargs.get("interval", 60)

    def generate_bash(self) -> str:
        # Genera uno script che logga "Idle" ogni interval secondi
        script = f"""
        while true; do
            logger "[{{DEVICE}}] Idle: waiting for {self.interval} seconds"
            sleep {self.interval}
        done &
        """
        # Uso textwrap.dedent per rimuovere indentazioni indesiderate
        return textwrap.dedent(script)
