"""
IX-Emmanuel Core Module

Processes aerospace and physics queries, interfacing with IX-Gibson
through the GibsonAdapter to provide expert domain responses.
"""

from .gibson_adapter import GibsonAdapter

class EmmanuelCore:
    def __init__(self):
        self.gibson = GibsonAdapter()

    def handle_query(self, query: str) -> str:
        """
        Send an aerospace or physics query to IX-Gibson and retrieve response.

        Args:
            query (str): User input related to aerospace or physics.

        Returns:
            str: Response from IX-Gibson or error message.
        """
        response = self.gibson.query_gibson(query)
        if "error" in response:
            return f"[Emmanuel Error] {response['error']}"
        return response.get("answer", "[Emmanuel] No answer available.")
