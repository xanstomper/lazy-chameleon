"""gpt_5_5 - reasoning examples."""
from __future__ import annotations
from typing import Any, Dict, List

gpt_5_5_reasoning_examples: List[Dict[str, Any]] = [
    {"instruction": "12 coins, one heavier, 3 weighings", "response": "4v4, then 1v1 approach.", "difficulty": 0.5},
    {"instruction": "3 and 5 gal jug, measure 4", "response": "Fill 5, pour to 3. Empty 3, pour 2. Fill 5, pour to 3. 4 left.", "difficulty": 0.6},
    {"instruction": "Next: 2,6,18,54,?", "response": "162. Multiply by 3.", "difficulty": 0.4},
]
__all__ = ["gpt_5_5_reasoning_examples"]
