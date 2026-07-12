"""Curriculum learning data with difficulty progression stages."""
from __future__ import annotations
from typing import Dict, List, Optional, Tuple
import random

CURRICULUM_STAGES: List[Dict] = [
    {
        "stage": 0,
        "name": "Foundation",
        "difficulty": "easy",
        "description": "Basic concepts and simple problems",
        "domains": ["math", "code"],
        "num_examples": 20,
        "mastery_threshold": 0.8,
        "prerequisites": [],
        "skills": ["arithmetic", "basic_algebra", "simple_loops"],
    },
    {
        "stage": 1,
        "name": "Core Skills",
        "difficulty": "easy",
        "description": "Essential problem-solving skills across all domains",
        "domains": ["math", "code", "logic"],
        "num_examples": 30,
        "mastery_threshold": 0.75,
        "prerequisites": [0],
        "skills": ["proof_techniques", "recursion", "sorting"],
    },
    {
        "stage": 2,
        "name": "Intermediate",
        "difficulty": "easy",
        "description": "Multi-step problems requiring synthesis",
        "domains": ["math", "code", "science", "logic"],
        "num_examples": 35,
        "mastery_threshold": 0.75,
        "prerequisites": [1],
        "skills": ["calculus", "data_structures", "basic_physics"],
    },
    {
        "stage": 3,
        "name": "Advanced Foundations",
        "difficulty": "medium",
        "description": "Advanced techniques and deeper understanding",
        "domains": ["math", "code", "science", "logic", "instruction_following"],
        "num_examples": 40,
        "mastery_threshold": 0.7,
        "prerequisites": [2],
        "skills": ["linear_algebra", "algorithms", "thermodynamics"],
    },
    {
        "stage": 4,
        "name": "Expert Preparation",
        "difficulty": "medium",
        "description": "Complex multi-domain problems",
        "domains": ["math", "code", "science", "logic", "security"],
        "num_examples": 40,
        "mastery_threshold": 0.7,
        "prerequisites": [3],
        "skills": ["differential_equations", "concurrency", "quantum_mechanics"],
    },
    {
        "stage": 5,
        "name": "Expert",
        "difficulty": "hard",
        "description": "Expert-level problems from competition and research",
        "domains": ["math", "code", "science"],
        "num_examples": 30,
        "mastery_threshold": 0.65,
        "prerequisites": [4],
        "skills": ["number_theory", "system_design", "relativity"],
    },
    {
        "stage": 6,
        "name": "Mastery",
        "difficulty": "expert",
        "description": "Cutting-edge frontier problems",
        "domains": ["math", "code", "science", "logic", "creative"],
        "num_examples": 20,
        "mastery_threshold": 0.6,
        "prerequisites": [5],
        "skills": ["research", "innovation", "cross_domain_synthesis"],
    },
]

