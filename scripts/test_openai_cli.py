import os
import sys

# Ensure project root is on sys.path so 'app' package can be imported
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from app.openai_client import send_prompt, load_system_prompt

# Edit this prompt to test different inputs
PROMPT = """No disposition of the registered estate (other than a charge) by the proprietor of the registered estate or by the proprietor of any registered charge is to be registered without a certificate signed on behalf of Riverside Lodge Management Limited of 323 Wilmslow Road, Fallowfield, Manchester M14 6NW by its director, secretary or solicitor that the provisions of Part III of the Fourth Schedule of the registered lease have been complied with.."""

def main():
    # Load and show system prompt
    system_prompt = load_system_prompt()
    print("System Prompt:")
    print(system_prompt or "(none)")
    
    print("\nUser Prompt:")
    print(PROMPT)
    print("\nSending to OpenAI API...\n")
    
    try:
        resp = send_prompt(PROMPT)  # system prompt loaded automatically
        print("Response:\n")
        print(resp)
    except Exception as e:
        print("Error:", e, file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()