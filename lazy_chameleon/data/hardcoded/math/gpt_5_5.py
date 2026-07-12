"""gpt_5_5 - math examples."""
from __future__ import annotations
from typing import Any, Dict, List

gpt_5_5_math_examples: List[Dict[str, Any]] = [
    {"instruction": "Find lim x->0 (sin x)/x", "response": "Limit = 1 via squeeze theorem.", "difficulty": 0.3},
    {"instruction": "Solve dy/dx = 2x + 3y", "response": "Integrating factor e^{-3x}. y = Ce^{3x} - 2x/3 - 2/9.", "difficulty": 0.3},
    {"instruction": "Eigenvalues of [[2,1],[1,2]]", "response": "lambda = 1, 3", "difficulty": 0.7},
    {"instruction": "Prove sqrt(3) irrational", "response": "Assume reduced a/b, contradiction.", "difficulty": 0.6},
    {"instruction": "gcd(123, 456) by Euclid", "response": "gcd = 3.", "difficulty": 0.6},
]
__all__ = ["gpt_5_5_math_examples"]
