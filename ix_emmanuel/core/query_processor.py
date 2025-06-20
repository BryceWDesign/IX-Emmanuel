"""
IX-Emmanuel Query Processor

Interprets philosophical and psychological queries, delivering
structured responses using ontology-based logic.
"""

from core.ontology_engine import OntologyEngine

class IXEmmanuelQueryProcessor:
    def __init__(self):
        self.engine = OntologyEngine()

    def process_query(self, query: str) -> str:
        query = query.lower().strip()
        trigger_phrases = ["explain", "what is", "tell me about"]

        # Determine topic
        topic = None
        for trigger in trigger_phrases:
            if query.startswith(trigger):
                topic = query.replace(trigger, "").strip()
                break

        if not topic:
            return "Please begin your query with 'What is', 'Explain', or 'Tell me about'."

        topic_info = self.engine.retrieve_topic(topic)
        if "error" in topic_info:
            return topic_info["error"]

        response = f"🧠 Topic: {topic.capitalize()}\n"
        response += f"Definition: {topic_info.get('definition')}\n\n"

        if "theories" in topic_info:
            response += "Theories:\n"
            for t in topic_info["theories"]:
                response += f"- {t}\n"

        if "philosophical_stances" in topic_info:
            response += "Philosophical Stances:\n"
            for p in topic_info["philosophical_stances"]:
                response += f"- {p}\n"

        if "questions" in topic_info:
            response += "\nUnresolved Questions:\n"
            for q in topic_info["questions"]:
                response += f"• {q}\n"

        return response

# Example usage
if __name__ == "__main__":
    qp = IXEmmanuelQueryProcessor()
    print(qp.process_query("Explain consciousness"))
    print(qp.process_query("What is free will"))
    print(qp.process_query("What is ethics"))
