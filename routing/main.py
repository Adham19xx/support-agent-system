import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()


api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("API key missing")

client = genai.Client(api_key=api_key)


def run_restart_protocol(text):
    return f"Restarting system (len={len(text)})"


def run_escalation_protocol(text):
    return "Escalating to engineer"


def run_faq_protocol(text):
    return "Sending help email"


def deterministic_routing_agent(ticket_text):

    prompt = f"""
Classify this support ticket into EXACTLY ONE category:
- RESTART: for 500 errors, server down, crashes, or reboot requests.
- ESCALATE: for repeated complaints, slowness, or human engineer requests.
- FAQ: for general questions, help docs, or basic guidance.

Only return the category name (RESTART, ESCALATE, or FAQ).

Ticket:
"{ticket_text}"
"""

    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",  # الاسم من القائمة المتاحة عندك
            contents=prompt,
            config=types.GenerateContentConfig(temperature=0.0)
        )
    except Exception as e:
        return f"Error: {str(e)}"

    category = response.text.strip().upper()
    print("Model decision:", category)

    if category == "RESTART":
        return run_restart_protocol(ticket_text)

    elif category == "ESCALATE":
        return run_escalation_protocol(ticket_text)

    elif category == "FAQ":
        return run_faq_protocol(ticket_text)

    else:
        return "Unknown result"


if __name__ == "__main__":

    print("Test 1:")
    print(deterministic_routing_agent(
        "The website is down with a 500 error"
    ))

    print("\nTest 2:")
    print(deterministic_routing_agent(
        "Server is slow and I complained many times"
    ))
    
    