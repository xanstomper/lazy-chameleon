"""claude_sonnet_5 - math examples."""
from __future__ import annotations
from typing import Any, Dict, List

claude_sonnet_5_math_examples: List[Dict[str, Any]] = [
    {"instruction": "gcd(123, 456) by Euclid", "response": "gcd = 3.", "difficulty": 0.6},
    {"instruction": "Eigenvalues of [[2,1],[1,2]]", "response": "lambda = 1, 3", "difficulty": 0.5},
    {"instruction": "Sum 7 with 2 dice probability", "response": "6/36 = 1/6", "difficulty": 0.5},
]
__all__ = ["claude_sonnet_5_math_examples"]
