import textwrap
from devices.behavior.base import BaseBehavior


class CurlBehavior(BaseBehavior):
    def __init__(self, interval: int, url: str):
        self.interval = interval
        self.url = url

    def init(self, **kwargs):
        super().__init__(**kwargs)
        self.interval = kwargs.get("interval", 60)
        self.url = kwargs.get("url", "http://example.com")

    def generate_bash(self) -> str:
        script = f"""
        while true; do
            code=$(curl -s -o /dev/null -w "%{{http_code}}" {self.url})
            logger "[{{DEVICE}}] CURL {self.url} -> $code"
            sleep {self.interval}
        done &
        """
        return textwrap.dedent(script)
