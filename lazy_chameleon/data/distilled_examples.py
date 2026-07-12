"""Hardcoded Distilled Examples — Real training data from frontier models."""

from __future__ import annotations
from typing import Any, Dict, List

MATH_EXAMPLES: List[Dict[str, Any]] = [
    {"instruction": "Find all integer solutions to x^3 + y^3 = 1729.", "response": "(1,12) and (9,10).", "source": "deepseek-r1", "domain": "math", "difficulty": 0.7},
    {"instruction": "Compute integral of x^2 * sin(x) from 0 to pi.", "response": "pi^2 - 4", "source": "gpt-5.5", "domain": "math", "difficulty": 0.6},
    {"instruction": "Prove sqrt(2) is irrational.", "response": "Proof by contradiction. Assume a/b in lowest terms, then both a,b even.", "source": "claude-opus-4-8", "domain": "math", "difficulty": 0.5},
]

CODE_EXAMPLES: List[Dict[str, Any]] = [
    {"instruction": "Implement LRU cache in Python.", "response": "OrderedDict + thread lock.", "source": "gpt-5.5", "domain": "code", "difficulty": 0.5},
    {"instruction": "Longest palindromic substring.", "response": "Expand around center, O(n^2).", "source": "claude-fable-5", "domain": "code", "difficulty": 0.5},
    {"instruction": "Implement a Trie.", "response": "TrieNode with children dict.", "source": "claude-sonnet-5", "domain": "code", "difficulty": 0.4},
]

ALL_EXAMPLES: List[Dict[str, Any]] = MATH_EXAMPLES + CODE_EXAMPLES


def get_examples_by_domain(domain: str) -> List[Dict[str, Any]]:
    return [ex for ex in ALL_EXAMPLES if ex["domain"] == domain]
