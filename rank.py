import csv

from preprocessing.loader import load_candidates
from preprocessing.jd_parser import parse_job_description

from ranking.rank_candidates import rank_candidates


CANDIDATES = "data/candidates.jsonl"

JOB_DESCRIPTION = "data/job_description.docx"

OUTPUT = "outputs/submission.csv"


def main():

    print("Loading candidates...")

    candidates = load_candidates(CANDIDATES)

    print(len(candidates), "loaded")

    print("Parsing JD...")

    jd = parse_job_description(JOB_DESCRIPTION)

    print("Ranking candidates...")

    ranked = rank_candidates(candidates, jd)

    top100 = ranked[:100]

    with open(
        OUTPUT,
        "w",
        newline="",
        encoding="utf8"
    ) as f:

        writer = csv.writer(f)

        writer.writerow([
            "candidate_id",
            "rank",
            "score",
            "reasoning"
        ])

        rank = 1

        for row in top100:

            writer.writerow([

                row["candidate"]["candidate_id"],

                rank,

                row["score"],

                row["reason"]

            ])

            rank += 1

    print("Done.")


if __name__ == "__main__":
    main()