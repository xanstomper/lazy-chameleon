"""llama_4_maverick - reasoning examples."""
from __future__ import annotations
from typing import Any, Dict, List

llama_4_maverick_reasoning_examples: List[Dict[str, Any]] = [
    {"instruction": "Bat $1 more, total $1.10, ball cost?", "response": "$0.05. x+(x+1)=1.10.", "difficulty": 0.3},
    {"instruction": "3 pills every 30 min, how long?", "response": "1 hour. 0, 30, 60.", "difficulty": 0.3},
    {"instruction": "Clock hands overlap in 24h?", "response": "22 times.", "difficulty": 0.5},
]
__all__ = ["llama_4_maverick_reasoning_examples"]
