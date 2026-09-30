def detect_opportunities(
    keyword_data,
    competitor_data,
    technical_data,
    content_data
):

    opportunities = []

    for item in keyword_data.get("keywords", []):
        if item.get("priority") == "high":
            opportunities.append({
                "type": "keyword_gap",
                "title": item.get("keyword"),
                "reason": item.get("reason"),
                "priority": "high"
            })

    for item in competitor_data.get("competitor_gaps", []):
        opportunities.append({
            "type": "competitor_gap",
            "title": item.get("gap"),
            "reason": item.get("opportunity"),
            "priority": item.get("priority", "medium")
        })

    for item in technical_data.get("issues", []):
        opportunities.append({
            "type": "technical",
            "title": item.get("issue"),
            "reason": "Technical SEO improvement opportunity",
            "priority": item.get("priority", "medium")
        })

    for item in content_data.get(
        "content_opportunities",
        []
    ):
        opportunities.append({
            "type": "content_gap",
            "title": item.get("topic"),
            "reason": item.get("suggested_title"),
            "priority": item.get("priority", "medium")
        })

    return opportunities