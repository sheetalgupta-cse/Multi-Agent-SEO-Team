def audit_agent(
    website_data: dict
):

    issues = []

    strengths = []

    # --------------------------------
    # Get website information
    # --------------------------------

    title = website_data.get(
        "title",
        ""
    )

    description = website_data.get(
        "description",
        ""
    )

    headings = website_data.get(
        "headings",
        []
    )

    images = website_data.get(
        "images",
        []
    )

    links = website_data.get(
        "links",
        []
    )

    word_count = website_data.get(
        "word_count",
        0
    )

    status_code = website_data.get(
        "status_code",
        200
    )

    # --------------------------------
    # TITLE CHECK
    # --------------------------------

    if not title:

        issues.append({

            "issue": "Missing title tag",

            "severity": "Critical",

            "pages_or_items": "Homepage",

            "recommendation": (
                "Add a unique and descriptive "
                "title containing the primary "
                "target keyword."
            )
        })

    elif len(title) < 30:

        issues.append({

            "issue": "Title tag is too short",

            "severity": "Medium",

            "pages_or_items": "Homepage",

            "recommendation": (
                "Create a more descriptive title "
                "that communicates the page topic "
                "and target keyword."
            )
        })

    elif len(title) > 60:

        issues.append({

            "issue": "Title tag may be too long",

            "severity": "Low",

            "pages_or_items": "Homepage",

            "recommendation": (
                "Consider shortening the title "
                "to improve search-result readability."
            )
        })

    else:

        strengths.append(
            "Homepage has a properly sized title tag."
        )

    # --------------------------------
    # META DESCRIPTION CHECK
    # --------------------------------

    if not description:

        issues.append({

            "issue": "Missing meta description",

            "severity": "High",

            "pages_or_items": "Homepage",

            "recommendation": (
                "Add a compelling meta description "
                "that summarizes the page and "
                "encourages users to click."
            )
        })

    elif len(description) < 70:

        issues.append({

            "issue": "Meta description is short",

            "severity": "Medium",

            "pages_or_items": "Homepage",

            "recommendation": (
                "Expand the meta description with "
                "relevant keywords and a clear value proposition."
            )
        })

    elif len(description) > 160:

        issues.append({

            "issue": "Meta description may be too long",

            "severity": "Low",

            "pages_or_items": "Homepage",

            "recommendation": (
                "Shorten the meta description so "
                "the key message is visible in search results."
            )
        })

    else:

        strengths.append(
            "Homepage has a usable meta description."
        )

    # --------------------------------
    # H1 CHECK
    # --------------------------------

    if not headings:

        issues.append({

            "issue": "No headings detected",

            "severity": "High",

            "pages_or_items": "Homepage",

            "recommendation": (
                "Add a clear H1 heading describing "
                "the main purpose of the page."
            )
        })

    else:

        # Check whether an H1 is represented
        # in scraper output.

        h1_found = False

        for heading in headings:

            if isinstance(heading, dict):

                tag = str(
                    heading.get("tag", "")
                ).lower()

                if tag == "h1":
                    h1_found = True

            elif str(heading).lower().startswith(
                "h1"
            ):

                h1_found = True

        if h1_found:

            strengths.append(
                "H1 heading detected on the website."
            )

        else:

            issues.append({

                "issue": "H1 heading not detected",

                "severity": "High",

                "pages_or_items": "Homepage",

                "recommendation": (
                    "Add one clear H1 containing "
                    "the main page topic."
                )
            })

    # --------------------------------
    # IMAGE CHECK
    # --------------------------------

    if isinstance(images, list) and images:

        missing_alt = 0

        for image in images:

            if isinstance(image, dict):

                alt = image.get(
                    "alt",
                    ""
                )

                if not alt:
                    missing_alt += 1

        if missing_alt > 0:

            issues.append({

                "issue": "Images missing alt text",

                "severity": "Medium",

                "pages_or_items": (
                    f"{missing_alt} image(s)"
                ),

                "recommendation": (
                    "Add descriptive and relevant "
                    "alt text to important images."
                )
            })

        else:

            strengths.append(
                "Images have alt text available."
            )

    # --------------------------------
    # CONTENT CHECK
    # --------------------------------

    if isinstance(word_count, int):

        if word_count < 300:

            issues.append({

                "issue": "Low page content volume",

                "severity": "Medium",

                "pages_or_items": "Homepage",

                "recommendation": (
                    "Expand useful, user-focused content "
                    "to better address search intent."
                )
            })

        else:

            strengths.append(
                "Website contains a reasonable amount "
                "of textual content."
            )

    # --------------------------------
    # STATUS CODE CHECK
    # --------------------------------

    if status_code not in [
        200,
        None
    ]:

        issues.append({

            "issue": "Website returned an unexpected status code",

            "severity": "Critical",

            "pages_or_items": "Homepage",

            "recommendation": (
                "Verify server availability and "
                "ensure the homepage returns HTTP 200."
            )
        })

    # --------------------------------
    # SEO SCORE
    # --------------------------------

    score = 100

    for issue in issues:

        severity = issue.get(
            "severity",
            "Low"
        )

        if severity == "Critical":
            score -= 20

        elif severity == "High":
            score -= 15

        elif severity == "Medium":
            score -= 8

        elif severity == "Low":
            score -= 3

    score = max(
        0,
        min(100, score)
    )

    # --------------------------------
    # SUMMARY
    # --------------------------------

    if score >= 80:

        summary = (
            "The website has a strong technical "
            "SEO foundation with some opportunities "
            "for further optimization."
        )

    elif score >= 60:

        summary = (
            "The website has a moderate SEO foundation "
            "but several improvements could increase "
            "search visibility."
        )

    else:

        summary = (
            "The website has significant SEO issues "
            "that should be prioritized before scaling "
            "organic growth."
        )

    # --------------------------------
    # FINAL RESULT
    # --------------------------------

    return {

        "score": score,

        "issues": issues,

        "strengths": strengths,

        "summary": summary
    }