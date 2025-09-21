import os
from dotenv import load_dotenv
from alith import Agent

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from the environment
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found in .env file. Please add it.")

# Instantiate the Agent for OpenAI
# The 'alith' library can be configured to use different providers.
# By providing the api_key and a standard model name, it will default to OpenAI.
agent = Agent(
    model="gpt-3.5-turbo",
    api_key=api_key,
)

# Run inference queries
print("--- Query 1: What is cryptocurrency? ---")
response1 = agent.prompt("What is cryptocurrency?")
print(response1)

print("\n--- Query 2: What is blockchain? ---")
response2 = agent.prompt("What is blockchain?")
print(response2)