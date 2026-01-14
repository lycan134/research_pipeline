# Automated Research & Insight Pipeline

A Python pipeline that automatically:

- Fetches research papers from arXiv  
- Cleans and deduplicates data  
- Extracts keywords, top authors, and bullet summaries  
- Stores results in SQLite for analysis

---

## Setup

```bash
git clone https://github.com/YOUR_USERNAME/research_pipeline.git
cd research_pipeline
python -m venv venv
# Activate venv:
# Windows (PowerShell)
venv\Scripts\Activate.ps1
# macOS/Linux
source venv/bin/activate
pip install -r requirements.txt
