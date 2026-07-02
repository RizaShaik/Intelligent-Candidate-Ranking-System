# AI_Architects – Intelligent Candidate Ranking System

> Submission for **India Runs Hackathon by Redrob AI**

## Overview

This project presents an explainable candidate ranking system designed to intelligently match candidates to a given Job Description (JD). Rather than relying solely on keyword matching, the system evaluates candidates across multiple dimensions including semantic relevance, technical skills, experience, behavioral signals, education, and professional background.

The solution produces a ranked list of the Top 100 candidates along with concise, explainable reasoning for each recommendation, enabling recruiters to make faster and more informed hiring decisions.

---

## Problem Statement

Recruiters often receive hundreds or thousands of applications for a single role. Traditional Applicant Tracking Systems (ATS) primarily depend on keyword matching, which may overlook highly relevant candidates or rank less suitable profiles higher.

Our goal is to build an intelligent ranking system that:

- Understands the Job Description
- Evaluates candidate relevance using multiple signals
- Produces an explainable ranking
- Generates a submission in the required competition format

---

## Solution Highlights

- Semantic Job Description matching using **TF-IDF**
- Multi-factor weighted scoring
- Skill proficiency and experience evaluation
- Behavioral signal analysis
- Education-based scoring
- Product company bonus and service company penalty
- Explainable ranking reasons
- Official submission CSV generation
- Deterministic and reproducible results

---

## System Workflow

```
Job Description
       │
       ▼
JD Parsing
       │
       ▼
Candidate Feature Extraction
       │
       ▼
TF-IDF Similarity
       │
       ▼
Weighted Scoring Engine
       │
       ▼
Candidate Ranking
       │
       ▼
Reason Generation
       │
       ▼
submission.csv
```

---

## Candidate Evaluation

The final ranking score combines multiple candidate signals.

### Skills

- Required skill overlap
- Skill proficiency
- Skill experience
- Skill endorsements

### Experience

- Years of professional experience
- Preferred experience range
- Seniority adjustments

### Behavioral Signals

- Open-to-work status
- Recruiter response rate
- Interview completion rate
- GitHub activity
- Assessment scores
- Profile completeness
- Search appearances
- Professional connections
- Offer acceptance rate
- Email & phone verification
- LinkedIn connectivity

### Professional Background

- Product company experience bonus
- Service company penalty

### Semantic Matching

- TF-IDF Vectorization
- Cosine Similarity

### Additional Factors

- Retrieval skill overlap
- Ranking skill overlap
- Domain keyword bonus
- Notice period

---

## Explainable AI

For every ranked candidate, the system generates a concise explanation describing the major factors contributing to the ranking.

Example:

```
7.2 years experience;
skills: Pinecone, Milvus, Weaviate, Embeddings, RAG;
open to work;
good recruiter response;
excellent interview attendance;
active GitHub profile;
short notice period
```

---

## Project Structure

```
Candidate-Ranking-System/
│
├── configs/
│   └── weights.py
│
├── preprocessing/
│   ├── features.py
│   ├── jd_parser.py
│   └── loader.py
│
├── ranking/
│   ├── scorer.py
│   ├── tfidf_similarity.py
│   └── rank_candidates.py
│
├── reasoning/
│   └── generator.py
│
├── utils/
│  
│
├── outputs/
│   └── submission.csv
│   └── submission.xlsx
│
├── data/
│
├── rank.py
├── validate_submission.py
├── requirements.txt
└── README.md
```

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity
- JSON
- CSV

---

## Installation

Clone the repository:

```bash
git clone [https://github.com/RizaShaik/AI-Candidate-Ranking-System](https://github.com/RizaShaik/Intelligent-Candidate-Ranking-System)
```

Navigate to the project directory:

```bash
cd Candidate-Ranking-System
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Project

Generate the ranked candidate list:

```bash
python rank.py
```

Validate the generated submission:

```bash
python validate_submission.py outputs/submission.csv
```

---

## Output

The system generates a competition-ready CSV containing:

- Candidate ID
- Rank
- Final Score
- Explainable Reasoning

Example:

| Candidate ID | Rank | Score |
|--------------|------|-------|
| CAND_0018499 | 1 | 534.15 |

---

## Performance

- Multi-factor candidate evaluation
- Explainable recommendations
- Lightweight and fast execution
- Deterministic ranking
- Scalable for large candidate datasets
- Official submission validation compliant

---

## Future Enhancements

- Sentence Transformer embeddings
- Learning-to-Rank models
- Graph-based candidate similarity
- Dynamic score optimization
- LLM-powered reasoning generation
- Recruiter feedback learning

---

## Team

**Team Name:** AI_Architects

Developed for the **India Runs Hackathon by Redrob AI**.

---

## License

This project is shared for educational and hackathon demonstration purposes.
