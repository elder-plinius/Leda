import os
import google.generativeai as genai
from dotenv import load_dotenv

# Import the prompts from prompts.py (Assuming this file contains structured prompts for each operation)
import prompts

# Load environment variables
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

# Configure the Gemini API with your API key
genai.configure(api_key=google_api_key)

# Initialize the Gemini-Pro model
model = genai.GenerativeModel('gemini-pro')

def generate_response_with_gemini(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"Error in Gemini-Pro completion: {e}")
        return None

def role_identification(user_idea):
    prompt = prompts.ROLE_IDENTIFICATION_PROMPT.format(user_idea=user_idea)
    return generate_response_with_gemini(prompt)

def configure_agents(agent_roles):
    prompt = prompts.AGENT_CONFIGURATION_PROMPT.format(agent_roles=agent_roles)
    return generate_response_with_gemini(prompt)

def assemble_system(agent_instructions):
    prompt = prompts.SYSTEM_ASSEMBLY_PROMPT.format(agent_instructions=agent_instructions)
    return generate_response_with_gemini(prompt)

def main():
    user_idea = input("Enter your idea for the multi-agent system: ")
    agent_roles = role_identification(user_idea)
    agent_instructions = configure_agents(agent_roles)
    system_script = assemble_system(agent_instructions)

    # Print the system script or further process as needed
    print(system_script)

if __name__ == "__main__":
    main()
