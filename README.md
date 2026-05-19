from .public_web import collect_public_web


def collect_weibo_public(source: dict):
    """Public Weibo URL feasibility connector. It logs failure if blocked."""
    return collect_public_web(source)
