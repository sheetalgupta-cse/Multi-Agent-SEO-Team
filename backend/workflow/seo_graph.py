from typing import TypedDict
from concurrent.futures import ThreadPoolExecutor

from agents.planner import create_seo_plan
from agents.keyword_agent import keyword_agent
from agents.competitor_agent import competitor_agent
from agents.technical_agent import technical_agent
from agents.content_agent import content_agent
from agents.evaluator import evaluate_recommendations
from agents.action_plan import generate_action_plan

from services.opportunity import detect_opportunities


class SEOState(TypedDict, total=False):

    website: str
    goal: str

    plan: dict

    keywords: dict
    competitors: dict
    technical: dict
    content: dict

    opportunities: list
    evaluation: dict
    action_plan: dict


def run_seo_workflow(
    website: str,
    goal: str
):

    # FEATURE 1
    plan = create_seo_plan(
        website,
        goal
    )

    # FEATURE 2
    # Run core agents in parallel

    with ThreadPoolExecutor(
        max_workers=3
    ) as executor:

        keyword_future = executor.submit(
            keyword_agent,
            website,
            goal
        )

        competitor_future = executor.submit(
            competitor_agent,
            website,
            goal
        )

        technical_future = executor.submit(
            technical_agent,
            website
        )

        keywords = keyword_future.result()
        competitors = competitor_future.result()
        technical = technical_future.result()

    # Content agent uses previous results

    content = content_agent(
        website,
        keywords,
        competitors
    )

    # FEATURE 3

    opportunities = detect_opportunities(
        keywords,
        competitors,
        technical,
        content
    )

    # FEATURE 4

    evaluation = evaluate_recommendations(
        website,
        opportunities
    )

    # FEATURE 5

    action_plan = generate_action_plan(
        website,
        evaluation
    )

    return {
        "website": website,
        "goal": goal,
        "plan": plan,
        "keywords": keywords,
        "competitors": competitors,
        "technical": technical,
        "content": content,
        "opportunities": opportunities,
        "evaluation": evaluation,
        "action_plan": action_plan
    }