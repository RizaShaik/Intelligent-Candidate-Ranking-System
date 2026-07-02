from configs.weights import HONEYPOT_PENALTY


def honeypot_penalty(candidate):

    years = candidate["profile"]["years_of_experience"]

    penalty = 0

    # Impossible skill duration

    for skill in candidate["skills"]:

        duration_years = skill.get("duration_months", 0) / 12

        if duration_years > years + 1:
            penalty += 25

    # Too many expert skills

    expert = sum(
        1
        for s in candidate["skills"]
        if s["proficiency"] == "expert"
    )

    if expert >= 10:
        penalty += 30

    # Impossible career duration

    total = sum(
        job["duration_months"]
        for job in candidate["career_history"]
    ) / 12

    if total > years + 2:
        penalty += 30

    if penalty > 50:
        return HONEYPOT_PENALTY

    return -penalty