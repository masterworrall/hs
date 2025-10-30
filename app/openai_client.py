import os
from dotenv import load_dotenv
from openai import OpenAI

# load .env from project root (or environment)
load_dotenv(dotenv_path=os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".env")))

API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    # fallback to environment variable if .env not present
    API_KEY = os.getenv("OPENAI_API_KEY")

_client = OpenAI(api_key=API_KEY)

DEFAULT_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

def load_system_prompt() -> str:
    """Load system prompt from data/system.prompt file"""
    try:
        prompt_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "system.prompt"))
        with open(prompt_path, "r", encoding="utf-8") as f:
            return f.read().strip()
    except Exception as e:
        print(f"Warning: Could not load system prompt: {e}", file=sys.stderr)
        return ""

def send_prompt(prompt: str, system_prompt: str = None, model: str = DEFAULT_MODEL, **kwargs) -> str:
    """
    Send prompts to the OpenAI API with optional system prompt.
    If system_prompt is None, loads from data/system.prompt
    """
    if not prompt:
        return ""
        
    if system_prompt is None:
        system_prompt = load_system_prompt()

    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})
    
    resp = _client.chat.completions.create(
        model=model,
        messages=messages,
        **kwargs
    )
    
    # Extract response text from chat completion
    try:
        return resp.choices[0].message.content
    except Exception:
        return str(resp)