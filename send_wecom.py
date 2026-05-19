import re
from datetime import datetime
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


def _clean_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    return text


def collect_public_web(source: dict, timeout=20):
    """Collect text from a public website URL. This is MVP extraction, not a perfect crawler."""
    url = source.get("URL / Query") or source.get("URL")
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; MarketDynamicsAgent/0.1; public-source-monitor)"
    }
    response = requests.get(url, headers=headers, timeout=timeout)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "lxml")

    for tag in soup(["script", "style", "noscript", "svg", "form", "nav", "footer"]):
        tag.decompose()

    title = _clean_text(soup.title.get_text(" ")) if soup.title else source.get("Source Name", "Untitled")

    # MVP: collect page text. Later can add article-list extraction per source.
    candidates = soup.find_all(["article", "main"])
    if candidates:
        raw_text = "\n".join(_clean_text(c.get_text(" ")) for c in candidates)
    else:
        raw_text = _clean_text(soup.get_text(" "))

    if len(raw_text) > 12000:
        raw_text = raw_text[:12000]

    return [{
        "title": title,
        "published_date": "",
        "url": url,
        "raw_text": raw_text,
        "image_url": "",
        "access_status": "Accessible"
    }]
