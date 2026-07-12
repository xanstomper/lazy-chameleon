"""glm_5_2 - design examples."""
from __future__ import annotations
from typing import Any, Dict, List

glm_5_2_design_examples: List[Dict[str, Any]] = [
    {"instruction": "Design KV store", "response": "Consistent hashing, Raft, LSM-tree.", "difficulty": 0.4},
    {"instruction": "Design file storage (Dropbox)", "response": "Chunk, Merkle tree, delta sync, S3.", "difficulty": 0.7},
    {"instruction": "Design CDN", "response": "Edge servers, anycast DNS, origin pull.", "difficulty": 0.8},
    {"instruction": "Design leaderboard 100M", "response": "Redis sorted sets, shard by score.", "difficulty": 0.6},
]
__all__ = ["glm_5_2_design_examples"]
