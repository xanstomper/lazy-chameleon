"""qwen_3_7_max - reasoning examples."""
from __future__ import annotations
from typing import Any, Dict, List

qwen_3_7_max_reasoning_examples: List[Dict[str, Any]] = [
    {"instruction": "Clock hands overlap in 24h?", "response": "22 times.", "difficulty": 0.3},
    {"instruction": "3 and 5 gal jug, measure 4", "response": "Fill 5, pour to 3. Empty 3, pour 2. Fill 5, pour to 3. 4 left.", "difficulty": 0.7},
    {"instruction": "Bat $1 more, total $1.10, ball cost?", "response": "$0.05. x+(x+1)=1.10.", "difficulty": 0.4},
    {"instruction": "Next: 2,6,18,54,?", "response": "162. Multiply by 3.", "difficulty": 0.5},
    {"instruction": "How many months have 28 days?", "response": "All 12.", "difficulty": 0.8},
]
__all__ = ["qwen_3_7_max_reasoning_examples"]
