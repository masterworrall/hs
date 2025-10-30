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

def send_prompt(prompt: str, model: str = DEFAULT_MODEL, **kwargs) -> str:
    """
    Send a prompt to the Responses API and return text.
    """
    if not prompt:
        return ""
    resp = _client.responses.create(model=model, input=prompt, **kwargs)
    # Best-effort extraction of text
    if getattr(resp, "output_text", None):
        return resp.output_text
    try:
        output = getattr(resp, "output", None) or resp.get("output", None)
        if output:
            parts = []
            for item in output:
                for c in item.get("content", []):
                    if isinstance(c, dict):
                        if "text" in c:
                            parts.append(c["text"])
                        elif "parts" in c:
                            parts.extend(c["parts"])
                    elif isinstance(c, str):
                        parts.append(c)
            if parts:
                return "".join(parts)
    except Exception:
        pass
    return str(resp)