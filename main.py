import os
from datetime import datetime
from dotenv import load_dotenv
import google.generativeai as genai
import prompts

# Load environment variables
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

# Configure the Gemini API with your API key
genai.configure(api_key=google_api_key)

# Initialize the Gemini-Pro model
model = genai.GenerativeModel('gemini-pro')

def gemini_pro_completion(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"Error in Gemini-Pro completion: {e}")
        return None

def generate_system_script_content(user_idea):
    role_identification_prompt = prompts.AGENT_ROLE_IDENTIFICATION_AGENT_PROMPT.format(user_idea=user_idea)
    role_identification = gemini_pro_completion(role_identification_prompt)

    agent_configuration_prompt = prompts.AGENT_CONFIGURATION_AGENT_PROMPT.format(agent_roles=role_identification)
    agent_configuration = gemini_pro_completion(agent_configuration_prompt)

    system_assembly_prompt = prompts.SYSTEM_ASSEMBLY_AGENT_PROMPT.format(agent_sops=agent_configuration)
    system_assembly = gemini_pro_completion(system_assembly_prompt)

    return f"# System Script for {user_idea}\n\n{system_assembly}"

def save_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    print(f"File saved: {filename}")

def get_timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def main():
    user_idea = input("Enter your idea for the multi-agent system: ")
    timestamp = get_timestamp()

    system_script_content = generate_system_script_content(user_idea)

    # Save the generated system script to a timestamped file
    save_to_file(f'system_script_{timestamp}.py', system_script_content)

if __name__ == "__main__":
    main()
