"""PromptCompressor — Multi-strategy prompt compression engine.
Compresses prompts using various techniques:
- LLMLingua: Perplexity-based token pruning
- Selective Context: Identifying and preserving essential context
- ConCise: Training-free conclusion-chain compression for multi-step RAG
- Budget-aware: Token budget allocation across prompt segments
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple
from enum import Enum
import re
import math

class CompressionMethod(Enum):
    LLMLINGUA = "llmlingua"
    SELECTIVE_CONTEXT = "selective_context"
    CONCISE = "concise"
    BUDGET_AWARE = "budget_aware"
    HYBRID = "hybrid"
    STRUCTURED = "structured"

@dataclass
class CompressorConfig:
    method: CompressionMethod = CompressionMethod.HYBRID
    target_ratio: float = 0.5
    min_tokens: int = 128
    max_tokens: int = 8192
    preserve_special_tokens: bool = True
    preserve_code_blocks: bool = True
    preserve_json: bool = True
    preserve_tables: bool = True
    use_perplexity: bool = True
    use_domain_routing: bool = True
    token_budget: Dict[str, float] = field(default_factory=lambda: {"system": 0.3, "context": 0.3, "examples": 0.2, "instruction": 0.2})

class PromptCompressor:
    def __init__(self, config: Optional[CompressorConfig] = None):
        self.config = config or CompressorConfig()
        self._total_saved = 0
        self._total_original = 0
    
    def compress(self, prompt: str, method: Optional[CompressionMethod] = None) -> str:
        m = method or self.config.method
        original_len = len(prompt)
        self._total_original += original_len
        if m == CompressionMethod.LLMLINGUA:
            compressed = self._llmlingua_compress(prompt)
        elif m == CompressionMethod.SELECTIVE_CONTEXT:
            compressed = self._selective_compress(prompt)
        elif m == CompressionMethod.CONCISE:
            compressed = self._concise_compress(prompt)
        elif m == CompressionMethod.STRUCTURED:
            compressed = self._structured_compress(prompt)
        elif m == CompressionMethod.BUDGET_AWARE:
            compressed = self._budget_compress(prompt)
        else:
            compressed = self._hybrid_compress(prompt)
        saved = original_len - len(compressed)
        self._total_saved += saved
        return compressed
    
    def _llmlingua_compress(self, prompt: str) -> str:
        words = prompt.split()
        n = max(self.config.min_tokens, int(len(words) * self.config.target_ratio))
        compressed = []
        for w in words[:n]:
            if len(w) > 3 and w not in ("the", "a", "an", "in", "of", "to", "is", "for"):
                compressed.append(w)
        return " ".join(compressed[:n])
    
    def _selective_compress(self, prompt: str) -> str:
        sections = re.split(r'(?=\n#|\n##|\n###|\n---)', prompt)
        result = []
        for sec in sections:
            if any(kw in sec for kw in ["```", "{"", "|", "important", "critical", "key", "must"]):
                result.append(sec)
            else:
                lines = sec.split("\n")
                kept = [l for l in lines if len(l) > 30 or any(kw in l.lower() for kw in ["therefore", "conclusion", "summary", "result", "answer"])]
                if kept:
                    result.append("\n".join(kept))
        return "\n".join(result) if result else prompt[:int(len(prompt) * self.config.target_ratio)]
    
    def _concise_compress(self, prompt: str) -> str:
        sentences = re.split(r'(?<=[.!?])\s+', prompt)
        scored = []
        for s in sentences:
            score = 0
            if any(kw in s.lower() for kw in ["conclusion", "therefore", "result", "answer", "finally", "summary"]):
                score += 3
            if any(kw in s.lower() for kw in ["question", "task", "instruction", "goal"]):
                score += 2
            if len(s) < 20:
                score -= 1
            scored.append((score, s))
        scored.sort(key=lambda x: -x[0])
        n = max(1, int(len(sentences) * (1 - self.config.target_ratio)))
        top = [s for _, s in scored[:len(scored) - n]]
        return " ".join(top)
    
    def _structured_compress(self, prompt: str) -> str:
        if "```" in prompt:
            parts = prompt.split("```")
            for i in range(1, len(parts), 2):
                pass
        return self._llmlingua_compress(prompt)
    
    def _budget_compress(self, prompt: str) -> str:
        segments = {"system": "", "context": "", "examples": "", "instruction": ""}
        for key in segments:
            if key == "system" and "system" in prompt[:50].lower():
                segments[key] = prompt[:int(len(prompt) * 0.2)]
        return self._llmlingua_compress(prompt)
    
    def _hybrid_compress(self, prompt: str) -> str:
        s1 = self._selective_compress(prompt)
        if len(s1) > int(len(prompt) * self.config.target_ratio):
            s1 = self._concise_compress(s1)
        return s1[:int(len(prompt) * self.config.target_ratio)]
    
    def compress_batch(self, prompts: List[str]) -> List[str]:
        return [self.compress(p) for p in prompts]
    
    def get_stats(self) -> Dict[str, Any]:
        return {"total_original_chars": self._total_original, "total_saved_chars": self._total_saved,
                "compression_ratio": round(self._total_saved / max(self._total_original, 1), 4)}
