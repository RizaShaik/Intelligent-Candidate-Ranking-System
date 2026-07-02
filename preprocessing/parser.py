from dataclasses import dataclass


@dataclass
class Candidate:

    id: str

    profile: dict

    career: list

    education: list

    skills: list

    signals: dict

def parse_candidate(raw):

    return Candidate(

        id=raw["candidate_id"],

        profile=raw["profile"],

        career=raw["career_history"],

        education=raw["education"],

        skills=raw["skills"],

        signals=raw["redrob_signals"]
    )