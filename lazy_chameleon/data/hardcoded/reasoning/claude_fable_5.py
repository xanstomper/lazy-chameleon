"""claude_fable_5 - reasoning examples."""
from __future__ import annotations
from typing import Any, Dict, List

claude_fable_5_reasoning_examples: List[Dict[str, Any]] = [
    {"instruction": "Bat $1 more, total $1.10, ball cost?", "response": "$0.05. x+(x+1)=1.10.", "difficulty": 0.2},
    {"instruction": "6 people paint house in 8h. How long for 4?", "response": "12 hours. Inverse: 6*8/4.", "difficulty": 0.6},
    {"instruction": "12 coins, one heavier, 3 weighings", "response": "4v4, then 1v1 approach.", "difficulty": 0.6},
]
__all__ = ["claude_fable_5_reasoning_examples"]
