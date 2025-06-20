"""
IX-Emmanuel Core Mathematics Knowledge Module

Houses essential mathematical and logic knowledge, definitions, and symbolic principles.
Optimized for speed and clarity for rapid logic assembly under IX-Gibson orchestration.
"""

class MathKnowledge:
    def __init__(self):
        # Key definitions and concepts from mathematics and logic
        self.facts = {
            "pythagorean theorem": "In a right-angled triangle: a² + b² = c².",
            "derivative": "The rate at which a function changes at any point. d/dx[f(x)]",
            "integral": "The area under the curve of a function. ∫f(x)dx",
            "boolean logic": "A form of algebra using only true and false values.",
            "prime number": "A natural number greater than 1 that has no positive divisors other than 1 and itself.",
            "proof by induction": "A method of mathematical proof typically used to establish a given statement for all natural numbers.",
            "modus ponens": "If P implies Q and P is true, then Q must also be true.",
            "lambda calculus": "A formal system in mathematical logic for expressing computation by way of variable binding and substitution."
        }

    def get_fact(self, term: str) -> str:
        """
        Return a definition or fact for a mathematical term.
        """
        term_lower = term.lower().strip()
        return self.facts.get(term_lower, f"Sorry, I don't have information about '{term}' yet.")

# Test run
if __name__ == "__main__":
    mk = MathKnowledge()
    print(mk.get_fact("Modus Ponens"))
    print(mk.get_fact("Integral"))
    print(mk.get_fact("Infinity"))
