"""
Lazy Chameleon — System Prompt Library

A browsable, searchable library of 280+ leaked system prompts from frontier AI
models (Anthropic, OpenAI, Google, xAI, Meta, Microsoft, Mistral, Qwen,
Perplexity, Cursor, and more).

Provides SystemPromptLibrary for reading, browsing, and searching prompts,
and a CLI interface via `chameleon prompts`.
"""

from __future__ import annotations

import os
import re
import fnmatch
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

# ──────────────────────────────────────────────────────────────────────────────
# Data Model
# ──────────────────────────────────────────────────────────────────────────────

@dataclass
class SystemPrompt:
    """Represents a single system prompt from the library.

    Attributes
    ----------
    provider  : Normalised provider name (e.g. ``"anthropic"``).
    model     : Model identifier derived from the file stem (e.g. ``"claude-opus-4"``).
    file_path : Absolute path to the markdown file on disk.
    content   : The full text content of the prompt (loaded lazily).
    tags      : Optional list of tags for categorisation.
    """

    provider: str
    model: str
    file_path: str
    content: str = ""
    tags: List[str] = field(default_factory=list)

    # ── Convenience ────────────────────────────────────────────────────────
    @property
    def stem(self) -> str:
        """File stem without directory or extension."""
        return Path(self.file_path).stem

    @property
    def size_bytes(self) -> int:
        """File size in bytes."""
        try:
            return os.path.getsize(self.file_path)
        except OSError:
            return 0

    def load(self) -> str:
        """Explicitly load / re-load content from disk."""
        try:
            with open(self.file_path, "r", encoding="utf-8", errors="replace") as fh:
                self.content = fh.read()
        except OSError:
            self.content = ""
        return self.content

    def __len__(self) -> int:
        return len(self.content) if self.content else self.size_bytes

_PROVIDER_DIR_MAP = {
    "anthropic": "anthropic",
    "openai": "openai",
    "google": "google",
    "xai": "xai",
    "meta": "meta",
    "microsoft": "microsoft",
    "misc": "misc",
    "mistral": "mistral",
    "notion": "notion",
    "perplexity": "perplexity",
    "qwen": "qwen",
    "cursor": "cursor",
}


