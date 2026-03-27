# This script defines the chatbot logic:
# - Detects input language (Arabic/English)
# - Validates the user's question
# - Encodes the question into a vector
# - Finds the most similar question from the dataset using cosine similarity
# - Returns the corresponding answer or a fallback message if unknown
import pickle
import numpy as np
import re
from sentence_transformers import SentenceTransformer
from langdetect import detect, LangDetectException


model = SentenceTransformer(
    "sentence-transformers/paraphrase-MiniLM-L3-v2"
)


with open("vector_db.pkl", "rb") as f:
    embeddings, mapping, questions = pickle.load(f)


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def detect_language(text):
    try:
        lang = detect(text)
        return "ar" if lang == "ar" else "en"
    except LangDetectException:
        
        if re.search(r'[\u0600-\u06FF]', text):
            return "ar"
        return "en"


def invalid_message(lang):
    return (
        "من فضلك اكتب سؤال واضح."
        if lang == "ar"
        else "Please write a clear question."
    )

def unknown_answer_message(lang):
    return (
        "عذراً، لا أملك معلومات كافية للإجابة على هذا السؤال."
        if lang == "ar"
        else "Sorry, I don't have enough information to answer that question."
    )


def is_valid_text(text):
    text = text.strip()
    if len(text) < 3:
        return False
    words = text.split()
    if len(words) < 2:
        return False
    if not re.search(r"[a-zA-Z\u0600-\u06FF]", text):
        return False
    return True


def get_response(user_input):

    
    lang = detect_language(user_input)

    
    if not is_valid_text(user_input):
        return invalid_message(lang)

    
    user_vector = model.encode([user_input])[0]

    
    scores = [cosine_similarity(user_vector, emb) for emb in embeddings]

    best_index = np.argmax(scores)
    best_score = scores[best_index]

    
    THRESHOLD = 0.50  

    if best_score < THRESHOLD:
        return unknown_answer_message(lang)

    
    best_match = mapping[best_index]

    return best_match["answer_ar"] if lang == "ar" else best_match["answer_en"]