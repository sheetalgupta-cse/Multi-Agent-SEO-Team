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


def evaluate_recommendations(
    website: str,
    opportunities: list
):

    llm = get_llm(temperature=0)

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """
You are an SEO Quality Control Agent.

Evaluate SEO recommendations based on:

1. Relevance
2. Evidence
3. Actionability
4. Priority

Only validate useful recommendations.

Return ONLY valid JSON.
Do not use markdown.
"""
        ),
        (
            "human",
            """
Website:
{website}

Recommendations:
{opportunities}

Return exactly:

{{
    "validated": [
        {{
            "recommendation": "Recommendation",
            "confidence": 0,
            "status": "validated",
            "reason": "Why this recommendation is useful"
        }}
    ]
}}

Confidence must be a number between 0 and 100.
"""
        )
    ])

    result = (prompt | llm).invoke({
        "website": website,
        "opportunities": json.dumps(opportunities)
    })

    try:
        return parse_json_response(result.content)
    except Exception as e:
        print("Evaluator JSON error:", e)
        print("Raw response:", result.content)
        return {"validated": []}