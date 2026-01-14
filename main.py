from fetchers.arxiv import fetch_arxiv
from processing.clean import clean_papers
from insights.summarize import extract_keywords, top_authors, generate_bullets
from storage.database import create_tables, insert_papers, insert_insights

if __name__ == "__main__":
    topic = "nickel oxide formation energy"

    # Step 0: Create tables
    create_tables()

    # Step 1: Fetch & clean papers
    results = fetch_arxiv(query=topic, max_results=10)
    cleaned = clean_papers(results)
    insert_papers(cleaned)

    # Step 2: Generate insights
    keywords = extract_keywords(cleaned, top_n=10)
    bullets = generate_bullets(cleaned, max_bullets=5)

    # Prepare insight entries
    insights = []
    for paper in cleaned:
        insights.append({
            "arxiv_id": paper["arxiv_id"],
            "keywords": keywords,
            "bullets": bullets
        })

    insert_insights(insights)

    print("✅ Papers and insights stored in SQLite successfully!")
