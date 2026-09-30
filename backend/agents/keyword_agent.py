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


def keyword_agent(website: str, goal: str):

    llm = get_llm(temperature=0.2)

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """
You are an expert SEO keyword research specialist.

Analyze the website and business goal.

Generate useful SEO keyword opportunities including:
- primary keywords
- long-tail keywords
- search intent
- priority
- reason

Return ONLY valid JSON.
Do not use markdown.
"""
        ),
        (
            "human",
            """
Website: {website}

Goal: {goal}

Return exactly this JSON structure:

{{
    "keywords": [
        {{
            "keyword": "example keyword",
            "intent": "informational/commercial/transactional/navigational",
            "priority": "high/medium/low",
            "reason": "Why this keyword is useful"
        }}
    ]
}}

Generate 8-12 realistic keyword opportunities.
"""
        )
    ])

    result = (prompt | llm).invoke({
        "website": website,
        "goal": goal
    })

    try:
        return parse_json_response(result.content)
    except Exception as e:
        print("Keyword Agent JSON error:", e)
        print("Raw response:", result.content)
        return {"keywords": []}