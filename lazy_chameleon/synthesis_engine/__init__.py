"""Synthesis Engine — Scales 480B MoE to 1-5T using real synthetic parameters.

Components:
- ParamScaleEngine: Scales architecture (experts, layers, hidden size)
- FrontierMimic: Main agent mimics frontier models using synthesized params
- LazySynthesisCluster: 64 lazy synthesizers generating in parallel
- ParameterBrewingPipeline: End-to-end pipeline
"""
from .param_scale_engine import ParamScaleEngine, ParamScaleConfig, ScaledConfig
from .frontier_mimic import FrontierMimic, FrontierProfile, FRONTIER_PROFILES
from .lazy_synthesis_cluster import LazySynthesisCluster, LazySynthesizer
from .brewing_pipeline import ParameterBrewingPipeline, PipelineResult
__all__ = ["ParamScaleEngine", "ParamScaleConfig", "ScaledConfig",
           "FrontierMimic", "FrontierProfile", "FRONTIER_PROFILES",
           "LazySynthesisCluster", "LazySynthesizer",
           "ParameterBrewingPipeline", "PipelineResult"]
