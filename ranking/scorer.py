from preprocessing.features import (
    candidate_skill_set,
    years_of_experience,
    get_candidate_text,
    notice_period,

    profile_completeness,
    search_appearance,
    connections,
    endorsements,
    offer_acceptance,
    verified_email,
    verified_phone,
    linkedin,

    github_score,
    recruiter_response,
    interview_completion,
    saved_by_recruiters,
    open_to_work,
    assessment_average,
)

from ranking.tfidf_similarity import compute_similarity


# -----------------------------
# Experience
# -----------------------------

def experience_score(exp):

    # Ideal range
    if 5 <= exp <= 8:
        return 100

    # Still good
    elif 8 < exp <= 10:
        return 90

    # Slightly senior
    elif 10 < exp <= 12:
        return 75

    # Noticeable penalty
    elif 12 < exp <= 15:
        return 55

    # Very senior
    elif exp > 15:
        return 35

    # Junior
    elif 3 <= exp < 5:
        return 65

    return 25


# -----------------------------
# Skill Score
# -----------------------------

PROFICIENCY_SCORE = {
    "beginner": 1,
    "intermediate": 2,
    "advanced": 3,
    "expert": 4
}


def skill_score(candidate, jd):

    score = 0

    jdskills = jd["required_skills"]

    for skill in candidate["skills"]:

        name = skill["name"].lower()

        if name not in jdskills:
            continue

        score += 12

        score += PROFICIENCY_SCORE.get(
            skill["proficiency"],
            1
        ) * 2

        score += min(
            skill["duration_months"],
            60
        ) * 0.08

        score += min(
            skill["endorsements"],
            50
        ) * 0.05

    return score


# -----------------------------
# Education
# -----------------------------

TIER = {
    "tier_1": 10,
    "tier_2": 7,
    "tier_3": 5,
    "tier_4": 3,
    "unknown": 2
}


def education_score(candidate):

    if not candidate["education"]:
        return 0

    return TIER.get(
        candidate["education"][0]["tier"],
        2
    )


# -----------------------------
# Behaviour
# -----------------------------

def behavior_score(candidate):

    score = 0

    if open_to_work(candidate):
        score += 15

    score += recruiter_response(candidate) * 25

    score += interview_completion(candidate) * 20

    score += min(saved_by_recruiters(candidate), 20)

    g = github_score(candidate)

    if g > 0:
        score += g * 0.20

    score += assessment_average(candidate) * 0.10

    score += profile_completeness(candidate) * 0.10

    score += min(search_appearance(candidate), 300) * 0.03

    score += min(connections(candidate), 500) * 0.02

    score += min(endorsements(candidate), 100) * 0.05

    offer = offer_acceptance(candidate)

    if offer > 0:
        score += offer * 8

    if verified_email(candidate):
        score += 2

    if verified_phone(candidate):
        score += 2

    if linkedin(candidate):
        score += 2

    return score


# -----------------------------
# Companies
# -----------------------------

PRODUCT_COMPANIES = {
    "google",
    "amazon",
    "meta",
    "microsoft",
    "apple",
    "netflix",
    "linkedin",
    "uber",
    "airbnb",
    "atlassian",
    "razorpay",
    "swiggy",
    "zomato",
    "flipkart"
}


def product_bonus(candidate):

    score = 0

    for job in candidate["career_history"]:

        company = job["company"].lower()

        if any(p in company for p in PRODUCT_COMPANIES):
            score += 20

    exp = years_of_experience(candidate)

    if exp > 15:
        score *= 0.6

    elif exp > 12:
        score *= 0.8

    return score


SERVICE_COMPANIES = {
    "infosys",
    "tcs",
    "wipro",
    "mindtree",
    "cognizant",
    "accenture",
    "capgemini",
    "tech mahindra",
    "hcl"
}


def service_penalty(candidate):

    jobs = candidate["career_history"]

    if not jobs:
        return 0

    count = 0

    for job in jobs:

        company = job["company"].lower()

        if any(s in company for s in SERVICE_COMPANIES):
            count += 1

    if count == len(jobs):
        return -30

    return 0


# -----------------------------
# Main Score
# -----------------------------

def compute_score(candidate, jd):

    score = 0

    exp = years_of_experience(candidate)

    score += experience_score(exp)

    if exp > 15:
        score -= 25

    elif exp > 12:
        score -= 10

    score += skill_score(
        candidate,
        jd
    )

    score += education_score(candidate)

    score += behavior_score(candidate)

    score += product_bonus(candidate)

    score += service_penalty(candidate)

    similarity = compute_similarity(
        jd["text"],
        get_candidate_text(candidate)
    )

    score += similarity * 40

    skills = candidate_skill_set(candidate)

    score += len(
        skills &
        jd["retrieval_skills"]
    ) * 10

    score += len(
        skills &
        jd["ranking_skills"]
    ) * 12

    KEYWORDS = [
        "retrieval",
        "ranking",
        "recommendation",
        "semantic search",
        "hybrid search",
        "vector search",
        "embeddings",
        "faiss",
        "pinecone",
        "weaviate",
        "milvus",
        "qdrant",
        "ndcg",
        "mrr",
        "evaluation"
    ]

    text = get_candidate_text(candidate)

    hits = 0

    for word in KEYWORDS:
        if word in text:
            hits += 1

    hits = min(hits, 6)

    score += hits * 4

    notice = notice_period(candidate)

    if notice <= 30:
        score += 10
    elif notice <= 60:
        score += 5
    else:
        score -= 5

    return round(score, 2)