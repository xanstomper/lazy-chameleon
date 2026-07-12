"""claude_sonnet_5 - reasoning examples."""
from __future__ import annotations
from typing import Any, Dict, List

claude_sonnet_5_reasoning_examples: List[Dict[str, Any]] = [
    {"instruction": "3 and 5 gal jug, measure 4", "response": "Fill 5, pour to 3. Empty 3, pour 2. Fill 5, pour to 3. 4 left.", "difficulty": 0.7},
    {"instruction": "6 people paint house in 8h. How long for 4?", "response": "12 hours. Inverse: 6*8/4.", "difficulty": 0.8},
    {"instruction": "Bat $1 more, total $1.10, ball cost?", "response": "$0.05. x+(x+1)=1.10.", "difficulty": 0.3},
]
__all__ = ["claude_sonnet_5_reasoning_examples"]
