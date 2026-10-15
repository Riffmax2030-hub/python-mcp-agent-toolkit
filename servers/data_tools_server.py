import statistics
from typing import Dict, Any, List
from servers.base import BaseMCPServer

class DataToolsServer(BaseMCPServer):
    def __init__(self):
        super().__init__("data-tools-server")

    def list_tools(self) -> List[Dict[str, Any]]:
        return [
            {
                "name": "calculate_statistics",
                "description": "Calculates summary statistics (mean, median, stdev) for a list of numbers.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "numbers": {"type": "array", "items": {"type": "number"}}
                    },
                    "required": ["numbers"]
                }
            },
            {
                "name": "filter_outliers",
                "description": "Filters numbers exceeding a standard score threshold.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "numbers": {"type": "array", "items": {"type": "number"}},
                        "threshold": {"type": "number", "default": 2.0}
                    },
                    "required": ["numbers"]
                }
            }
        ]

    async def call_tool(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        if name == "calculate_statistics":
            nums = arguments.get("numbers", [])
            if not nums:
                raise ValueError("Numbers array cannot be empty")
            return {
                "count": len(nums),
                "mean": round(statistics.mean(nums), 3),
                "median": round(statistics.median(nums), 3),
                "variance": round(statistics.variance(nums), 3) if len(nums) > 1 else 0.0
            }
        elif name == "filter_outliers":
            nums = arguments.get("numbers", [])
            thresh = arguments.get("threshold", 2.0)
            if len(nums) < 2:
                return {"clean_numbers": nums}
            mean = statistics.mean(nums)
            stdev = statistics.stdev(nums)
            clean = [x for x in nums if abs(x - mean) <= thresh * stdev]
            return {"clean_numbers": clean, "outliers_removed": len(nums) - len(clean)}
        else:
            raise KeyError(f"Tool {name} not found on server {self.server_name}")
