from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def compute_similarity(jd_text, candidate_text):

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    matrix = vectorizer.fit_transform(
        [jd_text, candidate_text]
    )

    return cosine_similarity(
        matrix[0:1],
        matrix[1:2]
    )[0][0]