import re


def get_candidate_text(candidate):
    """
    Convert an entire candidate profile into one searchable text string.
    """

    parts = []

    profile = candidate["profile"]

    parts.extend([
        profile.get("headline", ""),
        profile.get("summary", ""),
        profile.get("current_title", ""),
        profile.get("current_company", ""),
        profile.get("current_industry", "")
    ])

    for job in candidate.get("career_history", []):
        parts.extend([
            job.get("company", ""),
            job.get("title", ""),
            job.get("industry", ""),
            job.get("description", "")
        ])

    for skill in candidate.get("skills", []):
        parts.append(skill.get("name", ""))

    text = " ".join(parts)

    text = text.lower()

    text = re.sub(r"[^a-z0-9 ]", " ", text)

    text = re.sub(r"\s+", " ", text)

    return text


def candidate_skill_set(candidate):
    """
    Return all candidate skills in lowercase.
    """

    skills = set()

    for skill in candidate.get("skills", []):

        skills.add(skill["name"].lower())

    return skills


def years_of_experience(candidate):

    return candidate["profile"].get(
        "years_of_experience",
        0
    )


def github_score(candidate):

    return candidate["redrob_signals"].get(
        "github_activity_score",
        -1
    )


def recruiter_response(candidate):

    return candidate["redrob_signals"].get(
        "recruiter_response_rate",
        0
    )


def interview_completion(candidate):

    return candidate["redrob_signals"].get(
        "interview_completion_rate",
        0
    )


def saved_by_recruiters(candidate):

    return candidate["redrob_signals"].get(
        "saved_by_recruiters_30d",
        0
    )


def open_to_work(candidate):

    return candidate["redrob_signals"].get(
        "open_to_work_flag",
        False
    )


def notice_period(candidate):

    return candidate["redrob_signals"].get(
        "notice_period_days",
        180
    )


def assessment_average(candidate):

    scores = candidate["redrob_signals"].get(
        "skill_assessment_scores",
        {}
    )

    if len(scores) == 0:
        return 0

    return sum(scores.values()) / len(scores)

def profile_completeness(candidate):
    return candidate["redrob_signals"]["profile_completeness_score"]


def search_appearance(candidate):
    return candidate["redrob_signals"]["search_appearance_30d"]


def connections(candidate):
    return candidate["redrob_signals"]["connection_count"]


def endorsements(candidate):
    return candidate["redrob_signals"]["endorsements_received"]


def offer_acceptance(candidate):
    return candidate["redrob_signals"]["offer_acceptance_rate"]


def verified_email(candidate):
    return candidate["redrob_signals"]["verified_email"]


def verified_phone(candidate):
    return candidate["redrob_signals"]["verified_phone"]


def linkedin(candidate):
    return candidate["redrob_signals"]["linkedin_connected"]