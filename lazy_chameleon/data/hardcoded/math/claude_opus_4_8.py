"""claude_opus_4_8 - math examples."""
from __future__ import annotations
from typing import Any, Dict, List

claude_opus_4_8_math_examples: List[Dict[str, Any]] = [
    {"instruction": "Solve dy/dx = 2x + 3y", "response": "Integrating factor e^{-3x}. y = Ce^{3x} - 2x/3 - 2/9.", "difficulty": 0.4},
    {"instruction": "Find lim x->0 (sin x)/x", "response": "Limit = 1 via squeeze theorem.", "difficulty": 0.6},
    {"instruction": "Integral of x^2 e^x dx", "response": "(x^2 - 2x + 2)e^x + C.", "difficulty": 0.6},
]
__all__ = ["claude_opus_4_8_math_examples"]
