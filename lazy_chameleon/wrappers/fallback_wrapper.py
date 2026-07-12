"""FallbackWrapper — Automatic fallback between providers on failure."""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional
import logging

logger = logging.getLogger(__name__)

@dataclass
class FallbackStrategy:
    providers: List[str] = field(default_factory=lambda: ["anthropic", "openai", "deepseek"])
    retry_delay: float = 1.0
    exponential_backoff: bool = True
    max_retries_per_provider: int = 2

class FallbackWrapper:
    def __init__(self, strategy: Optional[FallbackStrategy] = None):
        self.strategy = strategy or FallbackStrategy()

    def execute(self, prompt: str, **kwargs) -> Any:
        from lazy_chameleon.bridges import ProviderRegistry
        registry = ProviderRegistry()
        last_error = None
        for provider in self.strategy.providers:
            for attempt in range(self.strategy.max_retries_per_provider):
                try:
                    bridge = registry.get_bridge(provider)
                    return bridge.generate(prompt, **kwargs)
                except Exception as e:
                    last_error = e
                    logger.warning(f"{provider} attempt {attempt+1} failed: {e}")
                    if self.strategy.exponential_backoff:
                        import time
                        time.sleep(self.strategy.retry_delay * (2 ** attempt))
        raise RuntimeError(f"All providers failed: {last_error}")
