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


def generate_action_plan(
    website: str,
    validated_recommendations: dict
):

    llm = get_llm(temperature=0.2)

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """
You are an SEO Strategy Manager.

Convert validated SEO recommendations into
a practical prioritized implementation plan.

Consider:
- SEO impact
- priority
- effort
- business value

Return ONLY valid JSON.
Do not use markdown.
"""
        ),
        (
            "human",
            """
Website:
{website}

Validated recommendations:
{recommendations}

Return exactly:

{{
    "action_plan": [
        {{
            "priority": "high/medium/low",
            "action": "Specific SEO action",
            "reason": "Why this should be done",
            "effort": "low/medium/high"
        }}
    ]
}}

Generate a practical prioritized action plan.
"""
        )
    ])

    result = (prompt | llm).invoke({
        "website": website,
        "recommendations": json.dumps(validated_recommendations)
    })

    try:
        return parse_json_response(result.content)
    except Exception as e:
        print("Action Plan JSON error:", e)
        print("Raw response:", result.content)
        return {"action_plan": []}