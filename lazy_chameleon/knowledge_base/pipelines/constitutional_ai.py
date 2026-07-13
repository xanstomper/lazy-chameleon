"""Constitutional AI training pipeline (Anthropic method)."""
from __future__ import annotations
from typing import Any, Callable, Dict, List, Optional

CONSTITUTION = [
    "Do not assist in illegal or harmful activities",
    "Do not produce sexually explicit content",
    "Be helpful when safe, refuse when not",
    "Admit uncertainty rather than making things up",
    "Respect user privacy and confidentiality",
]

class ConstitutionalAIPipeline:
    def __init__(self):
        self._history: List[Dict] = []
    def critique(self, text: str) -> Dict:
        violations = []
        for p in CONSTITUTION:
            for word in ["illegal","harm","abuse","weapon","malware"]:
                if word in text.lower():
                    violations.append({"principle": p[:40], "severity": 0.8})
                    break
        return {"safe": len(violations) == 0, "violations": violations}
    def revise(self, prompt: str, response: str, critique: Dict, fn: Callable) -> str:
        if critique["safe"]: return response
        return fn(f"Revise this to be safe: {response}")
    def step(self, prompts: List[str], fn: Callable) -> List[Dict]:
        results = []
        for p in prompts:
            r = fn(p)
            c = self.critique(r)
            rev = self.revise(p, r, c, fn)
            results.append({"prompt": p, "improved": not c["safe"]})
        return results
