from bs4 import BeautifulSoup
import fitz
import json
from backend.ingestion.vector_store import VectorStore

class DocumentIngestor:
    def __init__(self, vector_store: VectorStore):
        self.db = vector_store

    def load_text(self, path, content=None):
        ext = path.split(".")[-1]
        if ext in ["md", "txt"]:
            return content
        if ext == "html":
            return BeautifulSoup(content, "html.parser").get_text()
        if ext == "json":
            return json.dumps(json.loads(content))
        if ext == "pdf":
            doc = fitz.open(stream=content, filetype="pdf")
            return "\n".join([page.get_text() for page in doc])
        return ""

    def process_documents(self, docs, html):
        all_texts = []
        for idx, doc in enumerate(docs):
            text = self.load_text(f"doc_{idx}.txt", doc)
            all_texts.append(text)
        html_text = self.load_text("checkout.html", html)
        all_texts.append(html_text)
        self.db.add_texts(all_texts, [{"source": f"doc_{i}"} for i in range(len(all_texts))])
