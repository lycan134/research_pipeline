from typing import List, Dict
from collections import Counter
import re
from nltk.corpus import stopwords

STOPWORDS = set(stopwords.words("english"))

def extract_keywords(papers: List[Dict], top_n: int = 10) -> List[str]:
    """
    Extract top N frequent keywords from abstracts.
    """
    text = " ".join(paper["abstract"] for paper in papers)
    # Remove non-alphabetic characters
    words = re.findall(r'\b[a-zA-Z]{3,}\b', text.lower())
    # Remove stopwords
    words = [w for w in words if w not in STOPWORDS]
    counts = Counter(words)
    return [word for word, _ in counts.most_common(top_n)]

def top_authors(papers: List[Dict], top_n: int = 5) -> List[str]:
    """
    Count most frequent authors.
    """
    all_authors = []
    for paper in papers:
        all_authors.extend(paper["authors"])
    counts = Counter(all_authors)
    return [author for author, _ in counts.most_common(top_n)]

def generate_bullets(papers: List[Dict], max_bullets: int = 5) -> List[str]:
    """
    Generate simple bullets: first sentence from abstracts.
    """
    bullets = []
    for paper in papers[:max_bullets]:
        # Take first sentence of abstract
        first_sentence = paper["abstract"].split(".")[0].strip()
        bullets.append(f"- {first_sentence}.")
    return bullets
