def impossible_experience(candidate):

    total = sum(

        job["duration_months"]

        for job in candidate.career

    ) / 12

    profile = candidate.profile["years_of_experience"]

    if total - profile > 2:

        return True

    return False

def impossible_skills(candidate):

    exp_months = (

        candidate.profile["years_of_experience"]

        * 12

    )

    for skill in candidate.skills:

        duration = skill.get(

            "duration_months",

            0

        )

        if duration > exp_months + 24:

            return True

    return False

def expert_skill_count(candidate):

    return sum(

        1

        for s in candidate.skills

        if s["proficiency"] == "expert"

    )

def fake_expert(candidate):

    for skill in candidate.skills:

        if (

            skill["proficiency"] == "expert"

            and

            skill.get("duration_months", 0) < 6

        ):

            return True

    return False

def honeypot_penalty(candidate):

    penalty = 0

    if impossible_experience(candidate):
        penalty += 20

    if impossible_skills(candidate):
        penalty += 20

    if fake_expert(candidate):
        penalty += 15

    if expert_skill_count(candidate) > 10:
        penalty += 10

    return penalty

