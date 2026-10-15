import asyncio
from typing import Dict, Any, List
from servers.base import BaseMCPServer
from toolkit.security import SecurityGuard

class MCPAgent:
    def __init__(self):
        self.servers: Dict[str, BaseMCPServer] = {}

    def register_server(self, server: BaseMCPServer):
        self.servers[server.server_name] = server

    def get_available_tools(self) -> List[Dict[str, Any]]:
        all_tools = []
        for server in self.servers.values():
            all_tools.extend(server.list_tools())
        return all_tools

    async def execute_tool_call(self, server_name: str, tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        if server_name not in self.servers:
            raise KeyError(f"Server '{server_name}' is not registered.")
        
        # Sanitize parameters
        clean_args = SecurityGuard.sanitize_arguments(arguments)
        
        # Execute tool
        server = self.servers[server_name]
        return await server.call_tool(tool_name, clean_args)
