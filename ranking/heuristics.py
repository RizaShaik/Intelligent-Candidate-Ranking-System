def get_all_text(candidate):

    pieces = []

    profile = candidate["profile"]

    pieces.append(profile["headline"])
    pieces.append(profile["summary"])
    pieces.append(profile["current_title"])

    for job in candidate["career_history"]:
        pieces.append(job["description"])
        pieces.append(job["title"])

    for skill in candidate["skills"]:
        pieces.append(skill["name"])

    return " ".join(pieces).lower()

from ranking.heuristics import get_all_text

PRODUCTION_TERMS = [
    "production",
    "deployed",
    "real users",
    "serving",
    "pipeline",
    "latency",
    "scalable",
    "distributed",
    "deployment",
]


def production_bonus(candidate):

    text = get_all_text(candidate)

    score = 0

    for word in PRODUCTION_TERMS:
        if word in text:
            score += 1.5

    return min(score, 8)

from ranking.heuristics import get_all_text

RETRIEVAL_TERMS = [

    "retrieval",

    "ranking",

    "recommendation",

    "search",

    "matching",

    "hybrid search",

    "dense retrieval",

    "semantic search",

    "bm25",

    "faiss",

    "milvus",

    "pinecone",

    "weaviate",

    "qdrant",

    "elasticsearch",

]


def retrieval_bonus(candidate):

    text = get_all_text(candidate)

    score = 0

    for word in RETRIEVAL_TERMS:

        if word in text:
            score += 2

    return min(score, 10)

from ranking.heuristics import get_all_text

EVAL_TERMS = [

    "ndcg",

    "mrr",

    "map",

    "offline evaluation",

    "online evaluation",

    "a/b",

    "ab test",

    "precision",

    "recall",

]


def evaluation_bonus(candidate):

    text = get_all_text(candidate)

    score = 0

    for word in EVAL_TERMS:

        if word in text:

            score += 2

    return min(score, 6)

from ranking.heuristics import get_all_text

CV_TERMS = [

    "image classification",

    "segmentation",

    "object detection",

    "opencv",

    "yolo",

    "mask rcnn",

    "vision transformer",

]


def cv_penalty(candidate):

    text = get_all_text(candidate)

    hits = 0

    for word in CV_TERMS:

        if word in text:
            hits += 1

    if hits >= 4:
        return -12

    return 0

from ranking.heuristics import get_all_text


def research_penalty(candidate):

    text = get_all_text(candidate)

    if "phd" in text and "production" not in text:
        return -8

    if "research assistant" in text and "deployed" not in text:
        return -8

    return 0

def title_churn_penalty(candidate):

    history = candidate["career_history"]

    if len(history) < 3:
        return 0

    short_jobs = 0

    for job in history:

        if job["duration_months"] < 18:
            short_jobs += 1

    if short_jobs >= 3:
        return -6

    return 0

