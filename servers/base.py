from abc import ABC, abstractmethod
from typing import Dict, Any, List

class BaseMCPServer(ABC):
    def __init__(self, server_name: str):
        self.server_name = server_name
        self.tools: Dict[str, Any] = {}

    @abstractmethod
    def list_tools(self) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    async def call_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        pass
