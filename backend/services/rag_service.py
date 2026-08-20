"""Grounded RAG service for RRR.

This service deliberately answers only from indexed local knowledge. It does not
invent component specifications or repair facts when evidence is missing.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Iterable


KNOWLEDGE_ROOT = Path(__file__).resolve().parents[2] / "knowledge"

@dataclass(frozen=True)
class SourceChunk:
    source: str
    page: str
    text: str


def _chunks(text: str, source: str, page: str = "") -> Iterable[SourceChunk]:
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    for paragraph in paragraphs:
        words = paragraph.split()
        for i in range(0, len(words), 180):
            chunk = " ".join(words[i:i + 180])
            if chunk:
                yield SourceChunk(source, page, chunk)


def load_knowledge() -> list[SourceChunk]:
    chunks: list[SourceChunk] = []
    if not KNOWLEDGE_ROOT.exists():
        return chunks
    for path in KNOWLEDGE_ROOT.rglob("*"):
        if path.suffix.lower() in {".txt", ".md"}:
            chunks.extend(_chunks(path.read_text(encoding="utf-8"), path.name))
    return chunks


def _tokens(value: str) -> set[str]:
    return {x for x in re.findall(r"[a-z0-9][a-z0-9._/-]*", value.lower()) if len(x) > 1}


def retrieve(query: str, limit: int = 5) -> list[dict]:
    query_tokens = _tokens(query)
    scored: list[tuple[float, SourceChunk]] = []
    for chunk in load_knowledge():
        tokens = _tokens(chunk.text)
        overlap = len(query_tokens & tokens)
        if overlap:
            score = overlap / max(1, len(query_tokens))
            scored.append((score, chunk))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [
        {"score": round(score, 4), "source": c.source, "page": c.page, "text": c.text}
        for score, c in scored[:limit]
    ]


def answer(query: str, limit: int = 5) -> dict:
    sources = retrieve(query, limit)
    if not sources:
        return {
            "answer": "I cannot answer this reliably from the RRR knowledge base yet. Please provide the relevant manufacturer manual or datasheet.",
            "grounded": False,
            "sources": [],
        }
    evidence = "\n\n".join(f"[{i+1}] {s['text']}" for i, s in enumerate(sources))
    return {
        "answer": "Retrieved evidence is available. The generation layer must use only this evidence and cite the numbered sources.",
        "grounded": True,
        "evidence": evidence,
        "sources": sources,
    }
