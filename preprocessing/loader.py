import json


def load_candidates(file_path):
    """
    Loads all candidate records from a JSONL file.
    Returns a list of candidate dictionaries.
    """

    candidates = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if line:
                candidates.append(json.loads(line))

    print(f"Loaded {len(candidates)} candidates.")

    return candidates