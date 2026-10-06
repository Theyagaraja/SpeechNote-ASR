"""Small deterministic text-processing utilities."""

from __future__ import annotations

import re
from collections import Counter

STOP_WORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from",
    "has", "have", "how", "i", "in", "is", "it", "of", "on", "or",
    "that", "the", "this", "to", "was", "we", "were", "what", "when",
    "where", "which", "who", "with", "you", "your", "our", "their",
    "they", "he", "she", "but", "not", "can", "will", "would", "could",
    "should", "do", "does", "did", "than", "then", "there", "these",
    "those", "into", "about", "also", "so", "if", "because", "its",
}


def normalize_text(text: str) -> str:
    """Normalize whitespace without changing the user's wording."""
    return re.sub(r"\s+", " ", text).strip()


def word_count(text: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", text, flags=re.UNICODE))


def sentence_count(text: str) -> int:
    if not text.strip():
        return 0
    sentences = re.findall(r"[^.!?]+[.!?]+|[^.!?]+$", text.strip())
    return len([s for s in sentences if s.strip()])


def extract_keywords(text: str, limit: int = 8) -> list[str]:
    """Return frequent content words using a deterministic frequency method."""
    words = re.findall(r"\b[a-zA-Z][a-zA-Z'-]{2,}\b", text.lower())
    meaningful = [w for w in words if w not in STOP_WORDS]
    counts = Counter(meaningful)
    return [word for word, _ in counts.most_common(limit)]


def summarize_statistics(text: str) -> dict[str, int]:
    return {
        "words": word_count(text),
        "sentences": sentence_count(text),
        "characters": len(text),
    }
