from typing import List, Dict


def clean_papers(papers: List[Dict]) -> List[Dict]:
    """
    Remove duplicate papers based on arXiv ID and do minor cleanup.
    """

    seen_ids = set()
    cleaned = []

    for paper in papers:
        arxiv_id = paper.get("arxiv_id")
        if not arxiv_id:
            continue  # skip if missing arxiv_id

        if arxiv_id in seen_ids:
            continue  # duplicate found

        # Minor cleanup
        paper["title"] = paper["title"].strip()
        paper["abstract"] = paper["abstract"].strip()
        paper["authors"] = [author.strip() for author in paper["authors"]]

        cleaned.append(paper)
        seen_ids.add(arxiv_id)

    return cleaned
