"""Zhipu AI GLM models - 5.1, 5.2, bidirectional prefix LM."""
from __future__ import annotations
from typing import Any, Dict
import numpy as np

GLM = {
    "name": "Zhipu AI GLM",
    "models": {
        "glm_5_1": {"architecture": "Bidirectional Prefix LM", "context_window": 131072},
        "glm_5_2": {"architecture": "Bidirectional Prefix LM + MoE", "context_window": 262144},
    },
}

class GLMBidirectionalPrefix:
    def __init__(self, prefix_len: int = 512, hidden_dim: int = 7168):
        self.prefix_len = prefix_len
        self.hidden_dim = hidden_dim
    def create_mask(self, seq_len: int) -> np.ndarray:
        mask = np.zeros((seq_len, seq_len))
        mask[:self.prefix_len, :] = 1.0
        for i in range(self.prefix_len, seq_len):
            mask[i, :i+1] = 1.0
        return mask
    def forward(self, q: np.ndarray, k: np.ndarray, v: np.ndarray, mask: np.ndarray) -> np.ndarray:
        scores = (q @ k.T) / np.sqrt(self.hidden_dim)
        scores = scores * mask + (1 - mask) * -1e10
        w = np.exp(scores - scores.max(axis=-1, keepdims=True))
        return (w / w.sum(axis=-1, keepdims=True)) @ v
