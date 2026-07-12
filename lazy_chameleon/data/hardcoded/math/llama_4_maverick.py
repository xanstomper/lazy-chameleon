"""llama_4_maverick - math examples."""
from __future__ import annotations
from typing import Any, Dict, List

llama_4_maverick_math_examples: List[Dict[str, Any]] = [
    {"instruction": "Prove sqrt(3) irrational", "response": "Assume reduced a/b, contradiction.", "difficulty": 0.2},
    {"instruction": "Prove sum 1..n = n(n+1)/2", "response": "Induction: base n=1, add k+1.", "difficulty": 0.4},
    {"instruction": "Integral of x^2 e^x dx", "response": "(x^2 - 2x + 2)e^x + C.", "difficulty": 0.4},
    {"instruction": "C(10,3) value", "response": "120", "difficulty": 0.3},
    {"instruction": "Solve dy/dx = 2x + 3y", "response": "Integrating factor e^{-3x}. y = Ce^{3x} - 2x/3 - 2/9.", "difficulty": 0.4},
]
__all__ = ["llama_4_maverick_math_examples"]
