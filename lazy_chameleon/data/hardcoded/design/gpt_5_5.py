"""gpt_5_5 - design examples."""
from __future__ import annotations
from typing import Any, Dict, List

gpt_5_5_design_examples: List[Dict[str, Any]] = [
    {"instruction": "Design file storage (Dropbox)", "response": "Chunk, Merkle tree, delta sync, S3.", "difficulty": 0.7},
    {"instruction": "Design leaderboard 100M", "response": "Redis sorted sets, shard by score.", "difficulty": 0.4},
    {"instruction": "Design KV store", "response": "Consistent hashing, Raft, LSM-tree.", "difficulty": 0.4},
    {"instruction": "Design CDN", "response": "Edge servers, anycast DNS, origin pull.", "difficulty": 0.3},
    {"instruction": "Design chat for 10M", "response": "WebSocket, Redis pub/sub, Cassandra, Kafka.", "difficulty": 0.7},
]
__all__ = ["gpt_5_5_design_examples"]
