"""All datasets used by frontier models."""
from __future__ import annotations
from typing import Any, Dict, List

FRONTIER_DATASETS = {
    "pretraining": [
        {"name": "Common Crawl", "used_by": ["GPT", "Claude", "Grok", "Qwen"]},
        {"name": "Wikipedia", "used_by": ["ALL"]},
        {"name": "BooksCorpus", "used_by": ["GPT", "Claude"]},
        {"name": "GitHub Code", "used_by": ["ALL"]},
        {"name": "arXiv Papers", "used_by": ["ALL"]},
    ],
    "instruction": [
        {"name": "ShareGPT", "size": "~1M conversations"},
        {"name": "Synthetic Instructions", "size": "Can generate unlimited"},
    ],
    "reasoning": [
        {"name": "MATH Dataset", "size": "~12K problems"},
        {"name": "GSM8K", "size": "~8K problems"},
        {"name": "CodeContests", "size": "~13K"},
    ],
    "multilingual": [
        {"name": "Chinese Web Corpus", "size": "~10T tokens"},
        {"name": "mC4", "size": "~6.3T tokens, 101 langs"},
    ],
}

def get_all_datasets() -> List[str]:
    ds = set()
    for cat in FRONTIER_DATASETS:
        for d in FRONTIER_DATASETS[cat]: ds.add(d["name"])
    return sorted(ds)
