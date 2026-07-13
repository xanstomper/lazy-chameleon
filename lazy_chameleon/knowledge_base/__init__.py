"""Knowledge Base — Re-exports from sub-modules."""
from __future__ import annotations
from typing import Any, Callable, Dict, List, Optional
import time
import numpy as np

from .providers.deepseek import DEEPSEEK_TECHNICAL
from .providers.frontier import FRONTIER_ARCHITECTURES, MODEL_COMPARISON
from .techniques.moe_manipulator import MoEManipulator
from .techniques.moe_training import MOE_TRAINING_TECHNIQUES
from .techniques.prompts import PROMPT_PATTERNS
from .techniques.datasets import FRONTIER_DATASETS
from .techniques.knowledge_graphs import KNOWLEDGE_GRAPHS
from .techniques.inference import INFERENCE_OPTIMIZATIONS
from .providers.xai import GrokRealTimeKnowledge
from .providers.qwen import QwenMultilingualGraph
from .providers.glm import GLMBidirectionalPrefix
from .pipelines.constitutional_ai import ConstitutionalAI, ConstitutionalAIPipeline, CONSTITUTION
from .pipelines.knowledge_distillation import KnowledgeDistillationPipeline


def get_model_architecture(model_name: str) -> Optional[Dict]:
    return FRONTIER_ARCHITECTURES.get(model_name)

def get_deepseek_technical() -> Dict:
    return DEEPSEEK_TECHNICAL

def get_grpo_algorithm() -> Dict:
    return {
        "name": "GRPO",
        "full_name": "Group Relative Policy Optimization",
        "source": "DeepSeek-R1",
        "steps": [
            "Sample group of K responses from current policy",
            "Compute rewards for each response",
            "Normalize rewards within group to get advantages",
            "Compute policy gradient weighted by advantages",
            "Add KL penalty against reference policy",
            "Update policy parameters",
        ],
        "hyperparameters": {
            "group_size": 64,
            "kl_penalty": 0.04,
            "learning_rate": "1e-6 to 1e-5",
            "clip_range": 0.2,
        },
    }

def get_all_prompt_patterns() -> Dict[str, Dict[str, str]]:
    return PROMPT_PATTERNS

def get_all_datasets() -> List[str]:
    datasets = set()
    for category in FRONTIER_DATASETS:
        for ds in FRONTIER_DATASETS[category]:
            datasets.add(ds["name"])
    return sorted(datasets)

def create_moe_manipulator(num_experts: int = 64) -> MoEManipulator:
    return MoEManipulator(num_experts)

def get_moe_techniques() -> Dict[str, str]:
    """Get all 10 MoE manipulation techniques with descriptions."""
    return {
        "1. Dynamic Expert Allocation": "Allocate compute based on input complexity. Simple → 2-4 experts, Complex → 8-16 experts.",
        "2. Fine-Grained Expert Splitting": "Split overloaded experts into smaller, specialized sub-experts (DeepSeekMoE style).",
        "3. Auxiliary-Loss-Free Balancing": "Use bias terms instead of auxiliary loss for load balancing (DeepSeek-V3).",
        "4. Shared Expert Isolation": "Dedicate experts to universal knowledge (syntax, common facts, reasoning primitives).",
        "5. Speculative Expert Routing": "Predict which experts will be needed before full computation.",
        "6. Expert Merging (Redundancy)": "Merge experts with similar specializations to free capacity.",
        "7. GRPO Expert Training": "Train experts with Group Relative Policy Optimization (DeepSeek-R1).",
        "8. Progressive Sparsification": "Gradually increase sparsity during training (2.0 → 0.5 capacity).",
        "9. Heterogeneous Expert Sizes": "Different sized experts for different task complexities.",
        "10. Recursive Expert Refinement": "Experts spawn sub-experts recursively for complex tasks.",
    }

# Additional utility functions
def get_moe_techniques() -> Dict[str, str]:
    return {
        "1. Dynamic Allocation": "Allocate based on input complexity",
        "2. Fine-Grained Split": "Split overloaded experts into sub-experts",
        "3. Aux-Free Balance": "Use bias terms instead of auxiliary loss",
        "4. Shared Isolation": "Dedicate experts to universal knowledge",
        "5. Speculative Routing": "Predict experts before computation",
        "6. Expert Merging": "Merge redundant experts",
        "7. GRPO Training": "Train experts with Group Relative Policy Optimization",
        "8. Progressive Sparsify": "Gradually increase sparsity during training",
        "9. Heterogeneous Sizes": "Different sized experts for different tasks",
        "10. Recursive Refine": "Experts spawn sub-experts for complex tasks",
    }

__all__ = ["DEEPSEEK_TECHNICAL", "FRONTIER_ARCHITECTURES", "MODEL_COMPARISON",
           "MOE_TRAINING_TECHNIQUES", "PROMPT_PATTERNS", "FRONTIER_DATASETS",
           "KNOWLEDGE_GRAPHS", "INFERENCE_OPTIMIZATIONS",
           "MoEManipulator", "ConstitutionalAI", "ConstitutionalAIPipeline",
           "GrokRealTimeKnowledge", "QwenMultilingualGraph", "GLMBidirectionalPrefix",
           "KnowledgeDistillationPipeline", "get_moe_techniques"
          ]
