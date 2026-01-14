import sqlite3
from typing import List, Dict
from datetime import datetime

DB_NAME = "research_pipeline.db"

def create_tables():
    """Create tables for papers and insights if they don't exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Table for papers
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS papers (
            arxiv_id TEXT PRIMARY KEY,
            title TEXT,
            authors TEXT,
            abstract TEXT,
            published TEXT,
            link TEXT,
            fetched_at TEXT
        )
    """)

    # Table for insights
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS insights (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            arxiv_id TEXT,
            keywords TEXT,
            bullet_summary TEXT,
            FOREIGN KEY(arxiv_id) REFERENCES papers(arxiv_id)
        )
    """)

    conn.commit()
    conn.close()

def insert_papers(papers: List[Dict]):
    """Insert papers into the database (ignore duplicates)."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    for paper in papers:
        cursor.execute("""
            INSERT OR IGNORE INTO papers 
            (arxiv_id, title, authors, abstract, published, link, fetched_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            paper["arxiv_id"],
            paper["title"],
            ", ".join(paper["authors"]),
            paper["abstract"],
            paper["published"],
            paper["link"],
            datetime.now().isoformat()
        ))

    conn.commit()
    conn.close()

def insert_insights(insights: List[Dict]):
    """Insert insights for papers."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    for insight in insights:
        cursor.execute("""
            INSERT INTO insights 
            (arxiv_id, keywords, bullet_summary)
            VALUES (?, ?, ?)
        """, (
            insight["arxiv_id"],
            ", ".join(insight.get("keywords", [])),
            " ".join(insight.get("bullets", []))
        ))

    conn.commit()
    conn.close()
