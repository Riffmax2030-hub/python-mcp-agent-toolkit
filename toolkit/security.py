import os
from pathlib import Path

class SecurityGuard:
    @staticmethod
    def is_safe_path(base_dir: str, target_path: str) -> bool:
        base = Path(base_dir).resolve()
        target = (base / target_path).resolve()
        return target.is_relative_to(base)

    @staticmethod
    def sanitize_arguments(arguments: dict) -> dict:
        # Prevents command injection markers or suspicious control characters
        sanitized = {}
        for k, v in arguments.items():
            if isinstance(v, str):
                if any(bad in v for bad in [";", "&&", "||", "`", "$("]):
                    raise ValueError(f"Dangerous characters detected in argument '{k}'")
            sanitized[k] = v
        return sanitized
