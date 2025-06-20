"""
IX-Emmanuel CLI Interface

Provides an interactive command-line interface for aerospace and physics
queries routed through EmmanuelCore to IX-Gibson.
"""

from core.emmanuel_core import EmmanuelCore

def run_emmanuel_cli():
    core = EmmanuelCore()
    print("IX-Emmanuel — Aerospace and Physics Specialist")
    print("Enter your queries below. Type 'exit' to quit.\n")

    while True:
        user_input = input("Emmanuel> ").strip()
        if user_input.lower() in ("exit", "quit"):
            print("Exiting IX-Emmanuel interface. Safe travels.")
            break
        output = core.handle_query(user_input)
        print(f"→ {output}")

if __name__ == "__main__":
    run_emmanuel_cli()
