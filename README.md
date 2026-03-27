# Data Science Chatbot (Vector-based AI)

A **Vector-based Question Answering Chatbot** specialized in **Data Science** topics.

This chatbot supports both **Arabic** and **English** queries and returns answers using semantic similarity powered by **NLP vector embeddings**.

**This is Version 1 (V1)** of the project.
Future versions are under development with more advanced AI capabilities and improved datasets.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [File &amp; Folder Structure](#file--folder-structure)
- [Workflow](#workflow)
- [Technologies Used](#technologies-used)
- [Dataset](#dataset)
- [Future Improvements (Upcoming Versions)](#future-improvements-upcoming-versions)
- [Team](#team)
- [License](#license)
- [Requirements](#requirements)

---

## Project Overview

This project is a **Vector-Based Question Answering System** designed to help students learn **Data Science concepts interactively**.

The chatbot works offline by converting questions into **vector embeddings** and comparing them using **cosine similarity** to retrieve the closest answer.

The system automatically detects whether the user writes in:

- Arabic
- English

and responds in the same language.

**Goal:**
Provide a lightweight educational AI assistant for beginners in Data Science.

---

## Features

- Arabic & English language support
- Automatic language detection
- Vector similarity search
- Offline semantic matching
- NLP embeddings using Sentence Transformers
- Web chat interface (Flask)
- Precomputed embeddings for fast responses
- Friendly fallback message for unknown questions

---

## File & Folder Structure

DataScience_Chatbot/

├── data/

│   ├── qa_data.json        # Questions & Answers dataset

│   └── all_questions.json  # Full list of 148 Arabic & English questions

├── static/

│   ├── style.css

│   └── script.js

├── templates/

│   └── index.html

├── bot.py

├── build_vectors.py

├── vector_db.pkl

├── app.py

├── README.md

└── requirements.txt

### File & Folder Goals

| File / Folder               | Purpose                                                                 |
| --------------------------- | ----------------------------------------------------------------------- |
| `data/qa_data.json`       | Knowledge base containing chatbot questions and answers.                |
| `data/all_questions.json` | Complete list of 148 bilingual questions for expansion and suggestions. |
| `bot.py`                  | Core chatbot logic: language detection and similarity matching.         |
| `build_vectors.py`        | Generates vector embeddings offline from the dataset.                   |
| `vector_db.pkl`           | Stores precomputed embeddings for fast response retrieval.              |
| `app.py`                  | Flask backend server connecting frontend with chatbot logic.            |
| `templates/index.html`    | Main HTML structure of the chat interface.                              |
| `static/style.css`        | Controls UI design, layout, and visual styling.                         |
| `static/script.js`        | Handles frontend behavior and API communication.                        |

---

## Workflow

### 1. Offline Step — Embedding Generation

Run:

```bash
python build_vectors.py
```

This will:

* Encode all dataset questions
* Generate vector embeddings
* Save them inside `vector_db.pkl`

### 2. Online Step — Running Chatbot

Run:

```bash
python app.py
```

Then open:

`http://127.0.0.1:5000/`

### System Flow

User → Frontend (script.js) → Flask (app.py) → bot.py → vector_db.pkl → Best Answer → User

---

## Technologies Used

| Technology            | Version  | Purpose               |
| --------------------- | -------- | --------------------- |
| Python                | 3.x      | Main backend language |
| Flask                 | 2.3.3    | Web server            |
| sentence-transformers | 2.2.2    | Text embeddings       |
| numpy                 | 1.25.2   | Vector math           |
| pickle                | Built-in | Save embeddings       |
| langdetect            | 1.0.9    | Language detection    |
| HTML/CSS/JS           | —       | Frontend interface    |

---

## Dataset

The chatbot uses two datasets:

### 1. QA Dataset

Contains questions and answers used directly by the chatbot.

`data/qa_data.json`

### 2. Questions Dataset

Contains **148 Arabic and English questions** used for:

* Suggested prompts
* Dataset expansion
* Future training improvements

`data/all_questions.json`

---

## Future Improvements (Upcoming Versions)

Planned for Version 2 & beyond:

* Smart question suggestions
* Improved semantic ranking
* Larger dataset coverage
* Context-aware conversations
* UI redesign
* Model fine-tuning
* API integration
* Deployment online

---

## Team

| Name                     | Role        | Id University |
| ------------------------ | ----------- | ------------- |
| Yousef Mohamed El-Sayed  | Team Leader | 4241151       |
| Abdelrahman Talaat Emad  | Member      | 4241143       |
| Menna Adel Mahmoud       | Member      | 4241433       |
| Ola Asad Anwer           | Member      | 4241332       |
| Shahd Mohamed El-Sayed   | Member      | 4241414       |
| Nasser Mahmoud Aboulnaga | Member      | 4241235       |
| Mohamed Gamal            | Member      | 4241557       |
| Aseel Madhat El-Sayed    | Member      | 4241270       |
| Enjy Mohamed Abdelbaset  | Member      | 4241088       |
| Yasser El-Sayed Saber    | Member      | 4231080       |

---

## License

This project is open-source and intended for  **educational purposes only** .

---

## Requirements

    `Flask==2.3.3 `

    `sentence-transformers==2.2.2 `

    `numpy==1.25.2 `

    `langdetect==1.0.9`

Install dependencies:

    `pip install -r requirements.txt`
