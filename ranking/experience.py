from configs.weights import EXPERIENCE_WEIGHT


def experience_score(candidate):

    years = candidate["profile"]["years_of_experience"]

    score = 0

    # JD prefers roughly 5–9 years.
    if 5 <= years <= 9:
        score = EXPERIENCE_WEIGHT

    elif 4 <= years < 5:
        score = EXPERIENCE_WEIGHT * 0.85

    elif 9 < years <= 12:
        score = EXPERIENCE_WEIGHT * 0.75

    elif 3 <= years < 4:
        score = EXPERIENCE_WEIGHT * 0.60

    else:
        score = EXPERIENCE_WEIGHT * 0.20

    return score