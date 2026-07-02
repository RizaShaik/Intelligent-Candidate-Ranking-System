from ranking.scorer import compute_score
from reasoning.generator import generate_reason


def rank_candidates(candidates, jd_features):

    ranked = []

    for candidate in candidates:

        score = compute_score(candidate, jd_features)

        reason = generate_reason(candidate, score)

        ranked.append({
            "candidate": candidate,
            "score": score,
            "reason": reason
        })

    ranked.sort(
        key=lambda x: (-x["score"], x["candidate"]["candidate_id"])
    )

    return ranked