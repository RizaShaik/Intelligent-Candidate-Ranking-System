from configs.weights import SKILL_WEIGHT
from ranking.jd_rules import RETRIEVAL_KEYWORDS
from ranking.jd_rules import LLM_KEYWORDS


def skill_score(candidate):

    score = 0

    text = ""

    for s in candidate["skills"]:
        text += " " + s["name"].lower()

    for job in candidate["career_history"]:
        text += " " + job["description"].lower()

    # Retrieval signals
    retrieval_hits = 0

    for word in RETRIEVAL_KEYWORDS:

        if word in text:
            retrieval_hits += 1

    # LLM signals
    llm_hits = 0

    for word in LLM_KEYWORDS:

        if word in text:
            llm_hits += 1

    score += min(retrieval_hits * 2.8, 15)

    score += min(llm_hits * 1.3, 6)

    # Production bonus
    production_words = [

        "production",

        "deployed",

        "real users",

        "scale",

        "pipeline",

        "latency",

        "evaluation",

        "ndcg",

        "mrr",

        "ab testing",

        "offline",

        "online"

    ]

    prod = 0

    for p in production_words:

        if p in text:
            prod += 1

    score += min(prod, 6)

    return min(score, SKILL_WEIGHT)