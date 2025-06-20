"""
IX-Emmanuel Domain-Specific Query Processor

Processes user queries related to mathematics and logic.
Delegates to MathKnowledge for factual answers.
"""

from math_knowledge import MathKnowledge

class IXEmmanuelQueryProcessor:
    def __init__(self):
        self.knowledge = MathKnowledge()

    def process_query(self, query: str) -> str:
        query_lower = query.lower().strip()

        # Supported patterns
        if query_lower.startswith("what is "):
            term = query_lower[8:]
            return self.knowledge.get_fact(term)
        elif "define" in query_lower:
            term = query_lower.split("define")[-1].strip()
            return self.knowledge.get_fact(term)
        elif "explain" in query_lower:
            term = query_lower.split("explain")[-1].strip()
            return self.knowledge.get_fact(term)
        else:
            return ("I am IX-Emmanuel, your mathematics and logic specialist. "
                    "Try asking me to define or explain a mathematical term or logical structure.")

# Example usage
if __name__ == "__main__":
    processor = IXEmmanuelQueryProcessor()
    print(processor.process_query("What is prime number?"))
    print(processor.process_query("Define derivative"))
    print(processor.process_query("Explain lambda calculus"))
