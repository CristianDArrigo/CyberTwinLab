import textwrap
from devices.behavior.base import BaseBehavior


class PingBehavior(BaseBehavior):
    def __init__(self, interval: int, target: str):
        self.interval = interval
        self.target = target

    def init(self, **kwargs):
        self.interval = kwargs.get("interval", 60)
        self.target = kwargs.get("target", "http://example.com")

    def generate_bash(self) -> str:
        script = f"""
        while true; do
            ping -c 1 {self.target} > /dev/null 2>&1
            if [ $? -eq 0 ]; then
                logger "[{{DEVICE}}] PING {self.target} SUCCESS"
            else
                logger "[{{DEVICE}}] PING {self.target} FAIL"
            fi
            sleep {self.interval}
        done &
        """
        return textwrap.dedent(script)
