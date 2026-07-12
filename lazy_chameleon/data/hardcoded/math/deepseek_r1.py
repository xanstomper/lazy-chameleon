"""deepseek_r1 - math examples."""
from __future__ import annotations
from typing import Any, Dict, List

deepseek_r1_math_examples: List[Dict[str, Any]] = [
    {"instruction": "C(10,3) value", "response": "120", "difficulty": 0.4},
    {"instruction": "gcd(123, 456) by Euclid", "response": "gcd = 3.", "difficulty": 0.8},
    {"instruction": "Integral of x^2 e^x dx", "response": "(x^2 - 2x + 2)e^x + C.", "difficulty": 0.7},
    {"instruction": "Sum 7 with 2 dice probability", "response": "6/36 = 1/6", "difficulty": 0.3},
    {"instruction": "Eigenvalues of [[2,1],[1,2]]", "response": "lambda = 1, 3", "difficulty": 0.5},
]
__all__ = ["deepseek_r1_math_examples"]
