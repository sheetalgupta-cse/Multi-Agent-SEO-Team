from langchain_core.prompts import ChatPromptTemplate
from agents.gemini import get_llm
import json


def parse_json_response(content):
    if isinstance(content, list):
        text = ""
        for item in content:
            if isinstance(item, dict):
                text += item.get("text", "")
            else:
                text += str(item)
        content = text

    content = str(content).strip()

    if "```json" in content:
        content = content.replace("```json", "").replace("```", "").strip()
    elif "```" in content:
        content = content.replace("```", "").strip()

    start = content.find("{")
    end = content.rfind("}")

    if start != -1 and end != -1:
        content = content[start:end + 1]

    return json.loads(content)


def content_agent(
    website: str,
    keywords: dict,
    competitor_data: dict
):

    llm = get_llm(temperature=0.4)

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """
You are an expert SEO content strategist.

Use keyword opportunities and competitor gaps to create
practical content opportunities.

Return ONLY valid JSON.
Do not use markdown.
"""
        ),
        (
            "human",
            """
Website:
{website}

Keyword opportunities:
{keywords}

Competitor gaps:
{competitors}

Return exactly:

{{
    "content_opportunities": [
        {{
            "topic": "Content topic",
            "primary_keyword": "Target keyword",
            "suggested_title": "SEO optimized title",
            "search_intent": "informational/commercial/transactional",
            "priority": "high/medium/low"
        }}
    ]
}}

Generate 6-10 useful content opportunities.
"""
        )
    ])

    result = (prompt | llm).invoke({
        "website": website,
        "keywords": json.dumps(keywords),
        "competitors": json.dumps(competitor_data)
    })

    try:
        return parse_json_response(result.content)
    except Exception as e:
        print("Content Agent JSON error:", e)
        print("Raw response:", result.content)
        return {"content_opportunities": []}