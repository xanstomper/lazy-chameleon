"""claude_opus_4_8 - design examples."""
from __future__ import annotations
from typing import Any, Dict, List

claude_opus_4_8_design_examples: List[Dict[str, Any]] = [
    {"instruction": "Design KV store", "response": "Consistent hashing, Raft, LSM-tree.", "difficulty": 0.6},
    {"instruction": "Design chat for 10M", "response": "WebSocket, Redis pub/sub, Cassandra, Kafka.", "difficulty": 0.6},
    {"instruction": "Design file storage (Dropbox)", "response": "Chunk, Merkle tree, delta sync, S3.", "difficulty": 0.3},
    {"instruction": "Design CDN", "response": "Edge servers, anycast DNS, origin pull.", "difficulty": 0.6},
]
__all__ = ["claude_opus_4_8_design_examples"]
