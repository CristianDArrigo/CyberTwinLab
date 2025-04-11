from typing import List, Optional, Literal, Union
from pydantic import BaseModel, Field


class BaseBehavior(BaseModel):
    type: str  # Type of behavior, e.g., 'idle', 'ping', 'curl'


class PingBehavior(BaseModel):
    type: Literal["ping"]
    interval: int = Field(default=60, description="Interval in seconds")
    target: str = Field(
        default="http://example.com", description="Target URL or IP address"
    )


class CurlBehavior(BaseModel):
    type: Literal["curl"]
    interval: int = Field(default=60, description="Interval in seconds")
    url: str = Field(default="http://example.com", description="URL to curl")


class HydraBehavior(BaseBehavior):
    type: Literal["Hydra"]
    interval: int
    target_url: str
    username: str
    wordlist: str


Behavior = Union[PingBehavior, CurlBehavior, HydraBehavior]
