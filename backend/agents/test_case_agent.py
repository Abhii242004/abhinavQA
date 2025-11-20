class TestCaseAgent:
    def __init__(self, vector_store):
        self.db = vector_store

    def generate_cases(self, query):
        context = self.db.similarity_search(query)
        # Here call LLM in real implementation, using stub for demo
        return [{
            "Test_ID": "TC-001",
            "Feature": "Discount Code",
            "Scenario": "Apply SAVE15",
            "Expected_Result": "15% discount applied",
            "Grounded_In": "product_specs.md"
        }]