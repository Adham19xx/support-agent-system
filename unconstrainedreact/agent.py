from google import genai

from tools import (
    get_user_info,
    search_bug_database,
    create_ticket
)

import os


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


tools = [
    get_user_info,
    search_bug_database,
    create_ticket
]
