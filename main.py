import os, argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types


parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
args = parser.parse_args()
# Now we can access `args.user_prompt`

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

if api_key == None:
    raise RuntimeError("Gemini API Key wasn't found")

client = genai.Client(api_key=api_key)
prompt = args.user_prompt
messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]

response = client.models.generate_content(
    model = 'gemini-2.5-flash', 
    contents = prompt
    )

if response.usage_metadata != None:
    print(f"User prompt: {prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
else:
    raise RuntimeError("Failed API request")

print(f"Response:\n{response.text}")
