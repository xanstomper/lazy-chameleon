"""Meta Llama, Google Gemini, Meituan LongCat models."""
from __future__ import annotations
from typing import Any, Dict

META = {
    "name": "Meta AI",
    "models": {
        "llama_4_maverick": {"architecture": "Dense + MoE augmentation", "context_window": 131072},
    },
}

GOOGLE = {
    "name": "Google DeepMind",
    "models": {
        "gemini_3_1_pro": {"architecture": "Multi-modal MoE", "context_window": 1000000},
    },
}

LONGCAT = {
    "name": "Meituan LongCat",
    "models": {
        "longcat_2": {"architecture": "MoE Transformer", "context_window": 1000000, "total_params": "1.6T"},
    },
}
