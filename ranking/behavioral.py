from datetime import datetime

TODAY = datetime(2026, 7, 1)

def days_since_active(candidate):

    last = datetime.strptime(
        candidate.signals["last_active_date"],
        "%Y-%m-%d"
    )

    return (TODAY - last).days

def open_to_work(candidate):

    return 8 if candidate.signals["open_to_work_flag"] else 0

def recruiter_response(candidate):

    rate = candidate.signals["recruiter_response_rate"]

    if rate >= 0.9:
        return 10

    if rate >= 0.75:
        return 8

    if rate >= 0.5:
        return 5

    if rate >= 0.3:
        return 2

    return -5

def notice_score(candidate):

    notice = candidate.signals["notice_period_days"]

    if notice <= 30:
        return 5

    if notice <= 60:
        return 3

    if notice <= 90:
        return 0

    return -4

def github_score(candidate):

    score = candidate.signals["github_activity_score"]

    if score == -1:
        return 0

    return score / 20

def interview_score(candidate):

    return (
        candidate.signals["interview_completion_rate"]
        * 5
    )

def recruiter_interest(candidate):

    saved = candidate.signals["saved_by_recruiters_30d"]

    appearance = candidate.signals["search_appearance_30d"]

    score = 0

    score += min(saved, 10)

    score += min(appearance / 100, 5)

    return score

def activity_score(candidate):

    days = days_since_active(candidate)

    if days <= 7:
        return 5

    if days <= 30:
        return 3

    if days <= 90:
        return 1

    return -5

def behavioral_score(candidate):

    score = 0

    score += open_to_work(candidate)

    score += recruiter_response(candidate)

    score += notice_score(candidate)

    score += github_score(candidate)

    score += interview_score(candidate)

    score += recruiter_interest(candidate)

    score += activity_score(candidate)

    return score

