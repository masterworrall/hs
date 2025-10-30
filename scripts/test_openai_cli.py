import os
import sys

# Ensure project root is on sys.path so 'app' package can be imported
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from app.openai_client import send_prompt

# Edit this prompt to test different inputs
PROMPT = """What is an RXC form regards the UK Land Registry"""

def main():
    print("Prompt:")
    print(PROMPT)
    print("\nSending to OpenAI Responses API...\n")
    try:
        resp = send_prompt(PROMPT)
        print("Response:\n")
        print(resp)
    except Exception as e:
        print("Error:", e, file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()