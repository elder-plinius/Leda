import os
from datetime import datetime
from dotenv import load_dotenv
import google.generativeai as genai
import prompts  # Ensure this imports your existing prompts file

# Load environment variables
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

# Configure the Gemini API with your API key
genai.configure(api_key=google_api_key)

# Initialize the Gemini-Pro model
model = genai.GenerativeModel('gemini-pro')

def gemini_pro_completion(prompt, temperature=0.0123):
    try:
        print(f"Sending prompt to Gemini with temperature {temperature}: {prompt}")
        response = model.generate_content(prompt, generation_config=genai.types.GenerationConfig(temperature=temperature))
        result = response.text.strip()
        print(f"Received from Gemini: {result}")
        return result
    except Exception as e:
        print(f"Error in Gemini-Pro completion: {e}")
        return None

def generate_agent_roles(user_idea):
    prompt = prompts.ROLE_IDENTIFICATION_PROMPT.format(user_idea=user_idea)
    return gemini_pro_completion(prompt)

def generate_agent_prompts(agent_roles):
    prompt = prompts.AGENT_CONFIGURATION_PROMPT.format(agent_roles=agent_roles)
    return gemini_pro_completion(prompt)

def generate_script_plan(agent_prompts, user_idea):
    prompt = prompts.SCRIPT_PLANNING_PROMPT.format(agent_prompts=agent_prompts, user_idea=user_idea)
    return gemini_pro_completion(prompt)

def generate_system_script(script_plan, agent_prompts):
    prompt = prompts.SYSTEM_ASSEMBLY_PROMPT.format(script_plan=script_plan, agent_prompts=agent_prompts)
    return gemini_pro_completion(prompt)

def save_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    print(f"File saved: {filename}")

def get_timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def main():
    user_idea = input("Enter your idea for the multi-agent system: ")
    timestamp = get_timestamp()

    agent_roles = generate_agent_roles(user_idea)
    agent_prompts = generate_agent_prompts(agent_roles)
    script_plan = generate_script_plan(agent_prompts, user_idea)
    system_script = generate_system_script(script_plan, agent_prompts)

    save_to_file(f'agent_prompts_{timestamp}.py', agent_prompts)
    save_to_file(f'system_script_{timestamp}.py', system_script)

if __name__ == "__main__":
    main()
