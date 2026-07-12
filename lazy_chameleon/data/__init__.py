"""
lazy_chameleon.data package.

Provides hardcoded distillation datasets, domain-specific task banks,
curriculum learning data, and evaluation harness examples sourced
from frontier AI models.
"""

from lazy_chameleon.data.hardcoded_datasets import (
    ALL_EXAMPLES,
    MATH_EXAMPLES,
    CODE_EXAMPLES,
    SCIENCE_EXAMPLES,
    LOGIC_EXAMPLES,
    INSTRUCTION_EXAMPLES,
    SECURITY_EXAMPLES,
    CREATIVE_EXAMPLES,
    get_examples_by_domain,
    get_examples_by_difficulty,
    get_examples_by_model,
    get_example_count,
)

from lazy_chameleon.data.domain_data import (
    DOMAIN_TASK_BANKS,
    DOMAIN_NAMES,
    get_domain_tasks,
    get_random_task,
)

from lazy_chameleon.data.curriculum_data import (
    CURRICULUM_STAGES,
    CURRICULUM_EXAMPLES,
    get_stage_examples,
    get_curriculum_progression,
)

from lazy_chameleon.data.eval_harness import (
    EVAL_EXAMPLES,
    EVAL_DOMAINS,
    EVAL_DIFFICULTIES,
    get_eval_by_id,
    get_eval_by_domain,
    run_sample_evaluation,
)

__all__ = [
    "ALL_EXAMPLES",
    "MATH_EXAMPLES",
    "CODE_EXAMPLES",
    "SCIENCE_EXAMPLES",
    "LOGIC_EXAMPLES",
    "INSTRUCTION_EXAMPLES",
    "SECURITY_EXAMPLES",
    "CREATIVE_EXAMPLES",
    "get_examples_by_domain",
    "get_examples_by_difficulty",
    "get_examples_by_model",
    "get_example_count",
    "DOMAIN_TASK_BANKS",
    "DOMAIN_NAMES",
    "get_domain_tasks",
    "get_random_task",
    "CURRICULUM_STAGES",
    "CURRICULUM_EXAMPLES",
    "get_stage_examples",
    "get_curriculum_progression",
    "EVAL_EXAMPLES",
    "EVAL_DOMAINS",
    "EVAL_DIFFICULTIES",
    "get_eval_by_id",
    "get_eval_by_domain",
    "run_sample_evaluation",
]
