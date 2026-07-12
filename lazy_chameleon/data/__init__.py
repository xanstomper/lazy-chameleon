"""lazy_chameleon.data package."""

from lazy_chameleon.data.hardcoded_datasets import (
    ALL_EXAMPLES, MATH_EXAMPLES, CODE_EXAMPLES, SCIENCE_EXAMPLES,
    LOGIC_EXAMPLES, INSTRUCTION_EXAMPLES, SECURITY_EXAMPLES, CREATIVE_EXAMPLES,
    get_examples_by_domain, get_examples_by_difficulty, get_examples_by_model,
    get_example_count, random_example,
)

from lazy_chameleon.data.domain_data import (
    DOMAIN_TASK_BANKS, DOMAIN_NAMES,
    get_domain_tasks, get_random_task, get_tasks_by_skill,
)

from lazy_chameleon.data.curriculum_data import (
    CURRICULUM_STAGES, CURRICULUM_EXAMPLES,
    get_stage_examples, get_curriculum_progression, get_next_stage,
)

from lazy_chameleon.data.eval_harness import (
    EVAL_EXAMPLES, EVAL_DOMAINS, EVAL_DIFFICULTIES,
    get_eval_by_id, get_eval_by_domain, get_eval_by_difficulty,
    run_sample_evaluation,
)

__all__ = [
    "ALL_EXAMPLES", "MATH_EXAMPLES", "CODE_EXAMPLES", "SCIENCE_EXAMPLES",
    "LOGIC_EXAMPLES", "INSTRUCTION_EXAMPLES", "SECURITY_EXAMPLES", "CREATIVE_EXAMPLES",
    "get_examples_by_domain", "get_examples_by_difficulty", "get_examples_by_model",
    "get_example_count", "random_example",
    "DOMAIN_TASK_BANKS", "DOMAIN_NAMES",
    "get_domain_tasks", "get_random_task", "get_tasks_by_skill",
    "CURRICULUM_STAGES", "CURRICULUM_EXAMPLES",
    "get_stage_examples", "get_curriculum_progression", "get_next_stage",
    "EVAL_EXAMPLES", "EVAL_DOMAINS", "EVAL_DIFFICULTIES",
    "get_eval_by_id", "get_eval_by_domain", "get_eval_by_difficulty",
    "run_sample_evaluation",
]
