"""grok_4_4 - design examples."""
from __future__ import annotations
from typing import Any, Dict, List

grok_4_4_design_examples: List[Dict[str, Any]] = [
    {"instruction": "Design file storage (Dropbox)", "response": "Chunk, Merkle tree, delta sync, S3.", "difficulty": 0.9},
    {"instruction": "Design chat for 10M", "response": "WebSocket, Redis pub/sub, Cassandra, Kafka.", "difficulty": 0.3},
    {"instruction": "Design KV store", "response": "Consistent hashing, Raft, LSM-tree.", "difficulty": 0.3},
    {"instruction": "Design recommendation system", "response": "Collaborative + content-based NN.", "difficulty": 0.3},
    {"instruction": "Design leaderboard 100M", "response": "Redis sorted sets, shard by score.", "difficulty": 0.6},
]
__all__ = ["grok_4_4_design_examples"]
