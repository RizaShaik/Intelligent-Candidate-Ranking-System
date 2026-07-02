from configs.weights import BEHAVIOR_WEIGHT


def behavior_score(candidate):

    s = candidate["redrob_signals"]

    score = 0

    if s["open_to_work_flag"]:
        score += 3

    score += min(s["recruiter_response_rate"] * 4, 4)

    score += min(s["interview_completion_rate"] * 3, 3)

    if s["notice_period_days"] <= 30:
        score += 2

    elif s["notice_period_days"] <= 60:
        score += 1

    if s["github_activity_score"] > 50:
        score += 2

    elif s["github_activity_score"] > 20:
        score += 1

    return min(score, BEHAVIOR_WEIGHT)