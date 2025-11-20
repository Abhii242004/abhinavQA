from fastapi import FastAPI
from pydantic import BaseModel
from backend.ingestion.document_ingestor import DocumentIngestor
from backend.ingestion.vector_store import VectorStore
from backend.agents.test_case_agent import TestCaseAgent
from backend.agents.selenium_agent import SeleniumScriptAgent

app = FastAPI()
vector_store = VectorStore()
ingestor = DocumentIngestor(vector_store)
test_case_agent = TestCaseAgent(vector_store)
selenium_agent = SeleniumScriptAgent(vector_store)

class UploadRequest(BaseModel):
    docs: list[str]
    html: str

class QueryRequest(BaseModel):
    query: str

class TestCaseRequest(BaseModel):
    test_case: dict

@app.post("/upload_docs")
def upload_docs(payload: UploadRequest):
    ingestor.process_documents(payload.docs, payload.html)
    return {"status": "Knowledge Base Built"}

@app.post("/generate_test_cases")
def generate_test_cases(payload: QueryRequest):
    return test_case_agent.generate_cases(payload.query)

@app.post("/generate_selenium")
def generate_selenium(payload: TestCaseRequest):
    return {"script": selenium_agent.generate_script(payload.test_case)}