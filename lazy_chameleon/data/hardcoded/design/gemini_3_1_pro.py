"""gemini_3_1_pro - design examples."""
from __future__ import annotations
from typing import Any, Dict, List

gemini_3_1_pro_design_examples: List[Dict[str, Any]] = [
    {"instruction": "Design KV store", "response": "Consistent hashing, Raft, LSM-tree.", "difficulty": 0.5},
    {"instruction": "Design CDN", "response": "Edge servers, anycast DNS, origin pull.", "difficulty": 0.3},
    {"instruction": "Design leaderboard 100M", "response": "Redis sorted sets, shard by score.", "difficulty": 0.8},
    {"instruction": "Design chat for 10M", "response": "WebSocket, Redis pub/sub, Cassandra, Kafka.", "difficulty": 0.7},
    {"instruction": "Design recommendation system", "response": "Collaborative + content-based NN.", "difficulty": 0.6},
]
__all__ = ["gemini_3_1_pro_design_examples"]
