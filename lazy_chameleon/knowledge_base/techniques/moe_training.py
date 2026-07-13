"""MoE training techniques reference."""
from __future__ import annotations
from typing import Any, Callable, Dict, List, Optional
import numpy as np

MOE_TRAINING_TECHNIQUES = {
    "load_balancing": {
        "auxiliary_loss": "Add load balancing loss to router",
        "z_loss": "Penalize extreme router logit values",
        "bias_adjustment": "Adjust bias terms instead of aux loss",
        "token_choice": "Let tokens choose experts",
        "expert_choice": "Let experts choose tokens",
    },
    "expert_architecture": {
        "fine_grained": "Many small experts (256 x 1/256)",
        "shared_isolation": "Isolate shared experts",
        "heterogeneous": "Varying expert sizes",
        "dynamic": "Create/destroy experts during training",
        "recursive": "Experts spawn sub-experts",
    },
}

class KnowledgeDistillationPipeline:
    def __init__(self, temperature: float = 2.0, alpha: float = 0.5):
        self.temp = temperature
        self.alpha = alpha

    def logit_distill(self, s: np.ndarray, t: np.ndarray) -> float:
        s = np.exp(s/self.temp) / np.sum(np.exp(s/self.temp), axis=-1, keepdims=True)
        t = np.exp(t/self.temp) / np.sum(np.exp(t/self.temp), axis=-1, keepdims=True)
        return float(np.mean(np.sum(t * np.log(t/(s+1e-10)), axis=-1)))

    def hidden_distill(self, s: np.ndarray, t: np.ndarray) -> float:
        return float(np.mean((s-t)**2))

    def attn_transfer(self, s: np.ndarray, t: np.ndarray) -> float:
        s = s / (s.sum(axis=-1, keepdims=True)+1e-10)
        t = t / (t.sum(axis=-1, keepdims=True)+1e-10)
        return float(np.mean((s-t)**2))

    def multi_teacher(self, s: np.ndarray, teachers: List[np.ndarray], weights: Optional[List[float]] = None) -> float:
        if weights is None: weights = [1.0/len(teachers)]*len(teachers)
        return sum(w * self.logit_distill(s, t) for w, t in zip(weights, teachers))

    def self_distill(self, logits: np.ndarray, past: np.ndarray) -> float:
        return self.logit_distill(logits, past)
