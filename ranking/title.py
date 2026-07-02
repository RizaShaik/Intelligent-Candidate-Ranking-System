from configs.weights import TITLE_WEIGHT
from ranking.jd_rules import TARGET_TITLES


def title_score(candidate):

    title = candidate["profile"]["current_title"].lower()

    score = 0

    # Exact match
    for target in TARGET_TITLES:

        if target in title:
            return TITLE_WEIGHT

    # Partial engineering titles
    if "engineer" in title:
        score += 12

    if "scientist" in title:
        score += 10

    if "developer" in title:
        score += 8

    if "architect" in title:
        score += 6

    return min(score, TITLE_WEIGHT)