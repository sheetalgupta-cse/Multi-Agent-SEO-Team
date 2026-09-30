from tools.scraper import scrape_website


def technical_agent(website: str):

    data = scrape_website(website)

    issues = []

    if not data["title"]:
        issues.append({
            "issue": "Missing page title",
            "priority": "high"
        })

    if not data["meta_description"]:
        issues.append({
            "issue": "Missing meta description",
            "priority": "high"
        })

    h1_count = len([
        h for h in data["headings"]
        if h.lower().startswith("h1:")
    ])

    if not data["headings"]:
        issues.append({
            "issue": "No heading structure detected",
            "priority": "medium"
        })

    if data["images_without_alt"]:
        issues.append({
            "issue": (
                f"{len(data['images_without_alt'])} "
                "images missing ALT text"
            ),
            "priority": "medium"
        })

    score = max(
        100 - len(issues) * 10,
        0
    )

    return {
        "technical_score": score,
        "issues": issues,
        "page_title": data["title"],
        "meta_description": data["meta_description"]
    }