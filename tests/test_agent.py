import unittest
import asyncio
from servers.data_tools_server import DataToolsServer
from toolkit.agent import MCPAgent
from toolkit.security import SecurityGuard

class TestMCPAgent(unittest.IsolatedAsyncioTestCase):
    async def test_tool_execution(self):
        agent = MCPAgent()
        server = DataToolsServer()
        agent.register_server(server)

        res = await agent.execute_tool_call(
            "data-tools-server", "calculate_statistics", {"numbers": [2, 4, 6]}
        )
        self.assertEqual(res["mean"], 4.0)
        self.assertEqual(res["count"], 3)

    def test_security_sanitization(self):
        with self.assertRaises(ValueError):
            SecurityGuard.sanitize_arguments({"cmd": "test; rm -rf /"})

if __name__ == "__main__":
    unittest.main()
