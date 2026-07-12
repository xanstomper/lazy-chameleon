"""deepseek_r1 - reasoning examples."""
from __future__ import annotations
from typing import Any, Dict, List

deepseek_r1_reasoning_examples: List[Dict[str, Any]] = [
    {"instruction": "3 and 5 gal jug, measure 4", "response": "Fill 5, pour to 3. Empty 3, pour 2. Fill 5, pour to 3. 4 left.", "difficulty": 0.2},
    {"instruction": "Next: 2,6,18,54,?", "response": "162. Multiply by 3.", "difficulty": 0.2},
    {"instruction": "How many months have 28 days?", "response": "All 12.", "difficulty": 0.2},
]
__all__ = ["deepseek_r1_reasoning_examples"]
