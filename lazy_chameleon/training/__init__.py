"""Lazy Chameleon Training Infrastructure.

Comprehensive training pipeline for distilling teacher model reasoning into
faster student models. Includes:

- Synthetic data generation with task taxonomies
- Knowledge distillation (Chain-of-Thought, Constitutional AI)
- Training via LoRA or OpenAI fine-tuning API
- Multi-benchmark evaluation framework
- Dataset management and mixing
"""

from .synthetic_data_generator import (
    SyntheticDataGenerator,
    TaskTaxonomy,
    DataPoint,
    DataAugmentor,
    DatasetExporter,
)
from .distiller import (
    ChainOfThoughtDistiller,
    ConstitutionalDistiller,
    MultiTeacherEnsemble,
    InferenceTimeDistiller,
    PatternLibrary,
)
from .trainer import TrainingConfig, LoRATrainer, OpenAIFineTuner, DataPreparer
from .evaluator import (
    BenchmarkEvaluator,
    PairwiseEvaluator,
    ConstitutionalEvaluator,
    EvalResult,
)
from .dataset import TrainingDataset, DataMixer

__all__ = [
    # Data Generation
    "SyntheticDataGenerator",
    "TaskTaxonomy",
    "DataPoint",
    "DataAugmentor",
    "DatasetExporter",
    # Distillation
    "ChainOfThoughtDistiller",
    "ConstitutionalDistiller",
    "MultiTeacherEnsemble",
    "InferenceTimeDistiller",
    "PatternLibrary",
    # Training
    "TrainingConfig",
    "LoRATrainer",
    "OpenAIFineTuner",
    "DataPreparer",
    # Evaluation
    "BenchmarkEvaluator",
    "PairwiseEvaluator",
    "ConstitutionalEvaluator",
    "EvalResult",
    # Dataset
    "TrainingDataset",
    "DataMixer",
]

__version__ = "0.1.0"
