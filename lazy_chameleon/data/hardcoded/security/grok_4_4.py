"""grok_4_4 - security examples."""
from __future__ import annotations
from typing import Any, Dict, List

grok_4_4_security_examples: List[Dict[str, Any]] = [
    {"instruction": "Prevent XSS attacks", "response": "CSP, escape HTML, HttpOnly, sanitize input.", "difficulty": 0.2},
    {"instruction": "Zero-trust architecture", "response": "Never trust, always verify. Micro-seg.", "difficulty": 0.4},
    {"instruction": "SQL injection prevention", "response": "Parameterized queries always.", "difficulty": 0.3},
    {"instruction": "OAuth 2.0 flow", "response": "Authorization code flow with redirect.", "difficulty": 0.9},
]
__all__ = ["grok_4_4_security_examples"]
