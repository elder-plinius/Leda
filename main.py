import os
from datetime import datetime
from dotenv import load_dotenv
import google.generativeai as genai
import prompts
from trulens_eval import Tru, TruCustomApp, Feedback, Select
from trulens_eval.tru_custom_app import instrument
from trulens_eval.feedback import Groundedness
from trulens_eval.feedback.provider.openai import OpenAI as fOpenAI

# Load environment variables
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")
os.environ["OPENAI_API_KEY"] = google_api_key

# Configure the Gemini API with your API key
genai.configure(api_key=google_api_key)

# Initialize the Gemini-Pro model and TruLens
model = genai.GenerativeModel('gemini-pro')
tru = Tru()
fopenai = fOpenAI()

class LedaApp:
    @instrument
    def generate_agent_roles(self, user_idea):
        prompt = prompts.ROLE_IDENTIFICATION_PROMPT.format(user_idea=user_idea)
        return gemini_pro_completion(prompt)

    @instrument
    def generate_agent_prompts(self, agent_roles):
        prompt = prompts.AGENT_CONFIGURATION_PROMPT.format(agent_roles=agent_roles)
        return gemini_pro_completion(prompt)

    @instrument
    def generate_script_plan(self, agent_prompts, user_idea):
        prompt = prompts.SCRIPT_PLANNING_PROMPT.format(agent_prompts=agent_prompts, user_idea=user_idea)
        return gemini_pro_completion(prompt)

    @instrument
    def generate_system_script(self, script_plan, agent_prompts):
        prompt = prompts.SYSTEM_ASSEMBLY_PROMPT.format(script_plan=script_plan, agent_prompts=agent_prompts)
        return gemini_pro_completion(prompt)

def gemini_pro_completion(prompt, temperature=0.0111):
    try:
        print(f"Sending prompt to Gemini with temperature {temperature}: {prompt}")
        response = model.generate_content(prompt, generation_config=genai.types.GenerationConfig(temperature=temperature))
        result = response.text.strip()
        print(f"Received from Gemini: {result}")
        return result
    except Exception as e:
        print(f"Error in Gemini-Pro completion: {e}")
        return None

# Feedback functions
groundedness_feedback = Feedback(
    Groundedness(groundedness_provider=fopenai).groundedness_measure,
    name="Groundedness"
).on(Select.RecordCalls.generate_agent_roles.output)


def save_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    print(f"File saved: {filename}")

def get_timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def main():
    user_idea = input("Enter your idea for the multi-agent system: ")
    timestamp = get_timestamp()
    leda_app = LedaApp()

    # Wrap the application logic with TruCustomApp
    with TruCustomApp(app=leda_app, app_id='LedaApp', feedbacks=[groundedness_feedback]) as tru_rag:
        agent_roles = leda_app.generate_agent_roles(user_idea)
        agent_prompts = leda_app.generate_agent_prompts(agent_roles)
        script_plan = leda_app.generate_script_plan(agent_prompts, user_idea)
        system_script = leda_app.generate_system_script(script_plan, agent_prompts)

        save_to_file(f'agent_prompts_{timestamp}.py', agent_prompts)
        save_to_file(f'system_script_{timestamp}.py', system_script)

    # View the leaderboard and dashboard after the execution
    print(tru.get_leaderboard(app_ids=["LedaApp"]))
    tru.run_dashboard()

if __name__ == "__main__":
    main()
