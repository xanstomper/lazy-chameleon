"""MoEResearch — Main agent commands spawned experts to research topics via webcrawler.

Flow:
1. Main expert says: "Research {topic}"
2. Main agent splits into hunter/gatherer cells
3. Each child cell uses the webcrawler to scrape topic from web + knowledge base
4. Cells merge back with their research findings
5. Main agent now has researched knowledge

No dashboard. No user input. Fully automatic.
"""
from __future__ import annotations
from typing import Any, Callable, Dict, List, Optional, Tuple
import time
import logging

logger = logging.getLogger(__name__)


class MoEResearch:
    def __init__(self):
        self._crawler = None
        self._research_log: List[Dict] = []
        self._init_crawler()

    def _init_crawler(self):
        try:
            from lazy_chameleon.moe_controller.web import MoEWebCrawler
            self._crawler = MoEWebCrawler()
            logger.info("WebCrawler ready for research")
        except Exception as e:
            logger.warning(f"Crawler init: {e}")

    def research(self, topic: str, domain: str = "general", depth: str = "standard") -> Dict[str, Any]:
        """Main agent researches a topic by commanding spawned experts to crawl it."""
        t0 = time.time()
        if not self._crawler:
            self._init_crawler()
        
        # Main agent creates crawl jobs (tells spawned experts what to research)
        sources_to_check = []
        if domain in ["math", "code", "reasoning", "science", "design", "security", "general"]:
            sources_to_check.append(f"knowledge_base:{domain}")
        sources_to_check.append(f"web:{topic}")
        
        results = []
        for source_desc in sources_to_check:
            for expert_id in range(1, 5):  # Spawn 4 research cells
                try:
                    query = f"{topic} {domain}"
                    jid = self._crawler.create_job(expert_id, domain, query, max_docs=20)
                    job = self._crawler.run_job(jid)
                    training = self._crawler.job_to_training(jid)
                    results.extend(training)
                except Exception as e:
                    logger.warning(f"Research cell {expert_id} error: {e}")
        
        # Merge all findings
        merged = self._merge_findings(results, topic, domain)
        merged["research_time_s"] = round(time.time() - t0, 2)
        merged["sources_checked"] = sources_to_check
        merged["cells_deployed"] = 4
        merged["total_findings"] = len(results)
        
        self._research_log.append(merged)
        return merged

    def _merge_findings(self, findings: List[Dict], topic: str, domain: str) -> Dict[str, Any]:
        """Merge all research findings into a structured result."""
        instructions = []
        responses = []
        sources = set()
        for f in findings:
            if f.get("instruction"):
                instructions.append(f["instruction"])
            if f.get("response"):
                responses.append(f["response"])
            if f.get("source"):
                sources.add(f["source"])
        return {
            "topic": topic,
            "domain": domain,
            "summary": f"Researched {topic} in {domain} domain using {len(sources)} knowledge sources",
            "key_instructions": instructions[:10],
            "key_responses": responses[:10],
            "knowledge_sources": list(sources),
            "total_raw_findings": len(findings),
        }

    def research_and_inject(self, topic: str, domain: str = "general") -> str:
        """Research a topic and return a ready-to-use context string."""
        result = self.research(topic, domain)
        context = f"Research on '{topic}' ({domain}):\n"
        for instr in result.get("key_instructions", [])[:5]:
            context += f"  - {instr}\n"
        context += f"\nSources: {', '.join(result.get('knowledge_sources', ['knowledge_base']))}"
        return context

    def get_history(self) -> List[Dict]:
        return list(self._research_log)
