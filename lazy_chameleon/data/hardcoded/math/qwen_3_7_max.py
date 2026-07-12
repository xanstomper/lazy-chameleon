"""qwen_3_7_max - math examples."""
from __future__ import annotations
from typing import Any, Dict, List

qwen_3_7_max_math_examples: List[Dict[str, Any]] = [
    {"instruction": "Derivative of x^3 sin(x)", "response": "3x^2 sin(x) + x^3 cos(x).", "difficulty": 0.3},
    {"instruction": "Integral of x^2 e^x dx", "response": "(x^2 - 2x + 2)e^x + C.", "difficulty": 0.3},
    {"instruction": "Prove sum 1..n = n(n+1)/2", "response": "Induction: base n=1, add k+1.", "difficulty": 0.8},
    {"instruction": "Solve dy/dx = 2x + 3y", "response": "Integrating factor e^{-3x}. y = Ce^{3x} - 2x/3 - 2/9.", "difficulty": 0.6},
]
__all__ = ["qwen_3_7_max_math_examples"]
