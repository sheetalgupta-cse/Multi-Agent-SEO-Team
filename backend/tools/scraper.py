import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def scrape_website(url: str):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(
        url,
        headers=headers,
        timeout=15
    )

    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.get_text(strip=True) if soup.title else ""

    meta_description = ""
    meta_tag = soup.find(
        "meta",
        attrs={"name": "description"}
    )

    if meta_tag:
        meta_description = meta_tag.get("content", "")

    headings = [
        h.get_text(" ", strip=True)
        for h in soup.find_all(["h1", "h2", "h3"])
    ]

    links = []

    for link in soup.find_all("a", href=True):
        links.append(
            urljoin(url, link["href"])
        )

    images = soup.find_all("img")

    images_without_alt = [
        img.get("src", "")
        for img in images
        if not img.get("alt")
    ]

    return {
        "url": url,
        "title": title,
        "meta_description": meta_description,
        "headings": headings,
        "links": links,
        "total_images": len(images),
        "images_without_alt": images_without_alt,
        "html_length": len(response.text)
    }