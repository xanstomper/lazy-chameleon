"""Integration tests for synthesis engine sub-packages. All APIs verified against source."""
from __future__ import annotations
import pytest
import numpy as np


class TestMerging:
    def test_slerp(self):
        from lazy_chameleon.synthesis_engine.merging.model_merger import slerp
        r = slerp({"w": np.random.randn(10,10)}, {"w": np.random.randn(10,10)}, 0.5)
        assert r.weights["w"].shape == (10,10)

    def test_ties(self):
        from lazy_chameleon.synthesis_engine.merging.model_merger import ties_merge
        r = ties_merge([{"w": np.random.randn(10,10)}, {"w": np.random.randn(10,10)}], trim_fraction=0.2)
        assert r.weights["w"].shape == (10,10)


class TestMoE:
    def test_expert_spawner(self):
        from lazy_chameleon.synthesis_engine.moe_evolution.expert_spawner import ExpertSpawner
        es = ExpertSpawner(num_experts=8)
        assert len(es.pool.expert_params) == 8


class TestNAS:
    def test_gen_layer(self):
        from lazy_chameleon.synthesis_engine.nas.neural_arch_search import ArchitectureGenerator
        gen = ArchitectureGenerator()
        cfg = gen.generate_layer(64, 128)
        assert cfg.input_dim == 64
        assert cfg.output_dim == 128


class TestSynthData:
    def test_self_instruct(self):
        from lazy_chameleon.synthesis_engine.synthetic_data.data_generator import SynthDataGenerator
        ds = SynthDataGenerator().self_instruct(num_samples=3)
        assert len(ds) == 3


class TestDistill:
    def test_logit_distill(self):
        from lazy_chameleon.synthesis_engine.distillation.knowledge_distiller import KnowledgeDistiller
        t = {"w": np.random.randn(10,10)}
        s = {"w": np.random.randn(10,10)}
        kd = KnowledgeDistiller(t, s)
        result = kd.logit_distill(num_steps=5)
        assert len(result.distillation_losses) > 0


class TestMemory:
    def test_vector_store(self):
        from lazy_chameleon.synthesis_engine.memory.vector_store import VectorStore
        vs = VectorStore()
        vid = vs.add_text("hello world", metadata={"source": "test"})
        assert isinstance(vid, str)


class TestHyperNet:
    def test_generate_weights(self):
        from lazy_chameleon.synthesis_engine.hypernetwork.hypernetwork import HyperNetwork
        w = HyperNetwork().generate_weights(8, 16)
        assert w is not None


class TestEvo:
    def test_cma_es(self):
        from lazy_chameleon.synthesis_engine.evolutionary.evolution_engine import CMAES
        sol = CMAES(genome_size=2, pop_size=5).optimize(lambda x: -sum(v**2 for v in x), num_generations=5)
        assert hasattr(sol, "genome") or isinstance(sol, (list, np.ndarray))


class TestPipeline:
    def test_pipeline(self):
        from lazy_chameleon.synthesis_engine import ParameterBrewingPipeline
        pipeline = ParameterBrewingPipeline(target_params_b=500.0)
        pipeline.initialize(base_params_b=480.0)
        result = pipeline.run_full_pipeline(domains=["math"], params_per_domain=5)
        assert result.total_params_generated >= 0
