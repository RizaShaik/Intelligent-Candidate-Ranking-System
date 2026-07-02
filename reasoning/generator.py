from preprocessing.features import (
    years_of_experience,
    candidate_skill_set,
    github_score,
    recruiter_response,
    interview_completion,
    open_to_work,
    notice_period
)


def generate_reason(candidate, score):

    reasons = []

    # Experience
    exp = years_of_experience(candidate)

    if exp >= 5:
        reasons.append(f"{exp:.1f} years experience")

    # Skills
    skills = candidate_skill_set(candidate)

    important = []

    KEY = [
        "python",
        "retrieval",
        "ranking",
        "faiss",
        "pinecone",
        "milvus",
        "qdrant",
        "weaviate",
        "embeddings",
        "semantic search",
        "recommendation",
        "llm",
        "rag"
    ]

    for k in KEY:

        if k in skills:

            important.append(k)

    if important:

        reasons.append(
            "skills: " + ", ".join(important[:5])
        )

    # Behaviour

    if open_to_work(candidate):

        reasons.append("open to work")

    if recruiter_response(candidate) >= 0.5:

        reasons.append("good recruiter response")

    if interview_completion(candidate) >= 0.8:

        reasons.append("excellent interview attendance")

    if github_score(candidate) > 60:

        reasons.append("active GitHub profile")

    notice = notice_period(candidate)

    if notice <= 30:

        reasons.append("short notice period")

    if len(reasons) == 0:

        reasons.append("general profile match")

    return "; ".join(reasons)