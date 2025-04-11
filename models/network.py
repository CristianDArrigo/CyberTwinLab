from typing import List
from pydantic import BaseModel
from models.behavior import Behavior
from models.device import Device


class NetworkConfig(BaseModel):
    name: str
    subnet: str


class FullConfig(BaseModel):
    network: NetworkConfig
    devices: List[Device]
