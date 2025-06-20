"""
IX-Emmanuel Utility Functions

Handles input normalization, semantic trimming,
and philosophical query diagnostics.
"""

import re

def normalize_input(text: str) -> str:
    """
    Normalize philosophical query input by stripping
    excess punctuation, whitespace, and casing.
    """
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s\-]', '', text)
    return text.lower()

def is_valid_philosophy_query(text: str) -> bool:
    """
    Validate if the query resembles a philosophical question.
    """
    return any(phrase in text for phrase in ["what is", "explain", "tell me about"]) and len(text) > 10

# Example usage
if __name__ == "__main__":
    inputs = [
        " What is consciousness? ",
        "EXPLAIN free will!!!",
        "yo",
        "define stuff"
    ]
    for i in inputs:
        clean = normalize_input(i)
        print(f"Original: '{i}' → Cleaned: '{clean}' | Valid: {is_valid_philosophy_query(clean)}")
