"""
IX-Emmanuel CLI Interface

Enables direct command-line interaction with the
philosophical reasoning engine.
"""

import sys
from core.query_processor import IXEmmanuelQueryProcessor

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py \"Explain [topic]\"")
        sys.exit(1)

    query = sys.argv[1]
    engine = IXEmmanuelQueryProcessor()
    response = engine.process_query(query)

    print("\n🧠 IX-Emmanuel Response 🧠")
    print(response)

if __name__ == "__main__":
    main()
