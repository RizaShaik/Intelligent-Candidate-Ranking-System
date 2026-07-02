from configs.weights import PRODUCT_WEIGHT
from configs.weights import CONSULTING_PENALTY

from ranking.jd_rules import GOOD_COMPANIES
from ranking.jd_rules import CONSULTING


def company_score(candidate):

    history = candidate["career_history"]

    score = 0

    product_found = False
    consulting_count = 0

    for job in history:

        company = job["company"].lower()

        for good in GOOD_COMPANIES:

            if good in company:
                product_found = True

        for bad in CONSULTING:

            if bad in company:
                consulting_count += 1

    if product_found:
        score += PRODUCT_WEIGHT

    if consulting_count == len(history):
        score += CONSULTING_PENALTY

    return score