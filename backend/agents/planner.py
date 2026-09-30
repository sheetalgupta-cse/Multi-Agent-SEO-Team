from langchain_core.prompts import ChatPromptTemplate
from agents.gemini import get_llm
import json


def create_seo_plan(website: str, goal: str):

    llm = get_llm(temperature=0)

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            """
You are an AI SEO Manager.

Your job is to create an SEO analysis plan.

Available agents:
- keyword
- competitor
- technical
- content

Decide which tasks are required.

Return ONLY valid JSON.
"""
        ),
        (
            "human",
            """
Website: {website}

SEO Goal: {goal}

Return:

{{
    "tasks": [
        {{
            "agent": "keyword",
            "task": "..."
        }}
    ]
}}
"""
        )
    ])

    result = (prompt | llm).invoke({
        "website": website,
        "goal": goal
    })

    try:
        return json.loads(result.content)
    except Exception:
        return {
            "tasks": [
                {
                    "agent": "keyword",
                    "task": "Perform keyword research"
                },
                {
                    "agent": "competitor",
                    "task": "Analyze competitors"
                },
                {
                    "agent": "technical",
                    "task": "Perform technical SEO audit"
                },
                {
                    "agent": "content",
                    "task": "Find content opportunities"
                }
            ]
        }