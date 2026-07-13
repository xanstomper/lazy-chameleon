"""Knowledge Base — How frontier AI models actually function."""
from __future__ import annotations
from typing import Any, Dict, List, Optional

from .providers.deepseek import DEEPSEEK_TECHNICAL
from .providers.openai import OPENAI
from .providers.anthropic import ANTHROPIC, ConstitutionalAI
from .providers.xai import XAI, GrokRealTimeKnowledge
from .providers.qwen import QWEN, QwenMultilingualGraph
from .providers.glm import GLM, GLMBidirectionalPrefix
from .providers.meta_google import META, GOOGLE, LONGCAT
from .techniques.moe_manipulator import MoEManipulator
from .techniques.moe_training import MOE_TRAINING_TECHNIQUES
from .techniques.prompts import PROMPT_PATTERNS
from .techniques.datasets import FRONTIER_DATASETS, get_all_datasets
from .techniques.knowledge_graphs import KNOWLEDGE_GRAPHS
from .techniques.inference import INFERENCE_OPTIMIZATIONS
from .pipelines.deepseek_r1 import GRPO, DeepSeekR1Pipeline
from .pipelines.constitutional_ai import ConstitutionalAIPipeline, CONSTITUTION
from .pipelines.knowledge_distillation import KnowledgeDistillationPipeline

KNOWLEDGE_BASE = {
    "providers": [OPENAI, ANTHROPIC, XAI, QWEN, GLM, META, DEEPSEEK_TECHNICAL, GOOGLE, LONGCAT],
    "all_models": {},
    "common_datasets": ["Common Crawl", "Wikipedia", "Books", "GitHub Code", "arXiv"],
    "common_architectures": ["Dense Transformer", "MoE Transformer", "Prefix LM"],
    "common_training_methods": ["Next-token prediction", "SFT", "RLHF", "DPO", "Constitutional AI"],
    "alignment_methods": ["RLHF", "DPO", "Constitutional AI", "RLAIF"],
}
for p in KNOWLEDGE_BASE["providers"]:
    if isinstance(p, dict) and "models" in p:
        for m, i in p["models"].items():
            i["provider"] = p.get("name", "unknown")
            KNOWLEDGE_BASE["all_models"][m] = i

def get_model_info(name: str) -> Optional[Dict]:
    return KNOWLEDGE_BASE["all_models"].get(name)

def get_provider_info(name: str) -> Optional[Dict]:
    m = {p.get("name","").lower(): p for p in [OPENAI,ANTHROPIC,XAI,QWEN,GLM,META,GOOGLE,LONGCAT] if isinstance(p,dict)}
    return m.get(name.lower())

def get_all_prompt_patterns() -> Dict:
    return PROMPT_PATTERNS

def compare_models(names: List[str]) -> Dict:
    c = {}
    for n in names:
        i = get_model_info(n)
        if i: c[n] = {k: str(i.get(k,"N/A"))[:80] for k in ["architecture","context_window","key_innovation","inference_cost"]}
    return c

def get_moe_techniques() -> Dict[str, str]:
    return {"1. Dynamic Allocation": "Allocate based on input complexity",
            "2. Fine-Grained Split": "Split overloaded experts into sub-experts",
            "3. Aux-Free Balance": "Use bias terms instead of auxiliary loss",
            "4. Shared Isolation": "Dedicate experts to universal knowledge",
            "5. Speculative Routing": "Predict experts before computation",
            "6. Expert Merging": "Merge redundant experts",
            "7. GRPO Training": "Train experts with Group Relative Policy Optimization",
            "8. Progressive Sparsify": "Gradually increase sparsity during training",
            "9. Heterogeneous Sizes": "Different sized experts for different tasks",
            "10. Recursive Refine": "Experts spawn sub-experts for complex tasks"}

__all__ = [
    "OPENAI", "ANTHROPIC", "XAI", "QWEN", "GLM", "META", "GOOGLE", "LONGCAT",
    "DEEPSEEK_TECHNICAL", "KNOWLEDGE_BASE", "FRONTIER_DATASETS",
    "PROMPT_PATTERNS", "KNOWLEDGE_GRAPHS", "INFERENCE_OPTIMIZATIONS",
    "MOE_TRAINING_TECHNIQUES",
    "MoEManipulator", "ConstitutionalAI", "GrokRealTimeKnowledge",
    "QwenMultilingualGraph", "GLMBidirectionalPrefix",
    "GRPO", "DeepSeekR1Pipeline", "ConstitutionalAIPipeline",
    "KnowledgeDistillationPipeline",
    "get_model_info", "get_provider_info", "get_all_prompt_patterns",
    "compare_models", "get_all_datasets", "get_moe_techniques",
]
