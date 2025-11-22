🤖 Autonomous QA Agent: Full-Stack RAG & Automation Service

This project comprises a FastAPI backend (the RAG and generation engine) and a Streamlit frontend (the user interface) designed to streamline Quality Assurance (QA) and test automation using Generative AI.

🌟 Architecture Overview

The system follows a three-step flow:

1) Ingestion (FastAPI): User documentation and HTML are ingested into a local ChromaDB vector store.

2) Test Case Generation (FastAPI + LLM): A user query triggers a RAG retrieval, and the Gemini model generates a structured, step-by-step JSON test case.

3) Script Generation (FastAPI + LLM): The structured JSON is converted into a runnable Python Selenium script, leveraging Google Search grounding for up-to-date best practices (e.g., using webdriver_manager).

🛠️ Setup and Prerequisites

To run both the frontend and backend, you need a shared environment.

Prerequisites

Python 3.10+ (Recommended)

Gemini API Key: Required for all generative tasks. This must be set as an environment variable (__api_key).

Web Driver: A compatible web browser (like Chrome) and its corresponding WebDriver executable (e.g., chromedriver) installed for running the generated Selenium scripts. The generated scripts often use webdriver_manager to handle this automatically, but local installation is recommended for stability.

Installation

Since the backend and frontend use separate dependency lists (app_requirements.txt and requirements.txt), it's easiest to install all packages in one environment.

Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Linux/macOS
venv\Scripts\activate     # On Windows


Install all dependencies:

pip install fastapi uvicorn pydantic beautifulsoup4 lxml requests chromadb sentence-transformers streamlit


Set Environment Variable (Crucial):
Before running, set your Gemini API Key. Replace YOUR_GEMINI_API_KEY with your actual key.

# For Linux/macOS
export __api_key="YOUR_GEMINI_API_KEY"

# For Windows (Command Prompt)
set __api_key="YOUR_GEMINI_API_KEY"


⚙️ Running the Applications

Start the Backend (FastAPI Service)

The backend handles the RAG database, knowledge retrieval, and AI generation logic.

uvicorn app:app --reload --host 0.0.0.0 --port 8000


The service will start at http://0.0.0.0:8000.

Start the Frontend (Streamlit UI)

The frontend is a lightweight UI that interacts with the running FastAPI backend.

streamlit run app_streamlit.py


The Streamlit app will typically open in your browser at http://localhost:8501.

🧪 Usage Examples

The entire process is managed through the Streamlit UI, calling the FastAPI endpoints internally.

Step 1: Build Knowledge Base

Action: In the Streamlit UI, upload the application's documentation (.txt, .md) and its raw HTML file (e.g., checkout.html).

Goal: Click "🚀 Build Knowledge Base". The Streamlit app calls the FastAPI endpoint /upload_docs to ingest the content into ChromaDB.

Result: The RAG system is now contextually aware of your application's fields, error messages, and business logic.

Step 2: Generate Structured Test Cases

Action: Enter a query describing the test, like: "Generate a test case for logging in with an empty password and a valid email."

Goal: Click "✨ Generate Test Cases". The Streamlit app calls /generate_test_cases, which uses RAG to retrieve context and the LLM to generate a JSON output conforming to the GeneratedTestCase schema.

Result: A clean, structured JSON test case is displayed, ready for automation.

Step 3: Generate Selenium Script

Action: Copy the JSON from Step 2 into the designated text area.

Goal: Click "🐍 Generate Selenium Script". The Streamlit app sends the JSON to the /generate_selenium endpoint. The LLM converts the structured steps into runnable Python code.

Result: A complete Python script using Selenium and best practices (like webdriver_manager and explicit waits) is provided, ready to be executed.

📝 Included Support Documents

While not explicitly provided in the file list, the backend is designed to accept two types of support documents for ingestion:

Document Type

Purpose

How it's Used

Documentation Text (.md, .txt)

Provides detailed business logic, API specifications, and functional requirements.

Used by RAG to ensure the generated Test Cases align with documented system behavior.

HTML Content

Provides the actual structure of the web page (CSS selectors, element IDs, button names, form fields).

Used by RAG to provide specific, concrete details for the element_identifier and expected_result fields in the generated Test Cases and the final Selenium Scripts.
