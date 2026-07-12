"""gpt_5_5 - security examples."""
from __future__ import annotations
from typing import Any, Dict, List

gpt_5_5_security_examples: List[Dict[str, Any]] = [
    {"instruction": "OAuth 2.0 flow", "response": "Authorization code flow with redirect.", "difficulty": 0.5},
    {"instruction": "CSRF attack prevention", "response": "Anti-CSRF tokens, SameSite cookies.", "difficulty": 0.2},
    {"instruction": "Prevent XSS attacks", "response": "CSP, escape HTML, HttpOnly, sanitize input.", "difficulty": 0.5},
    {"instruction": "Zero-trust architecture", "response": "Never trust, always verify. Micro-seg.", "difficulty": 0.9},
    {"instruction": "SQL injection prevention", "response": "Parameterized queries always.", "difficulty": 0.9},
]
__all__ = ["gpt_5_5_security_examples"]
