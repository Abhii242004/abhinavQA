Autonomous QA Agent – End-to-End Test Case Generator

This project is an AI-powered Autonomous QA Agent that takes product documentation (HTML, Markdown, UI/UX notes, etc.) and automatically:

✅ Builds a knowledge base
✅ Generates high-quality test cases
✅ Generates Python Selenium scripts
✅ Helps QA teams validate discount flows, checkout flows, UX rules, and functional behavior

It uses:

1) FastAPI backend (RAG, vector DB, LLM pipelines)

2) Streamlit frontend (user interface)

3) ChromaDB for semantic search

4) Python Selenium script generation

abhinavqa/
│
├── backend/
│   ├── api/
│   │   └── app.py
│   ├── ingestion/
│   ├── agents/
│   └── utils/
│
├── frontend/
│   └── streamlit_app.py
│
├── assets/
│   ├── checkout.html
│   ├── product_specs.md
│   └── ui_ux_guide.txt
│
├── requirements.txt
└── README.md

⚙️ Setup Instructions
1. Python Version
Python 3.10 or 3.11

2. Create Virtual Environment

Windows:

python -m venv venv
venv\Scripts\activate


Linux / macOS:

python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
pip install --upgrade pip
pip install -r requirements.txt


requirements.txt should include:

fastapi
uvicorn[standard]
streamlit
requests
chromadb
sentence-transformers
beautifulsoup4
unstructured
pymupdf
python-multipart
selenium
jinja2

🚀 How to Run the Application

The system has two components: FastAPI backend and Streamlit frontend.

1️⃣ Run FastAPI Backend
uvicorn backend.api.app:app --host 127.0.0.1 --port 8000 --reload


Open API docs:

http://127.0.0.1:8000/docs

2️⃣ Run Streamlit Frontend
streamlit run frontend/streamlit_app.py


Open UI at:

http://localhost:8501

🧠 How It Works
Step 1 — Upload Documents

Users upload:

checkout.html

product_specs.md

ui_ux_guide.txt

The backend extracts text, chunks it, generates embeddings, and stores everything inside ChromaDB.

Step 2 — Generate Test Cases

User enters a prompt like:

Generate test cases for discount code validation.


The backend uses RAG + LLM to produce:

Positive test cases

Negative validations

Boundary conditions

Business rule test coverage

Output is structured in:

JSON

Markdown table

Step 3 — Generate Selenium Scripts

User selects a generated test case and pastes it into the Streamlit text box.

Example input:

{
  "id": "TC-03",
  "scenario": "Apply expired discount code",
  "steps": [
    "Open checkout page",
    "Enter expired code SAVE2020",
    "Click Apply",
    "Verify error message"
  ]
}


Backend returns a ready-to-run Selenium script:

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("file:///path/to/checkout.html")
...
driver.quit()

📚 Included Support Documents
checkout.html

A sample e-commerce checkout page containing:

Add to cart buttons

Discount field

User details form

Shipping methods

Payment methods

Pay Now button
Used for DOM mapping during Selenium script generation.

product_specs.md

Contains:

Discount rules

Shipping rules

Validation constraints

Business logic
Referenced during test case generation.

ui_ux_guide.txt

Describes:

Error message formatting

Button styling rules

UX constraints
Used to enhance negative + UX test cases.

🧪 Usage Example

Upload all documents

Click Build Knowledge Base

Enter prompt:

Generate test cases for SAVE15 discount code.


Copy one test case

Paste into Selenium Script Generator

Receive executable Python Selenium script

🛠️ Troubleshooting

KeyError: 'script'

Happens if backend returns an error

Ensure backend is running on port 8000

Ensure test case JSON is valid