class SystemPromptLibrary:
    """Browsable, searchable library of leaked system prompts.

    Scans the ``prompts/`` package directory on initialisation and indexes
    every ``.md`` file, organising them by provider and model name.

    Typical usage::

        lib = SystemPromptLibrary()
        for p in lib.search("claude opus"):
            print(p.model, p.provider)

        stats = lib.get_stats()
        print(f"{stats['total']} prompts across {stats['providers']} providers")
    """

    def __init__(self, base_dir: Optional[str] = None):
        self._base_dir = Path(base_dir or _default_base_dir())
        self._prompts: Dict[str, SystemPrompt] = {}     # path -> prompt
        self._by_provider: Dict[str, List[SystemPrompt]] = {}
        self._by_model: Dict[str, List[SystemPrompt]] = {}
        self._tags_index: Dict[str, List[SystemPrompt]] = {}
        self._scanned: bool = False

    # ── Public API ─────────────────────────────────────────────────────────

    def browse(
        self,
        provider: Optional[str] = None,
        model: Optional[str] = None,
        tag: Optional[str] = None,
    ) -> List[SystemPrompt]:
        """Browse prompts, optionally filtered by *provider*, *model*, or *tag*.

        Returns a list of :class:`SystemPrompt` objects matching all supplied
        criteria.  Pass no arguments to get *all* prompts.
        """
        self._ensure_scanned()

        results: Dict[str, SystemPrompt] = {}

        if tag:
            for p in self._tags_index.get(tag, []):
                results[p.file_path] = p
        if provider:
            for p in self._by_provider.get(provider, []):
                results[p.file_path] = p
        if model:
            for p in self._by_model.get(model, []):
                results[p.file_path] = p

        if tag or provider or model:
            return list(results.values())

        # No filters -> return everything
        return list(self._prompts.values())

    def search(self, query: str) -> List[SystemPrompt]:
        """Full-text search across all prompt contents.

        Basic word-level matching (case-insensitive).  Returns prompts ranked
        by number of query terms matched (descending).
        """
        self._ensure_scanned()
        terms = [t.lower() for t in query.split() if t]
        if not terms:
            return []

        scored: List[Tuple[int, SystemPrompt]] = []
        for prompt in self._prompts.values():
            content = prompt.load().lower()
            score = sum(1 for t in terms if t in content)
            # Boost matches on file stem / model name
            stem_lower = prompt.stem.lower()
            score += sum(2 for t in terms if t in stem_lower)
            if score:
                scored.append((score, prompt))

        scored.sort(key=lambda x: (-x[0], x[1].model))
        return [p for _, p in scored]

    def get(self, path: str) -> Optional[SystemPrompt]:
        """Get a specific prompt by its *relative* or *absolute* path.

        The *path* can be:
        * An absolute file path.
        * A path relative to the library base directory.
        * A provider-relative path like ``"anthropic/claude-opus-4.md"``.
        """
        self._ensure_scanned()

        # Try as-is
        if path in self._prompts:
            return self._prompts[path]

        # Try resolving relative to base
        resolved = str(self._base_dir / path)
        if resolved in self._prompts:
            return self._prompts[resolved]

        # Try with .md extension
        if not resolved.endswith(".md"):
            resolved_md = resolved + ".md"
            if resolved_md in self._prompts:
                return self._prompts[resolved_md]

        # Try basename match
        for p_path, prompt in self._prompts.items():
            if prompt.stem == Path(path).stem:
                return prompt

        return None

    def list_providers(self) -> List[str]:
        """Return sorted list of all provider names in the library."""
        self._ensure_scanned()
        return sorted(self._by_provider.keys())

    def list_models(self, provider: str) -> List[str]:
        """Return sorted list of model names for a given *provider*."""
        self._ensure_scanned()
        prompts = self._by_provider.get(provider, [])
        return sorted(set(p.model for p in prompts))

    def get_stats(self) -> Dict:
        """Return summary statistics about the library.

        Returns a dict with keys: ``total``, ``providers``, ``models``,
        ``total_size_bytes``, and per-provider breakdown.
        """
        self._ensure_scanned()
        total = len(self._prompts)
        providers = len(self._by_provider)
        models = sum(len(v) for v in self._by_model.values())
        total_bytes = sum(p.size_bytes for p in self._prompts.values())

        per_provider = {}
        for prov, prompts in self._by_provider.items():
            per_provider[prov] = {
                "count": len(prompts),
                "models": len(set(p.model for p in prompts)),
                "size_bytes": sum(p.size_bytes for p in prompts),
            }

        return {
            "total": total,
            "providers": providers,
            "models": models,
            "total_size_bytes": total_bytes,
            "by_provider": per_provider,
        }

    def load_prompt(self, path: str) -> Optional[str]:
        """Convenience: get the content of a prompt by path, or ``None``."""
        prompt = self.get(path)
        if prompt is not None:
            return prompt.load()
        return None

    # ── Internals ──────────────────────────────────────────────────────────

    def _ensure_scanned(self) -> None:
        if not self._scanned:
            self._scan()

    def _scan(self) -> None:
        self._prompts = {}
        self._by_provider = {}
        self._by_model = {}
        self._tags_index = {}

        if not self._base_dir.is_dir():
            return

        for provider_dir, provider_name in _PROVIDER_DIR_MAP.items():
            provider_path = self._base_dir / provider_dir
            if not provider_path.is_dir():
                continue

            md_files = sorted(provider_path.rglob("*.md"))
            prompts_for_provider: List[SystemPrompt] = []

            for md_path in md_files:
                # Ignore README files
                if md_path.name.upper() == "README.MD":
                    continue

                model_name = _derive_model_name(md_path, provider_name)
                tags = _derive_tags(md_path, provider_name)
                abs_path = str(md_path.resolve())

                prompt = SystemPrompt(
                    provider=provider_name,
                    model=model_name,
                    file_path=abs_path,
                    tags=tags,
                )
                self._prompts[abs_path] = prompt
                prompts_for_provider.append(prompt)

                # Model index (many-to-many is fine)
                self._by_model.setdefault(model_name, []).append(prompt)

                # Tags index
                for t in tags:
                    self._tags_index.setdefault(t, []).append(prompt)

            self._by_provider[provider_name] = prompts_for_provider

        # Also catch top-level directories not in the explicit map
        for child in sorted(self._base_dir.iterdir()):
            if child.is_dir() and child.name not in _PROVIDER_DIR_MAP:
                provider_name = child.name
                md_files = sorted(child.rglob("*.md"))
                prompts_for_provider = []
                for md_path in md_files:
                    if md_path.name.upper() == "README.MD":
                        continue
                    model_name = _derive_model_name(md_path, provider_name)
                    tags = _derive_tags(md_path, provider_name)
                    abs_path = str(md_path.resolve())
                    prompt = SystemPrompt(
                        provider=provider_name,
                        model=model_name,
                        file_path=abs_path,
                        tags=tags,
                    )
                    self._prompts[abs_path] = prompt
                    prompts_for_provider.append(prompt)
                    self._by_model.setdefault(model_name, []).append(prompt)
                    for t in tags:
                        self._tags_index.setdefault(t, []).append(prompt)
                if prompts_for_provider:
                    self._by_provider[provider_name] = prompts_for_provider

        self._scanned = True


