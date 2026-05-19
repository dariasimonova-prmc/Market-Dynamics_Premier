import feedparser


def collect_rss(source: dict):
    url = source.get("URL / Query") or source.get("URL")
    feed = feedparser.parse(url)
    items = []
    for e in feed.entries[:20]:
        items.append({
            "title": getattr(e, "title", ""),
            "published_date": getattr(e, "published", ""),
            "url": getattr(e, "link", url),
            "raw_text": getattr(e, "summary", ""),
            "image_url": "",
            "access_status": "Accessible"
        })
    return items
