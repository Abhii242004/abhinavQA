import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_or_create_collection("knowledge_base")
embedder = SentenceTransformer("all-MiniLM-L6-v2")

class VectorStore:
    def add_texts(self, texts, metadatas):
        vectors = [embedder.encode(t).tolist() for t in texts]
        ids = [f"id_{i}" for i in range(len(texts))]
        collection.add(documents=texts, embeddings=vectors, ids=ids, metadatas=metadatas)

    def similarity_search(self, query, k=5):
        v = embedder.encode(query).tolist()
        results = collection.query(query_embeddings=[v], n_results=k)
        return [{"page_content": d} for d in results["documents"][0]]