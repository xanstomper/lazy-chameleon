"""All datasets used by frontier models."""
from __future__ import annotations
from typing import Any, Dict, List


FRONTIER_DATASETS = {
    "pretraining": [
        {"name": "Common Crawl", "size": "~50B pages", "used_by": ["GPT", "Claude", "Grok", "Qwen", "Llama"]},
        {"name": "Wikipedia", "size": "~6M articles, 100+ languages", "used_by": ["ALL"]},
        {"name": "BooksCorpus", "size": "~7M books", "used_by": ["GPT", "Claude", "Grok"]},
        {"name": "GitHub Code", "size": "~200M repos", "used_by": ["ALL"]},
        {"name": "arXiv Papers", "size": "~2M papers", "used_by": ["ALL"]},
        {"name": "Stack Exchange", "size": "~20M Q&A", "used_by": ["GPT", "Claude", "DeepSeek"]},
        {"name": "Reddit Comments", "size": "~5B comments", "used_by": ["GPT"]},
        {"name": "Chinese Web (Baidu)", "size": "~10B pages", "used_by": ["Qwen", "GLM"]},
        {"name": "X/Twitter Feed", "size": "Real-time", "used_by": ["Grok"]},
        {"name": "YouTube Transcripts", "size": "~1B hours", "used_by": ["Gemini", "GPT-5"]},
    ],
    "instruction": [
        {"name": "ShareGPT", "size": "~1M conversations", "used_by": ["GPT", "Claude"]},
        {"name": "OpenAssistant", "size": "~161K conversations", "used_by": ["Open-source models"]},
        {"name": "Synthetic Instructions (Self-Instruct)", "size": "Varies (can generate unlimited)", "used_by": ["ALL"]},
        {"name": "Evol-Instruct Data", "size": "~250K evolving instructions", "used_by": ["WizardLM family"]},
        {"name": "Constitutional AI Data", "size": "Proprietary", "used_by": ["Claude"]},
        {"name": "RLHF Comparison Data", "size": "~1M comparisons", "used_by": ["GPT", "Claude"]},
    ],
    "reasoning": [
        {"name": "MATH Dataset", "size": "~12K problems", "used_by": ["ALL"]},
        {"name": "GSM8K", "size": "~8K math word problems", "used_by": ["ALL"]},
        {"name": "CodeContests", "size": "~13K competitive programming", "used_by": ["DeepSeek", "GPT"]},
        {"name": "Synthetic Reasoning Traces", "size": "Can generate millions", "used_by": ["DeepSeek-R1", "GPT-o"]},
        {"name": "Proof-Pile", "size": "~8B tokens of math proofs", "used_by": ["DeepSeek", "GPT"]},
    ],
    "multilingual": [
        {"name": "Chinese Web Corpus", "size": "~10T tokens", "used_by": ["Qwen", "GLM"]},
        {"name": "mC4 (multilingual C4)", "size": "~6.3T tokens, 101 languages", "used_by": ["Qwen", "GLM"]},
        {"name": "CC-100 (CommonCrawl 100 langs)", "size": "~100T tokens", "used_by": ["Qwen"]},
    ],
}

