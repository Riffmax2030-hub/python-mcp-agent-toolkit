import asyncio
from servers.data_tools_server import DataToolsServer
from toolkit.agent import MCPAgent

async def main():
    agent = MCPAgent()
    server = DataToolsServer()
    agent.register_server(server)

    print("=== Registered MCP Tools ===")
    for tool in agent.get_available_tools():
        print(f"- {tool['name']}: {tool['description']}")

    print("\n=== Agent Executing Tool Call ===")
    sample_data = [10.5, 12.0, 11.2, 10.8, 145.0, 11.5, 12.2]  # includes outlier (145.0)
    print(f"Raw data: {sample_data}")

    # Step 1: Calculate initial statistics
    stats = await agent.execute_tool_call(
        "data-tools-server", "calculate_statistics", {"numbers": sample_data}
    )
    print(f"Initial Stats: Mean={stats['mean']}, Variance={stats['variance']}")

    # Step 2: Filter outliers
    clean = await agent.execute_tool_call(
        "data-tools-server", "filter_outliers", {"numbers": sample_data, "threshold": 2.0}
    )
    print(f"Filtered Data: {clean['clean_numbers']} (Removed {clean['outliers_removed']} outlier(s))")

    # Step 3: Recalculate clean statistics
    clean_stats = await agent.execute_tool_call(
        "data-tools-server", "calculate_statistics", {"numbers": clean["clean_numbers"]}
    )
    print(f"Clean Stats: Mean={clean_stats['mean']}, Variance={clean_stats['variance']}")

if __name__ == "__main__":
    asyncio.run(main())