# Pre-built curriculum progression mapping
CURRICULUM_EXAMPLES: List[Dict] = [
    {"stage": 0, "instruction": "Solve 2x+3=7", "expected_difficulty": "easy", "domain": "math", "skill": "basic_algebra"},
    {"stage": 0, "instruction": "Write a for loop in Python that prints 1 to 5", "expected_difficulty": "easy", "domain": "code", "skill": "simple_loops"},
    {"stage": 0, "instruction": "Calculate 15 percent of 200", "expected_difficulty": "easy", "domain": "math", "skill": "arithmetic"},
    {"stage": 0, "instruction": "What is the capital of France?", "expected_difficulty": "easy", "domain": "general", "skill": "facts"},
    {"stage": 1, "instruction": "Prove that the sum of two even numbers is even", "expected_difficulty": "easy", "domain": "math", "skill": "proof_techniques"},
    {"stage": 1, "instruction": "Implement a recursive factorial function", "expected_difficulty": "easy", "domain": "code", "skill": "recursion"},
    {"stage": 1, "instruction": "Syllogism: All men are mortal. Socrates is a man. Is Socrates mortal?", "expected_difficulty": "easy", "domain": "logic", "skill": "syllogisms"},
    {"stage": 1, "instruction": "Implement bubble sort", "expected_difficulty": "easy", "domain": "code", "skill": "sorting"},
    {"stage": 2, "instruction": "Find the derivative of x^3*sin(x)", "expected_difficulty": "medium", "domain": "math", "skill": "calculus"},
    {"stage": 2, "instruction": "Implement a stack using arrays", "expected_difficulty": "medium", "domain": "code", "skill": "data_structures"},
    {"stage": 2, "instruction": "Calculate the force between two charged particles", "expected_difficulty": "medium", "domain": "science", "skill": "basic_physics"},
    {"stage": 2, "instruction": "Knights and knaves logic puzzle", "expected_difficulty": "medium", "domain": "logic", "skill": "truth_tellers"},
    {"stage": 3, "instruction": "Find the eigenvalues of a 3x3 matrix", "expected_difficulty": "medium", "domain": "math", "skill": "linear_algebra"},
    {"stage": 3, "instruction": "Implement Dijkstra's shortest path", "expected_difficulty": "hard", "domain": "code", "skill": "algorithms"},
    {"stage": 3, "instruction": "Explain the second law of thermodynamics", "expected_difficulty": "medium", "domain": "science", "skill": "thermodynamics"},
    {"stage": 3, "instruction": "Write a detailed recipe for chocolate cake following specific formatting", "expected_difficulty": "medium", "domain": "instruction_following", "skill": "formatting"},
    {"stage": 4, "instruction": "Solve the differential equation y''+y=0", "expected_difficulty": "hard", "domain": "math", "skill": "differential_equations"},
    {"stage": 4, "instruction": "Implement a thread-safe concurrent cache", "expected_difficulty": "hard", "domain": "code", "skill": "concurrency"},
    {"stage": 4, "instruction": "Explain the double-slit experiment implications", "expected_difficulty": "hard", "domain": "science", "skill": "quantum_mechanics"},
    {"stage": 4, "instruction": "Identify the SQL injection vulnerability in this code", "expected_difficulty": "hard", "domain": "security", "skill": "injection"},
    {"stage": 5, "instruction": "Prove the infinitude of primes in arithmetic progression 4k+3", "expected_difficulty": "hard", "domain": "math", "skill": "number_theory"},
    {"stage": 5, "instruction": "Design a distributed key-value store with consistency guarantees", "expected_difficulty": "hard", "domain": "code", "skill": "system_design"},
    {"stage": 5, "instruction": "Calculate time dilation for a spaceship at 0.9c", "expected_difficulty": "hard", "domain": "science", "skill": "relativity"},
    {"stage": 6, "instruction": "Prove the Riemann Hypothesis consequences for prime distribution", "expected_difficulty": "expert", "domain": "math", "skill": "research"},
    {"stage": 6, "instruction": "Design a novel consensus algorithm with sub-linear message complexity", "expected_difficulty": "expert", "domain": "code", "skill": "innovation"},
    {"stage": 6, "instruction": "Unify quantum mechanics and general relativity conceptually", "expected_difficulty": "expert", "domain": "science", "skill": "cross_domain_synthesis"},
]


def get_stage_examples(stage: int) -> List[Dict]:
    """Get curriculum examples for a specific stage."""
    return [ex for ex in CURRICULUM_EXAMPLES if ex["stage"] == stage]


def get_curriculum_progression() -> List[Dict]:
    """Return the full progression with stage metadata."""
    progression = []
    for stage in CURRICULUM_STAGES:
        examples = get_stage_examples(stage["stage"])
        progression.append({
            "stage": stage,
            "examples": examples,
        })
    return progression


def get_next_stage(current_stage: int, accuracy: float) -> Optional[int]:
    """Determine if student should advance to next stage based on accuracy."""
    stages = {s["stage"]: s for s in CURRICULUM_STAGES}
    if current_stage not in stages:
        return None
    stage = stages[current_stage]
    if accuracy >= stage["mastery_threshold"]:
        return current_stage + 1
    return current_stage


__all__ = [
    "CURRICULUM_STAGES", "CURRICULUM_EXAMPLES",
    "get_stage_examples", "get_curriculum_progression",
    "get_next_stage",
]
