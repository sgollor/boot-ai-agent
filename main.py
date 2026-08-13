import argparse
import json
import os

from dotenv import load_dotenv
from openai import OpenAI

from call_function import available_functions, call_function
from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file
from functions.write_file import write_file
from prompts import system_prompt

load_dotenv()

api_key = os.environ.get("OPENROUTER_API_KEY")

if api_key is None:
    raise RuntimeError(
        "OPENROUTER_API_KEY not found. Make sure it is set in your .env file."
    )

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)


def generate_content(client, messages, tools=None):
    return client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        temperature=0,
        tools=tools,
    )


def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose output",
    )
    args = parser.parse_args()

    user_prompt = args.user_prompt
    messages = [
        {
            "role": "system",
            "content": system_prompt,
        },
        {
            "role": "user",
            "content": user_prompt,
        },
    ]

    response = generate_content(client, messages, tools=available_functions)

    usage = response.usage
    if usage is None:
        raise RuntimeError(
            "API request failed: response usage metadata is missing."
        )

    if args.verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {usage.prompt_tokens}")
        print(f"Response tokens: {usage.completion_tokens}")

    message = response.choices[0].message
    tool_calls = getattr(message, "tool_calls", None) or []
    if tool_calls:
        for tool_call in tool_calls:
            result_message = call_function(tool_call, verbose=args.verbose)
            if not result_message.get("content"):
                raise ValueError("Tool call returned empty content")

            if args.verbose:
                print(f"-> {result_message['content']}")
    else:
        print(message.content)


if __name__ == "__main__":
    main()
