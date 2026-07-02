from docx import Document
import re

REQUIRED_SKILLS = {
    "python",
    "embeddings",
    "retrieval",
    "ranking",
    "vector database",
    "hybrid search",
    "pinecone",
    "weaviate",
    "qdrant",
    "milvus",
    "faiss",
    "ndcg",
    "mrr",
    "map",
    "evaluation"
}

RETRIEVAL_SKILLS = {
    "retrieval",
    "semantic search",
    "hybrid search",
    "vector search",
    "embeddings",
    "faiss",
    "pinecone",
    "weaviate",
    "qdrant",
    "milvus"
}

RANKING_SKILLS = {
    "ranking",
    "recommendation",
    "learning to rank",
    "ltr",
    "reranking",
    "re-ranking",
    "ndcg",
    "mrr",
    "map"
}


def normalize(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9 ]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text


def parse_job_description(docx_path):

    document = Document(docx_path)

    text = "\n".join(
        p.text for p in document.paragraphs
    )

    text = normalize(text)

    required = {
        s for s in REQUIRED_SKILLS
        if s in text
    }

    retrieval = {
        s for s in RETRIEVAL_SKILLS
        if s in text
    }

    ranking = {
        s for s in RANKING_SKILLS
        if s in text
    }

    return {

        "required_skills": required,

        "retrieval_skills": retrieval,

        "ranking_skills": ranking,

        "text": text
    }