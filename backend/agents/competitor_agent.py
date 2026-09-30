from langchain_core.prompts import ChatPromptTemplate
from agents.gemini import get_llm
from tools.search import web_search
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


def competitor_agent(website: str, goal: str):

    llm = get_llm(temperature=0.2)

    search_results = web_search(
        f"competitors of {website}",
        5
    )

    competitor_data = [
        {
            "title": item.get("title", ""),
            "url": item.get("url", ""),
            "content": item.get("content", "")
        }
        for item in search_results
    ]

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """
You are an expert SEO competitor analyst.

Analyze the provided competitor search results.

Identify:
- competitors
- competitor SEO gaps
- content gaps
- opportunities
- priority

Return ONLY valid JSON.
Do not use markdown.
"""
        ),
        (
            "human",
            """
Website:
{website}

Goal:
{goal}

Competitor search results:
{competitors}

Return exactly:

{{
    "competitor_gaps": [
        {{
            "competitor": "Competitor name",
            "gap": "SEO gap identified",
            "opportunity": "Opportunity for target website",
            "priority": "high/medium/low"
        }}
    ]
}}

Generate useful competitor opportunities from the available evidence.
"""
        )
    ])

    result = (prompt | llm).invoke({
        "website": website,
        "goal": goal,
        "competitors": json.dumps(competitor_data)
    })

    try:
        return parse_json_response(result.content)
    except Exception as e:
        print("Competitor Agent JSON error:", e)
        print("Raw response:", result.content)
        return {"competitor_gaps": []}