# ──────────────────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────────────────

def _default_base_dir() -> str:
    """Return the directory where this __init__.py lives."""
    return str(Path(__file__).resolve().parent)


def _derive_model_name(path: Path, provider: str) -> str:
    """Derive a human-readable model name from a prompt file path."""
    stem = path.stem
    # Remove common prefixes for cleaner names
    name = stem.replace(f"{provider}-", "", 1) if stem.startswith(provider) else stem
    # Clean up
    name = name.replace("_", "-").replace(" ", "-")
    return name


def _derive_tags(path: Path, provider: str) -> List[str]:
    """Derive tags from the file path for categorisation."""
    tags: List[str] = [provider]
    parts = path.parts
    # Add parent directories as tags (for categorisation like "claude-code", "official")
    for i, part in enumerate(parts):
        if part.lower() in ("bundled-skills", "references", "examples", "scripts"):
            continue
        if part == provider or part.endswith(".md"):
            continue
        if part not in tags:
            tags.append(part.lower().replace(" ", "-").replace("_", "-"))

    # Add content-based tags
    stem_lower = path.stem.lower()
    if "claude" in stem_lower:
        tags.append("claude")
    if "gpt" in stem_lower or "chatgpt" in stem_lower:
        tags.append("gpt")
    if "gemini" in stem_lower:
        tags.append("gemini")
    if "grok" in stem_lower:
        tags.append("grok")
    if "code" in stem_lower or "codex" in stem_lower:
        tags.append("coding")
    if "safety" in stem_lower or "security" in stem_lower:
        tags.append("safety")
    if "api" in stem_lower:
        tags.append("api")
    if "thinking" in stem_lower:
        tags.append("thinking")
    if "personality" in stem_lower or stem_lower.startswith("personality"):
        tags.append("personality")
    if "offic" in stem_lower:
        tags.append("official")
    if "old" in str(path).lower():
        tags.append("archived")

    return list(set(tags))


# ──────────────────────────────────────────────────────────────────────────────
# Module-level convenience
# ──────────────────────────────────────────────────────────────────────────────

_LIBRARY: Optional[SystemPromptLibrary] = None


def get_library() -> SystemPromptLibrary:
    """Return the module-level singleton library."""
    global _LIBRARY
    if _LIBRARY is None:
        _LIBRARY = SystemPromptLibrary()
    return _LIBRARY


__all__ = [
    "SystemPrompt",
    "SystemPromptLibrary",
    "get_library",
]

