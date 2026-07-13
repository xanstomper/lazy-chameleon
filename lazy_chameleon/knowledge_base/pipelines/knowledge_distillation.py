"""Knowledge distillation pipelines for MoE models."""
from __future__ import annotations
from typing import Any, Callable, Dict, List, Optional
import numpy as np

class KnowledgeDistillationPipeline:
    def __init__(self, temperature: float = 2.0):
        self.temp = temperature

    def logit_distill(self, s: np.ndarray, t: np.ndarray) -> float:
        s = np.exp(s/self.temp) / np.sum(np.exp(s/self.temp), axis=-1, keepdims=True)
        t = np.exp(t/self.temp) / np.sum(np.exp(t/self.temp), axis=-1, keepdims=True)
        return float(np.mean(np.sum(t * np.log(t/(s+1e-10)), axis=-1)))

    def hidden_distill(self, s: np.ndarray, t: np.ndarray) -> float:
        return float(np.mean((s-t)**2))

    def multi_teacher(self, s: np.ndarray, teachers: List[np.ndarray], weights: Optional[List[float]] = None) -> float:
        if weights is None: weights = [1.0/len(teachers)]*len(teachers)
        return sum(w * self.logit_distill(s, t) for w, t in zip(weights, teachers))

    def progressive(self, student_fn: Callable, teacher_fn: Callable, curriculum: List[float]) -> List[float]:
        losses = []
        for diff in curriculum:
            s_out = student_fn(diff)
            t_out = teacher_fn(diff)
            losses.append(self.logit_distill(s_out, t_out))
        return losses
