import os
import json
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY not found in .env")

genai.configure(api_key=API_KEY)
MODEL_NAME = "gemini-2.0-flash"


def _parse_model_list(text: str) -> list[str]:
    """Parse model output into a clean list of strings."""

    t = text.strip()

    # 1) Remove ``` or ```json fences if present
    if t.startswith("```"):
        lines = t.splitlines()
        # drop first line (``` or ```json)
        lines = lines[1:]
        # drop last line if it's a fence
        if lines and lines[-1].strip().startswith("```"):
            lines = lines[:-1]
        t = "\n".join(lines).strip()

    # 2) Try direct JSON
    try:
        data = json.loads(t)
        if isinstance(data, list):
            return [s for s in data if isinstance(s, str)]
    except json.JSONDecodeError:
        pass

    # 3) Try to extract JSON between [ and ]
    start = t.find("[")
    end = t.rfind("]")
    if start != -1 and end != -1 and end > start:
        snippet = t[start : end + 1]
        try:
            data = json.loads(snippet)
            if isinstance(data, list):
                return [s for s in data if isinstance(s, str)]
        except json.JSONDecodeError:
            pass

    # 4) Last fallback: split by lines
    lines = [
        ln.strip("-•, ").strip()
        for ln in t.splitlines()
        if ln.strip()
    ]
    return lines


def generate_icebreakers_for_pair(sender: dict, receiver: dict) -> list[str]:
    sender_desc = (
        f"{sender['name']}, {sender.get('age', 'N/A')}, from {sender.get('location', 'unknown')}, "
        f"interests: {', '.join(sender.get('interests', []))}. "
        f"Bio: {sender.get('bio', '')}"
    )

    receiver_desc = (
        f"{receiver['name']}, {receiver.get('age', 'N/A')}, from {receiver.get('location', 'unknown')}, "
        f"interests: {', '.join(receiver.get('interests', []))}. "
        f"Bio: {receiver.get('bio', '')}"
    )

    prompt = f"""
You are an assistant that writes 3 short, friendly, safe opening messages.

Sender:
{sender_desc}

Receiver:
{receiver_desc}

Rules:
- Write 3 icebreakers that the SENDER can send to the RECEIVER.
- Be casual, respectful, and not cringey.
- Use shared or complementary interests when possible.
- Do NOT ask for phone numbers, Instagram, Snapchat, or any contact info.
- Do NOT include explicit/sexual or offensive content.
- Each message should be one or two sentences max.

Return ONLY a JSON array of exactly 3 strings.
Do NOT wrap it in markdown or ``` fences.
Example:
["msg1", "msg2", "msg3"]
"""

    model = genai.GenerativeModel(MODEL_NAME)
    response = model.generate_content(prompt)

    raw_text = response.text or ""
    messages = _parse_model_list(raw_text)

    # keep max 3
    return messages[:3]
