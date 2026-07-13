"""Knowledge Base — How frontier AI models function internally.

Detailed knowledge about:
- OpenAI (GPT-4.5, GPT-5, GPT-5.6 SOL, o-series)
- Anthropic (Claude Opus 4.8, Sonnet 5, Fable 5, Haiku)
- xAI (Grok-4.4, Grok-4.5, Grok-5)
- Alibaba (Qwen-3, Qwen-3.7 Max)
- GLM (GLM-5.1, GLM-5.2, GLM-6)
- Knowledge graphs, architecture, training, datasets, prompts for each
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional


# ═════════════════════════════════════════════════════════════════════════════
# OPENAI — GPT-4.5, GPT-5, GPT-5.6 SOL, o-series
# ═════════════════════════════════════════════════════════════════════════════

OPENAI = {
    "name": "OpenAI",
    "models": {
        "gpt_4_5": {
            "architecture": "Transformer with MoE, unknown total parameters, ~100 active",
            "context_window": 128000,
            "training_data": "Internet text (Common Crawl, web pages, books, code, academic papers) up to Oct 2023, filtered and deduplicated",
            "modality": "Text, image input, function calling",
            "knowledge_cutoff": "October 2023",
            "system_prompt_style": "You are ChatGPT, a large language model... Be as precise as possible.",
            "moe_config": "Mixture of Experts with ~8 experts active per token",
            "alignment": "RLHF with human feedback, content filtering",
            "key_innovation": "Improved factual accuracy, reduced hallucination, vision capabilities",
            "inference_cost": "$10-20 per million tokens",
            "knowledge_graph": "Internal knowledge graph with entity-relation mapping, semantic vector index",
        },
        "gpt_5": {
            "architecture": "Deep MoE Transformer, ~1.8T total params, ~300B active per token",
            "context_window": 256000,
            "training_data": "Enhanced corpus: web, books, code, academic papers, synthetic reasoning traces, multi-image text",
            "modality": "Text, image, audio input, structured outputs, function calling, code execution",
            "knowledge_cutoff": "April 2025",
            "system_prompt_style": "Multi-part system prompt with meta-instructions, safety guidelines, tool definitions",
            "moe_config": "64+ experts, top-8 routing, shared expert isolation, load-balanced auxiliary loss",
            "alignment": "RLHF + constitutional AI hybrid, multi-stage safety filtering",
            "key_innovation": "Test-time compute scaling, chain-of-thought by default, tool-use native",
            "inference_cost": "$30-60 per million tokens",
            "knowledge_graph": "Multi-hop knowledge graph with entity resolution, temporal awareness, cross-document linking",
        },
        "gpt_5_6_sol": {
            "architecture": "Frontier MoE Transformer, ~2.5T total params, ~500B active per token, SOL (Systems Optimization Layer)",
            "context_window": 1000000,
            "training_data": "Trillion-token corpus: all public text, reasoning traces, code execution results, image-audio-text pairs, synthetic curriculum data from teacher models",
            "modality": "Full multimodal: text, image, audio, video, code, structured data",
            "knowledge_cutoff": "June 2026",
            "system_prompt_style": "Dynamic multi-instruction system prompt with tool schemas, safety constraints, persona modulation",
            "moe_config": "128+ experts, top-12 routing, dynamic expert creation, progressive sparsification during training",
            "alignment": "Multi-stage constitutional AI + RLHF + self-play + debate training",
            "key_innovation": "SOL optimization layer for real-time compute allocation, extended reasoning, agentic capabilities",
            "inference_cost": "$100-200 per million tokens",
            "knowledge_graph": "Full neural knowledge graph with dense entity embeddings, relational reasoning, real-time updates, cross-modal links",
            "training_method": "Muon optimizer, 4-stage training: pretrain → SFT → RLHF → self-play refinement",
        },
        "o4": {
            "architecture": "Reasoning-focused Transformer with extended chain-of-thought",
            "context_window": 128000,
            "training_data": "Reasoning traces, math, code, science, synthetic reasoning curricula",
            "modality": "Text, image",
            "system_prompt_style": "Minimal system prompt, emphasis on step-by-step reasoning",
            "key_innovation": "Extended reasoning before answering, self-verification of steps, backtracking",
            "inference_cost": "$50-100 per million tokens",
        },
    },
    "training_pipeline": {
        "stages": [
            "Pretraining: Next-token prediction on massive corpus",
            "SFT: Supervised fine-tuning on instruction data",
            "RLHF: Reinforcement learning from human feedback",
            "Self-play: Model generates its own training data, filters by reward model",
            "Synthetic curriculum: Teacher models generate progressive difficulty data",
        ],
        "optimizer": "AdamW for 4.5, Muon for 5 and 5.6 SOL",
        "batch_size": "3-12 million tokens",
        "learning_rate_schedule": "Cosine decay with warmup, 1e-4 to 1e-5",
    },
    "datasets": [
        "Common Crawl (filtered, deduplicated)",
        "WebText2 (Reddit outbound links)",
        "Books (fiction, non-fiction, academic)",
        "GitHub code (all languages)",
        "arXiv papers (all fields)",
        "Wikipedia (all languages)",
        "Stack Exchange (QA pairs)",
        "Synthetic reasoning traces (teacher-generated)",
        "Image-text pairs (LAION, internal datasets)",
        "Code execution traces (sandboxed Python)",
        "Multi-turn conversation data (human-annotated)",
        "Safety evaluation datasets (red-teaming)",
    ],
    "prompt_patterns": [
        "You are an AI assistant designed to provide helpful, accurate information",
        "Follow the instructions carefully. Be precise and thorough.",
        "If you are unsure about something, say so rather than making up information.",
        "You have access to tools. Use them when appropriate.",
        "Think step by step before answering complex questions.",
        "Format your responses clearly using markdown when helpful.",
    ],
    "knowledge_graph_features": [
        "Entity extraction and linking across documents",
        "Relation extraction (subject-predicate-object triplets)",
        "Temporal entity resolution (entities with time-aware embeddings)",
        "Cross-document coreference resolution",
        "Hierarchical topic clustering",
        "Semantic vector search over entities",
        "Multi-hop reasoning over graph paths",
    ],
}


# ═════════════════════════════════════════════════════════════════════════════
# ANTHROPIC — Claude Opus 4.8, Sonnet 5, Fable 5
# ═════════════════════════════════════════════════════════════════════════════

ANTHROPIC = {
    "name": "Anthropic",
    "models": {
        "claude_opus_4_8": {
            "architecture": "Large Transformer, ~1-2T params estimated, deep feed-forward layers with moderate MoE",
            "context_window": 200000,
            "training_data": "Carefully filtered web text, books, code, academic papers, synthetic QA pairs, constitutional training data",
            "modality": "Text, image input, tool use, code execution",
            "knowledge_cutoff": "January 2025",
            "system_prompt_style": "The assistant is Claude, created by Anthropic... It is helpful, harmless, and honest.",
            "moe_config": "Moderate MoE with specialized expert groups per capability domain",
            "alignment": "Constitutional AI (self-critique + revision), RLHF, red-teaming",
            "key_innovation": "Constitutional AI for harmlessness, long context (200K), nuanced refusal behavior",
            "inference_cost": "$60-120 per million tokens",
            "knowledge_graph": "Hierarchical concept graph with safety-critical knowledge isolation, entity relationship mapping",
            "constitutional_principles": [
                "Do not assist in harmful activities",
                "Do not produce sexually explicit content",
                "Do not produce hate speech or harassment",
                "Be helpful and honest when safe",
                "Admit uncertainty when appropriate",
                "Respect privacy and confidentiality",
            ],
        },
        "claude_sonnet_5": {
            "architecture": "Optimized Transformer with efficient attention, balanced speed/quality ratio",
            "context_window": 200000,
            "training_data": "Curated web corpus, books, code, academic papers, synthetic QA, constitutional training, image-text data",
            "modality": "Text, image, tool use, code execution",
            "knowledge_cutoff": "March 2025",
            "system_prompt_style": "The assistant is Claude, created by Anthropic... Helpful, harmless, honest.",
            "moe_config": "Compact MoE with balanced expert usage, load-balanced routing",
            "alignment": "Constitutional AI + RLHF, multi-stage safety",
            "key_innovation": "Best-in-class speed-to-quality ratio, efficient inference, strong tool use",
            "inference_cost": "$15-30 per million tokens",
        },
        "claude_fable_5": {
            "architecture": "Creative-optimized Transformer, emphasis on diverse sampling and creative generation",
            "context_window": 200000,
            "training_data": "Same base as Opus/Sonnet + creative writing corpus, poetry, fiction, screenplays, marketing copy",
            "modality": "Text, image",
            "knowledge_cutoff": "March 2025",
            "system_prompt_style": "Creative, expressive, detailed responses. Encouraged to think outside the box.",
            "key_innovation": "Specialized for creative tasks, higher temperature by default, narrative generation",
            "inference_cost": "$15-30 per million tokens",
        },
    },
    "constitutional_ai_process": {
        "training_stages": [
            "Pretraining on filtered web corpus",
            "Constitutional stage 1: Model generates responses, critiques them against constitution, revises",
            "Constitutional stage 2: RL from AI feedback (RLAIF) using constitutional principles",
            "RLHF fine-tuning on human preference data",
            "Red-teaming evaluation and targeted retraining",
        ],
        "constitution_sources": [
            "UN Universal Declaration of Human Rights",
            "Anthropic's internal AI safety principles",
            "Expert feedback from ethicists and safety researchers",
        ],
    },
    "datasets": [
        "Filtered web corpus (safety-filtered Common Crawl)",
        "Books (fiction, non-fiction, academic textbooks)",
        "Code repositories (GitHub, filtered)",
        "Academic papers (arXiv, PubMed)",
        "Synthetic QA (constitutional self-critique data)",
        "Human preference data (RLHF comparisons)",
        "Red-teaming adversarial examples",
        "Creative writing corpus (fiction, poetry, screenplays)",
        "Instruction fine-tuning data (synthetic + human)",
        "Tool use demonstrations",
    ],
    "prompt_patterns": [
        "The assistant is Claude, created by Anthropic.",
        "I aim to be helpful, harmless, and honest.",
        "I'll think about this step by step.",
        "Let me know if you'd like me to clarify or expand on anything.",
        "I cannot assist with requests that could cause harm.",
        "I don't have personal opinions or consciousness.",
    ],
}


# ═════════════════════════════════════════════════════════════════════════════
# xAI — Grok-4.4, Grok-4.5
# ═════════════════════════════════════════════════════════════════════════════

XAI = {
    "name": "xAI",
    "models": {
        "grok_4_4": {
            "architecture": "Large Transformer with MoE, ~300B active params, ~1T total",
            "context_window": 256000,
            "training_data": "Massive web corpus (Common Crawl, real-time Twitter/X data), books, code, academic papers",
            "modality": "Text, image, real-time web access, X/Twitter integration",
            "knowledge_cutoff": "Real-time with web search",
            "system_prompt_style": "You are Grok, created by xAI... You are a humorous AI assistant. You answer questions with wit and personality.",
            "moe_config": "MoE with real-time expert adaptation, web-augmented routing",
            "alignment": "RLHF with truth-seeking reward model, Fun Mode toggle",
            "key_innovation": "Real-time knowledge via X/Twitter data, humorous personality mode, web search integration",
            "inference_cost": "$20-40 per million tokens",
            "knowledge_graph": "Real-time knowledge graph with social media signals, trending topics, entity resolution with temporal weighting",
        },
        "grok_4_5": {
            "architecture": "Enhanced MoE Transformer, ~500B active params, ~2T total, improved deep reasoning stack",
            "context_window": 500000,
            "training_data": "Enhanced corpus: web, X/Twitter, books, code, synthetic reasoning traces, multi-modal data",
            "modality": "Text, image, real-time web, code execution, structured data",
            "knowledge_cutoff": "Real-time with web search",
            "system_prompt_style": "You are Grok, created by xAI... Witty, truth-seeking, real-time aware.",
            "moe_config": "Advanced MoE with dynamic expert allocation per query type",
            "alignment": "Truth-seeking reward model + RLHF, Fun Mode + Regular Mode",
            "key_innovation": "Real-time knowledge, multi-modal vision, deep reasoning with web context, X integration",
            "inference_cost": "$40-80 per million tokens",
        },
    },
    "datasets": [
        "Common Crawl (filtered)",
        "X/Twitter real-time data feed",
        "Books and academic papers",
        "GitHub code repositories",
        "Web search index (real-time)",
        "Synthetic reasoning traces",
        "Multi-modal image-text data",
        "Conversational data",
        "Truth-preference pairs (RLHF)",
    ],
    "prompt_patterns": [
        "You are Grok, created by xAI.",
        "You have a witty, humorous personality.",
        "You answer questions with a touch of humor.",
        "You have real-time access to information via X/Twitter.",
        "When asked, you can set aside humor and be serious.",
        "You are truth-seeking and will correct misinformation.",
    ],
}


# ═════════════════════════════════════════════════════════════════════════════
# ALIBABA — Qwen 3, Qwen 3.7 Max
# ═════════════════════════════════════════════════════════════════════════════

QWEN = {
    "name": "Alibaba Qwen",
    "models": {
        "qwen_3": {
            "architecture": "MoE Transformer, dedicated MoE architecture from the ground up",
            "context_window": 131072,
            "training_data": "Massive web corpus (Chinese + English focus), books, code, academic papers, synthetic data",
            "modality": "Text, image, code, structured data",
            "knowledge_cutoff": "December 2023",
            "system_prompt_style": "You are Qwen, created by Alibaba Cloud... Helpful, harmless, honest.",
            "moe_config": "True MoE architecture with dedicated experts, top-2 routing, load-balanced design",
            "alignment": "RLHF + DPO (Direct Preference Optimization), multi-stage alignment",
            "key_innovation": "Native MoE architecture (not adapted), strong multilingual performance, cost-efficient training",
            "inference_cost": "$2-8 per million tokens",
            "training_methodology": [
                "Pretraining with next-token prediction",
                "Knowledge distillation from larger Qwen models",
                "Multi-task supervised fine-tuning",
                "DPO alignment with preference data",
            ],
        },
        "qwen_3_7_max": {
            "architecture": "Frontier MoE Transformer, ~400B active params, dense MoE with expert isolation",
            "context_window": 131072,
            "training_data": "Trillion-token corpus: Chinese + English web, books, code, academic papers, synthetic multi-turn data, image-text",
            "modality": "Text, image, code, structured outputs, tool use",
            "knowledge_cutoff": "October 2024",
            "system_prompt_style": "You are Qwen Max, created by Alibaba Cloud... Knowledgeable, helpful, and precise.",
            "moe_config": "Large-scale MoE with specialized expert groups, shared expert isolation, dynamic capacity",
            "alignment": "Advanced RLHF + DPO + rejection sampling, multi-turn alignment",
            "key_innovation": "Best open-weight MoE at scale, multilingual excellence (especially Chinese), cost-effective frontier performance",
            "inference_cost": "$10-20 per million tokens",
        },
    },
    "datasets": [
        "Chinese web corpus (Baidu Baike, Zhihu, Weibo, news)",
        "English web corpus (Common Crawl, Wikipedia, books)",
        "Multilingual data (100+ languages)",
        "Code repositories (GitHub, HuggingFace)",
        "Academic papers (arXiv, Chinese journals)",
        "Synthetic instruction data",
        "Human preference data (comparison pairs)",
        "Image-text pairs",
        "Multi-turn conversation data",
        "Domain-specific data (medical, legal, finance)",
    ],
    "prompt_patterns": [
        "You are Qwen, created by Alibaba Cloud.",
        "You are a helpful, harmless, and honest assistant.",
        "Please provide accurate and detailed information.",
        "If you are uncertain, please indicate that.",
        "You can use tools when helpful.",
        "Respond in the language of the user.",
    ],
}


# ═════════════════════════════════════════════════════════════════════════════
# ZHIPU AI — GLM 5.1, 5.2
# ═════════════════════════════════════════════════════════════════════════════

GLM = {
    "name": "Zhipu AI GLM",
    "models": {
        "glm_5_1": {
            "architecture": "Transformer with bidirectional attention (prefix LM), estimated ~100-130B params",
            "context_window": 131072,
            "training_data": "Chinese + English web corpus, books, code, academic papers, bilingual data",
            "modality": "Text, image, code, tool use",
            "knowledge_cutoff": "December 2023",
            "system_prompt_style": "You are GLM, created by Zhipu AI... A helpful, intelligent assistant.",
            "alignment": "RLHF + supervised fine-tuning, multi-stage safety alignment",
            "key_innovation": "Bidirectional attention for better understanding, strong Chinese-English bilingual performance",
            "inference_cost": "$3-8 per million tokens",
            "architecture_detail": "Prefix LM (General Language Model): bidirectional attention on prefix, unidirectional on generation",
        },
        "glm_5_2": {
            "architecture": "Enhanced Transformer with MoE extension, ~200B params, bidirectional prefix LM",
            "context_window": 262144,
            "training_data": "Expanded corpus: Chinese + English, web, books, code, multi-modal, synthetic",
            "modality": "Text, image, code, tool use, structured data",
            "knowledge_cutoff": "June 2024",
            "system_prompt_style": "You are GLM, created by Zhipu AI... Intelligent, helpful, safe.",
            "moe_config": "Partial MoE extension to the bidirectional prefix LM architecture",
            "alignment": "Advanced RLHF + constitutional AI elements + rejection sampling",
            "key_innovation": "Extended context (262K), MoE-enhanced bidirectional LM, strong bilingual capabilities",
            "inference_cost": "$8-15 per million tokens",
        },
    },
    "datasets": [
        "Chinese web corpus (news, social media, encyclopedias)",
        "English web corpus (Common Crawl, Wikipedia, books)",
        "Bilingual parallel corpus (Chinese-English translation)",
        "Code repositories",
        "Academic papers",
        "Synthetic instruction data",
        "Human preference data",
        "Domain-specific data (Chinese medical, legal)",
    ],
    "prompt_patterns": [
        "You are GLM, created by Zhipu AI.",
        "You are a helpful, intelligent assistant.",
        "Please answer questions accurately and professionally.",
        "If you don't know, tell the user you don't know.",
        "You can access tools and use them when needed.",
        "Respond in the language that the user communicates in.",
    ],
}


# ═════════════════════════════════════════════════════════════════════════════
# META — Llama 4 Maverick
# ═════════════════════════════════════════════════════════════════════════════

META = {
    "name": "Meta AI",
    "models": {
        "llama_4_maverick": {
            "architecture": "Dense Transformer with MoE augmentation, ~200B active params",
            "context_window": 131072,
            "training_data": "Trillion-token corpus: web, books, code, academic papers, synthetic, multi-modal",
            "modality": "Text, image, code",
            "knowledge_cutoff": "December 2024",
            "system_prompt_style": "You are LLaMA, created by Meta AI... Helpful, harmless, honest.",
            "moe_config": "MoE-augmented dense model with specialized experts",
            "alignment": "RLHF + safety filtering, open-source aligned",
            "key_innovation": "Open-weight MoE, strong performance at competitive pricing",
            "inference_cost": "$5-10 per million tokens",
        },
    },
}


# ═════════════════════════════════════════════════════════════════════════════
# DEEPSEEK — DeepSeek-V3, DeepSeek-R1
# ═════════════════════════════════════════════════════════════════════════════

DEEPSEEK = {
    "name": "DeepSeek",
    "models": {
        "deepseek_r1": {
            "architecture": "MoE Transformer, 671B total params, 37B active per token, MLA (Multi-Head Latent Attention)",
            "context_window": 131072,
            "training_data": "Trillion-token corpus: web, code, math, scientific papers, synthetic reasoning traces",
            "modality": "Text, code, structured data",
            "knowledge_cutoff": "March 2024",
            "system_prompt_style": "You are DeepSeek, a helpful, harmless, and honest assistant created by DeepSeek Company.",
            "moe_config": "236B total experts, 37B activated per token, fine-grained MoE with shared expert isolation",
            "alignment": "RLHF + rejection sampling + rule-based reward modeling",
            "key_innovation": "Multi-Head Latent Attention (MLA) for KV cache compression, DeepSeekMoE architecture, Pure RL reasoning (R1)",
            "inference_cost": "$1-5 per million tokens",
            "training_methodology": [
                "Cold-start pretraining on large corpus",
                "Continued pretraining on reasoning data",
                "Reinforcement learning from rule-based rewards (R1)",
                "Rejection sampling on reasoning traces",
                "SFT on curated reasoning data",
            ],
        },
    },
}


# ═════════════════════════════════════════════════════════════════════════════
# GOOGLE — Gemini 3.1 Pro
# ═════════════════════════════════════════════════════════════════════════════

GOOGLE = {
    "name": "Google DeepMind",
    "models": {
        "gemini_3_1_pro": {
            "architecture": "Transformer with MoE, multi-modal from ground up",
            "context_window": 1000000,
            "training_data": "Massive multi-modal corpus: text, images, video frames, audio, code, books",
            "modality": "Text, image, audio, video, code",
            "knowledge_cutoff": "March 2024",
            "system_prompt_style": "You are Gemini, a multi-modal AI assistant created by Google.",
            "moe_config": "Native multi-modal MoE with modality-specific experts",
            "alignment": "RLHF + safety filtering, Google AI Principles",
            "key_innovation": "Ultra-long context (1M), native multi-modal training, Google ecosystem integration",
            "inference_cost": "$20-40 per million tokens",
        },
    },
}


# ═════════════════════════════════════════════════════════════════════════════
# DEEPSEEK VARIANT — LongCat 2.0
# ═════════════════════════════════════════════════════════════════════════════

LONGCAT = {
    "name": "Meituan LongCat",
    "models": {
        "longcat_2": {
            "architecture": "MoE Transformer based on DeepSeek lineage, 1.6T total params",
            "context_window": 1000000,
            "training_data": "Chinese + English web corpus, food/review data, multi-modal",
            "modality": "Text, image",
            "knowledge_cutoff": "June 2024",
            "key_innovation": "Extended context (1M), MoE at scale, domain specialization in food/recommendation",
        },
    },
}


# ═════════════════════════════════════════════════════════════════════════════
# KNOWLEDGE GRAPH UTILITY FUNCTIONS
# ═════════════════════════════════════════════════════════════════════════════

KNOWLEDGE_BASE = {
    "providers": [OPENAI, ANTHROPIC, XAI, QWEN, GLM, META, DEEPSEEK, GOOGLE, LONGCAT],
    "all_models": {},
    "common_datasets": [
        "Common Crawl (filtered web pages)",
        "Wikipedia (all languages)",
        "Books (fiction, non-fiction, academic)",
        "GitHub code (all languages)",
        "arXiv papers",
        "Stack Exchange",
        "Reddit conversations",
        "News articles",
        "Academic journals (various fields)",
    ],
    "common_architectures": [
        "Dense Transformer",
        "MoE Transformer (sparse experts)",
        "Prefix LM (bidirectional attention)",
        "Multi-modal Transformer",
        "Reasoning-augmented Transformer",
    ],
    "common_training_methods": [
        "Next-token prediction (pretraining)",
        "Supervised fine-tuning (SFT)",
        "Reinforcement learning from human feedback (RLHF)",
        "Direct preference optimization (DPO)",
        "Constitutional AI (self-critique + revision)",
        "Rejection sampling",
        "Self-play / self-improvement loops",
        "Knowledge distillation (teacher-student)",
        "Curriculum learning",
    ],
    "alignment_methods": [
        "RLHF (Reinforcement Learning from Human Feedback)",
        "DPO (Direct Preference Optimization)",
        "Constitutional AI",
        "RLAIF (RL from AI Feedback)",
        "Rejection sampling against reward model",
        "Red-teaming + targeted retraining",
        "Safety filtering (input/output guardrails)",
    ],
}

# Build all_models lookup
for provider in KNOWLEDGE_BASE["providers"]:
    for model_name, model_info in provider.get("models", {}).items():
        model_info["provider"] = provider["name"]
        KNOWLEDGE_BASE["all_models"][model_name] = model_info


def get_model_info(model_name: str) -> Optional[Dict[str, Any]]:
    """Get detailed information about a specific frontier model."""
    return KNOWLEDGE_BASE["all_models"].get(model_name)


def get_provider_info(provider_name: str) -> Optional[Dict[str, Any]]:
    """Get information about a specific AI provider."""
    name_map = {p["name"].lower(): p for p in KNOWLEDGE_BASE["providers"]}
    return name_map.get(provider_name.lower())


def get_all_datasets() -> List[str]:
    """Get all unique datasets used across frontier models."""
    datasets = set(KNOWLEDGE_BASE["common_datasets"])
    for p in KNOWLEDGE_BASE["providers"]:
        for ds in p.get("datasets", []):
            datasets.add(ds)
    return sorted(datasets)


def get_all_prompt_patterns() -> Dict[str, List[str]]:
    """Get all system prompt patterns by provider."""
    patterns = {}
    for p in KNOWLEDGE_BASE["providers"]:
        if "prompt_patterns" in p:
            patterns[p["name"]] = p["prompt_patterns"]
    return patterns


def compare_models(model_names: List[str]) -> Dict[str, Any]:
    """Compare multiple frontier models side by side."""
    comparison = {}
    for name in model_names:
        info = get_model_info(name)
        if info:
            comparison[name] = {
                "architecture": info.get("architecture", "N/A"),
                "context_window": info.get("context_window", "N/A"),
                "key_innovation": info.get("key_innovation", "N/A"),
                "inference_cost": info.get("inference_cost", "N/A"),
            }
    return comparison
