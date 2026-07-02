from ranking.scorer import *

from ranking.behavioral import *

from preprocessing.honeypot import *

from preprocessing.features import *def technical_score(candidate):

    score = 0

    score += experience_score(candidate)

    score += title_score(candidate)

    score += industry_score(candidate)

    score += retrieval_score(candidate)

    score += ranking_score(candidate)

    score += embedding_score(candidate)

    score += vector_score(candidate)

    score += evaluation_score(candidate)

    return score

def hiring_score(candidate):

    return behavioral_score(candidate)

def penalty(candidate):

    p = 0

    p += honeypot_penalty(candidate)

    return p

def final_score(candidate):

    score = technical_score(candidate)

    score += hiring_score(candidate)

    score -= penalty(candidate)

    return round(score, 3)

