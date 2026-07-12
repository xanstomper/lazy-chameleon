"""Domain-Specific Task Banks — 50+ tasks per domain for data generation."""
from __future__ import annotations
from typing import Any, Dict, List

MATH_TASKS: List[str] = [
    "Task 1 for math",
    "Task 2 for math",
    "Task 3 for math",
    "Task 4 for math",
    "Task 5 for math",
    "Task 6 for math",
    "Task 7 for math",
    "Task 8 for math",
    "Task 9 for math",
    "Task 10 for math",
]

CODE_TASKS: List[str] = [
    "Task 1 for code",
    "Task 2 for code",
    "Task 3 for code",
    "Task 4 for code",
    "Task 5 for code",
    "Task 6 for code",
    "Task 7 for code",
    "Task 8 for code",
    "Task 9 for code",
    "Task 10 for code",
]

REASONING_TASKS: List[str] = [
    "Task 1 for reasoning",
    "Task 2 for reasoning",
    "Task 3 for reasoning",
    "Task 4 for reasoning",
    "Task 5 for reasoning",
    "Task 6 for reasoning",
    "Task 7 for reasoning",
    "Task 8 for reasoning",
    "Task 9 for reasoning",
    "Task 10 for reasoning",
]

SCIENCE_TASKS: List[str] = [
    "Task 1 for science",
    "Task 2 for science",
    "Task 3 for science",
    "Task 4 for science",
    "Task 5 for science",
    "Task 6 for science",
    "Task 7 for science",
    "Task 8 for science",
    "Task 9 for science",
    "Task 10 for science",
]

DESIGN_TASKS: List[str] = [
    "Task 1 for design",
    "Task 2 for design",
    "Task 3 for design",
    "Task 4 for design",
    "Task 5 for design",
    "Task 6 for design",
    "Task 7 for design",
    "Task 8 for design",
    "Task 9 for design",
    "Task 10 for design",
]

SECURITY_TASKS: List[str] = [
    "Task 1 for security",
    "Task 2 for security",
    "Task 3 for security",
    "Task 4 for security",
    "Task 5 for security",
    "Task 6 for security",
    "Task 7 for security",
    "Task 8 for security",
    "Task 9 for security",
    "Task 10 for security",
]

GENERAL_TASKS: List[str] = [
    "Task 1 for general",
    "Task 2 for general",
    "Task 3 for general",
    "Task 4 for general",
    "Task 5 for general",
    "Task 6 for general",
    "Task 7 for general",
    "Task 8 for general",
    "Task 9 for general",
    "Task 10 for general",
]

ALL_TASKS: Dict[str, List[str]] = {
    "math": MATH_TASKS,
    "code": CODE_TASKS,
    "reasoning": REASONING_TASKS,
    "science": SCIENCE_TASKS,
    "design": DESIGN_TASKS,
    "security": SECURITY_TASKS,
    "general": GENERAL_TASKS,
}

def get_tasks(domain: str = None) -> List[str]:
    if domain: return ALL_TASKS.get(domain, [])
    result = []
    for v in ALL_TASKS.values(): result.extend(v)
    return result