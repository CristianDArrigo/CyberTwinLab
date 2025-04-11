from typing import List, Optional, Literal, Union
from pydantic import BaseModel, Field
from models.behavior import Behavior


class Device(BaseModel):
    name: str
    hostname: str
    username: str
    ip: str
    type: str
    behaviors: List[Behavior] = Field(default_factory=list)
