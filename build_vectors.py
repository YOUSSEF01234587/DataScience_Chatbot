# This script encodes all questions into vectors using SentenceTransformer
# and saves the embeddings, original questions, and mapping into 'vector_db.pkl'.
import json
import pickle
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("sentence-transformers/paraphrase-MiniLM-L3-v2")

with open("data/qa_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

questions = []
mapping = []

for item in data:
    for q in item["question_ar"] + item["question_en"]:
        questions.append(q)
        mapping.append(item)

embeddings = model.encode(questions)

with open("vector_db.pkl", "wb") as f:
    pickle.dump((embeddings, mapping, questions), f)

print("Vector database created")