"""
IX-Emmanuel CLI Entry Point

Enables command-line querying of IX-Emmanuel for mathematics and logic.
Directly invokes the query processor and prints results.
"""

import sys
from core.query_processor import IXEmmanuelQueryProcessor

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py \"Your math or logic query here\"")
        sys.exit(1)

    query = sys.argv[1]
    processor = IXEmmanuelQueryProcessor()
    response = processor.process_query(query)

    print("\n📐 IX-Emmanuel Response 📐")
    print(response)

if __name__ == "__main__":
    main()
