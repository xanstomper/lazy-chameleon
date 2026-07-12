"""Lazy Chameleon Harness — System-level wrapper and injector for any LLM."""
from .harness_system_prompt import HARNESS_SYSTEM_PROMPT, HARNESS_SHORT_PROMPT
from .harness_injector import HarnessInjector, detect_injection_triggers
from .harness_wrapper import HarnessWrapper, HarnessConfig
__all__ = ["HARNESS_SYSTEM_PROMPT", "HARNESS_SHORT_PROMPT", "HarnessInjector", "HarnessWrapper", "HarnessConfig", "detect_injection_triggers"]
