from dataclasses import dataclass
from typing import Tuple


@dataclass
class Location:
    name: str
    key: str
    coords: Tuple[float, float]
