import os
import requests


def web_search(query: str, max_results: int = 5):
    api_key = os.getenv("TAVILY_API_KEY")

    if not api_key:
        return []

    response = requests.post(
        "https://api.tavily.com/search",
        json={
            "api_key": api_key,
            "query": query,
            "search_depth": "basic",
            "max_results": max_results
        },
        timeout=20
    )

    response.raise_for_status()

    data = response.json()

    return data.get("results", [])