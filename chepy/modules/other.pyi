from ..core import ChepyCore as ChepyCore, ChepyDecorators as ChepyDecorators
from typing import Any

class Other(ChepyCore):
    def __init__(self, *data: Any) -> None: ...
    state: Any = ...
    def generate_uuid(self) -> str: ...