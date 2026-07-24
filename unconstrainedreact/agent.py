from google import genai

from tools import (
    get_user_info,
    search_bug_database,
    create_ticket
)

from prompt import SYSTEM_PROMPT
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=r"C:\Users\A.M sherif\Downloads\support-agent-system-main\support-agent-system-main\unconstrainedreact\.env")

print("KEY:", os.getenv("GEMINI_API_KEY"))

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


tools = [
    get_user_info,
    search_bug_database,
    create_ticket
]


available_tools = {

    "get_user_info": get_user_info,

    "search_bug_database": search_bug_database,

    "create_ticket": create_ticket
}



def run_agent(user_message):

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=user_message,
        config={
            "tools": tools
        }
    )


    for part in response.candidates[0].content.parts:

        if part.function_call:

            tool_name = part.function_call.name

            arguments = part.function_call.args

            tool = available_tools[tool_name]

            tool_result = tool(**arguments)


            final_response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[
        user_message,
        tool_result
    ],
    config={
        "system_instruction": SYSTEM_PROMPT,
        "tools": tools
    }
)

            return final_response.text
