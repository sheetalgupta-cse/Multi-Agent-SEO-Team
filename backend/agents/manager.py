from agents.keyword_agent import keyword_agent
from agents.competitor_agent import competitor_agent
from agents.audit_agent import audit_agent
from agents.content_agent import content_agent


def extract_business_context(website_data):
    """
    Extract basic business information without using an LLM.
    """

    title = website_data.get("title", "") or ""
    description = website_data.get("description", "") or ""
    headings = website_data.get("headings", []) or []

    text = f"{title} {description} {' '.join(headings)}".lower()

    business = title if title else "Business Website"

    services = []

    possible_services = [
        "marketing",
        "seo",
        "digital marketing",
        "web development",
        "software",
        "consulting",
        "education",
        "training",
        "real estate",
        "ecommerce",
        "restaurant",
        "healthcare",
        "finance",
        "technology",
        "agency",
    ]

    for service in possible_services:

        if service in text:
            services.append(service)

    if not services:
        services = ["General Business Services"]

    audience = "Potential customers searching online"

    location = ""

    # Try to identify common location names
    locations = [
        "lucknow",
        "delhi",
        "mumbai",
        "bangalore",
        "hyderabad",
        "noida",
        "gurgaon",
        "pune",
        "chennai",
        "kolkata",
        "india",
    ]

    for city in locations:

        if city in text:
            location = city.title()
            break

    return {
        "business": business,
        "services": services,
        "audience": audience,
        "location": location,
    }


def calculate_seo_score(audit_result):
    """
    Calculate a basic SEO score from technical audit results.
    """

    score = audit_result.get("score")

    if isinstance(score, (int, float)):
        return max(0, min(100, int(score)))

    issues = audit_result.get("issues", [])

    if not issues:
        return 85

    penalty = min(len(issues) * 5, 60)

    return max(40, 100 - penalty)


def build_opportunities(
    keyword_result,
    competitor_result,
    audit_result,
    content_result
):
    """
    Combine outputs from all specialized agents
    into business-focused opportunities.
    """

    opportunities = []

    # Keyword opportunities
    keywords = keyword_result.get("keywords", [])

    if keywords:
        opportunities.append({
            "title": "Target high-potential keywords",
            "reason": f"{len(keywords)} keyword opportunities were identified.",
            "impact": "High",
            "priority": 1
        })

    # Competitor opportunities
    competitors = competitor_result.get("competitors", [])

    if competitors:
        opportunities.append({
            "title": "Close competitor content gaps",
            "reason": "Competitor research identified opportunities for stronger content coverage.",
            "impact": "High",
            "priority": 2
        })

    # Technical audit
    issues = audit_result.get("issues", [])

    if issues:
        opportunities.append({
            "title": "Fix technical SEO issues",
            "reason": f"{len(issues)} technical SEO issues require attention.",
            "impact": "High",
            "priority": 3
        })

    # Content
    content_opportunities = content_result.get(
        "content_opportunities",
        []
    )

    if content_opportunities:
        opportunities.append({
            "title": "Build SEO-focused content",
            "reason": "New content opportunities were identified from keyword research.",
            "impact": "Medium",
            "priority": 4
        })

    return opportunities


def build_action_plan(
    audit_result,
    keyword_result,
    content_result
):
    """
    Generate a simple 30-day SEO action plan
    without using a paid AI API.
    """

    action_plan = []

    issues = audit_result.get("issues", [])

    # Week 1
    if issues:

        action_plan.append({
            "week": 1,
            "task": "Fix technical SEO issues",
            "description": "Resolve the most important website SEO problems identified during the audit.",
            "priority": "High"
        })

    else:

        action_plan.append({
            "week": 1,
            "task": "Complete technical SEO baseline",
            "description": "Verify titles, meta descriptions, headings, links and crawlability.",
            "priority": "High"
        })

    # Week 2
    keywords = keyword_result.get("keywords", [])

    action_plan.append({
        "week": 2,
        "task": "Target priority keywords",
        "description": f"Create or optimize pages around {len(keywords)} identified keyword opportunities.",
        "priority": "High"
    })

    # Week 3
    content_opportunities = content_result.get(
        "content_opportunities",
        []
    )

    action_plan.append({
        "week": 3,
        "task": "Publish SEO content",
        "description": f"Develop content around {len(content_opportunities)} identified content opportunities.",
        "priority": "Medium"
    })

    # Week 4
    action_plan.append({
        "week": 4,
        "task": "Measure and optimize",
        "description": "Review keyword rankings, organic traffic opportunities and content performance.",
        "priority": "Medium"
    })

    return action_plan


def seo_manager(
    website: str,
    business_goal: str
):

    # --------------------------------
    # STEP 1: Scrape Website
    # --------------------------------

    from tools.scraper import scrape_website

    website_data = scrape_website(website)

    # --------------------------------
    # STEP 2: Extract Business Context
    # --------------------------------

    context = extract_business_context(
        website_data
    )

    business = context["business"]
    location = context["location"]

    # --------------------------------
    # STEP 3: Delegate Tasks
    # --------------------------------

    keyword_result = keyword_agent(
        business,
        business_goal,
        location
    )

    competitor_result = competitor_agent(
        business,
        location
    )

    audit_result = audit_agent(
        website_data
    )

    content_result = content_agent(
        business,
        business_goal,
        keyword_result
    )

    # --------------------------------
    # STEP 4: Calculate SEO Score
    # --------------------------------

    seo_score = calculate_seo_score(
        audit_result
    )

    # --------------------------------
    # STEP 5: Identify Opportunities
    # --------------------------------

    opportunities = build_opportunities(
        keyword_result,
        competitor_result,
        audit_result,
        content_result
    )

    # --------------------------------
    # STEP 6: Build Action Plan
    # --------------------------------

    action_plan = build_action_plan(
        audit_result,
        keyword_result,
        content_result
    )

    # --------------------------------
    # STEP 7: Executive Summary
    # --------------------------------

    summary = (
        f"The AI SEO Team analyzed {website}. "
        f"The website received an SEO score of {seo_score}/100. "
        f"The analysis identified "
        f"{len(opportunities)} major SEO opportunities "
        f"with a focus on {business_goal.lower()}."
    )

    # --------------------------------
    # STEP 8: Final Strategy
    # --------------------------------

    strategy = {

        "seo_score": seo_score,

        "executive_summary": summary,

        "top_opportunities": opportunities,

        "action_plan": action_plan,

        "keyword_opportunities":
            keyword_result.get(
                "keywords",
                []
            ),

        "competitor_insights":
            competitor_result.get(
                "competitors",
                []
            ),

        "technical_issues":
            audit_result.get(
                "issues",
                []
            ),

        "content_opportunities":
            content_result.get(
                "content_opportunities",
                []
            ),

        "recommended_strategy": (
            "Prioritize technical SEO fixes first, "
            "then target high-value keywords, "
            "create content around identified opportunities, "
            "and continuously monitor competitor activity."
        )
    }

    # --------------------------------
    # FINAL REPORT
    # --------------------------------

    return {

        "website": website,

        "business_goal": business_goal,

        "context": context,

        "agents": {

            "keyword": keyword_result,

            "competitor": competitor_result,

            "audit": audit_result,

            "content": content_result,
        },

        "strategy": strategy
    }