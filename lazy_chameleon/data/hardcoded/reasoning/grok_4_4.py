"""grok_4_4 - reasoning examples."""
from __future__ import annotations
from typing import Any, Dict, List

grok_4_4_reasoning_examples: List[Dict[str, Any]] = [
    {"instruction": "3 and 5 gal jug, measure 4", "response": "Fill 5, pour to 3. Empty 3, pour 2. Fill 5, pour to 3. 4 left.", "difficulty": 0.7},
    {"instruction": "3 pills every 30 min, how long?", "response": "1 hour. 0, 30, 60.", "difficulty": 0.3},
    {"instruction": "Clock hands overlap in 24h?", "response": "22 times.", "difficulty": 0.3},
    {"instruction": "12 coins, one heavier, 3 weighings", "response": "4v4, then 1v1 approach.", "difficulty": 0.9},
]
__all__ = ["grok_4_4_reasoning_examples"]
