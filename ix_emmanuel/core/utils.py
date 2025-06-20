"""
IX-Emmanuel Utilities Module

Provides helper functions for input cleaning and basic validation of math/logic queries.
"""

import re

def clean_query(query: str) -> str:
    """
    Normalize the query by trimming whitespace and removing excessive symbols.
    """
    query = query.strip()
    query = re.sub(r'\s+', ' ', query)
    query = re.sub(r'[^\w\s\-\+\=\^\(\)\[\]]+', '', query)
    return query

def is_valid_query(query: str) -> bool:
    """
    Validate that the query appears meaningful.
    """
    return bool(query and len(query) > 3 and any(char.isalpha() for char in query))

# Example usage
if __name__ == "__main__":
    test_queries = [
        "   What is derivative??   ",
        "!?$%",
        "mod",
        "Explain lambda calculus!"
    ]
    for q in test_queries:
        cleaned = clean_query(q)
        valid = is_valid_query(cleaned)
        print(f"'{q}' → Cleaned: '{cleaned}' | Valid: {valid}")
