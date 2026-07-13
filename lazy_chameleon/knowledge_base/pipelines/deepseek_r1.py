"""DeepSeek-R1 reasoning pipeline with GRPO and rejection sampling."""
from __future__ import annotations
from typing import Any, Callable, Dict, List, Optional
import numpy as np

class GRPO:
    def __init__(self, group_size: int = 64, kl_penalty: float = 0.04, lr: float = 1e-6):
        self.group_size = group_size
        self.kl = kl_penalty
        self.lr = lr
        self._stats: List[Dict] = []

    def compute_advantages(self, rewards: List[float]) -> np.ndarray:
        r = np.array(rewards)
        return (r - r.mean()) / (r.std() + 1e-10)

    def step(self, log_probs, old_log_probs, ref_log_probs, rewards):
        adv = self.compute_advantages(rewards)
        ratios = np.exp(log_probs - old_log_probs)
        clipped = np.clip(ratios, 0.8, 1.2)
        policy_loss = -np.mean(np.minimum(ratios * adv, clipped * adv))
        kl = float(np.mean(np.exp(ref_log_probs) * (ref_log_probs - log_probs)))
        total = float(policy_loss) + self.kl * kl
        record = {"policy_loss": float(policy_loss), "kl": kl, "total": total}
        self._stats.append(record)
        return record

class DeepSeekR1Pipeline:
    def __init__(self, episodes: int = 1000, group_size: int = 64):
        self.episodes = episodes
        self.group_size = group_size
        self._log: List[Dict] = []
        self._best: List[Dict] = []

    def cold_start(self, problems: List[str], solutions: List[str]) -> List[Dict]:
        data = [{"problem": p, "solution": s, "type": "cold_start"} for p, s in zip(problems, solutions)]
        self._best.extend(data)
        return data

    def generate_trace(self, problem: str, model_fn: Callable) -> Dict:
        trace = {"problem": problem, "steps": [], "final": None}
        for _ in range(20):
            step = model_fn(problem, trace["steps"])
            trace["steps"].append(step)
            if step.get("is_final"):
                trace["final"] = step.get("answer")
                break
        return trace

    def rejection_sample(self, traces: List[Dict], reward_fn: Callable, keep: float = 0.3) -> List[Dict]:
        scored = [(reward_fn(t), t) for t in traces]
        scored.sort(key=lambda x: -x[0])
        kept = [t for _, t in scored[:max(1, int(len(scored)*keep))]]
        self._best.extend(kept)
        return kept

    def train_episode(self, problems: List[str], model_fn: Callable, reward_fn: Callable, grpo: GRPO) -> Dict:
        traces = [self.generate_trace(p, model_fn) for p in problems[:self.group_size]]
        rewards = [reward_fn(t) for t in traces]
        good = self.rejection_sample(traces, reward_fn, 0.3)
        record = {"episode": len(self._log), "avg_reward": float(np.mean(rewards)), "kept": len(good)}
        self._log.append(record)
        return record
