import feedparser
from datetime import datetime
from typing import List, Dict


def fetch_arxiv(
    query: str,
    max_results: int = 10,
    start: int = 0,
    sort_by: str = "submittedDate",
    sort_order: str = "descending"
) -> List[Dict]:
    """
    Fetch papers from arXiv based on a search query.
    """

    base_url = "http://export.arxiv.org/api/query?"
    search_query = f"search_query=all:{query.replace(' ', '+')}"
    params = (
        f"{search_query}&start={start}&max_results={max_results}"
        f"&sortBy={sort_by}&sortOrder={sort_order}"
    )

    feed = feedparser.parse(base_url + params)

    papers = []
    for entry in feed.entries:
        paper = {
            "arxiv_id": entry.id.split("/abs/")[-1],
            "title": entry.title.replace("\n", " ").strip(),
            "authors": [author.name for author in entry.authors],
            "abstract": entry.summary.replace("\n", " ").strip(),
            "published": datetime(*entry.published_parsed[:6]).isoformat(),
            "link": entry.link,
        }
        papers.append(paper)

    return papers
