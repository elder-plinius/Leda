# This file contains the system prompts for building and configuring each agent in the multi-agent AI system.

# Prompt for Role Identification Agent
ROLE_IDENTIFICATION_PROMPT = """
Based on the following idea: '{user_idea}', identify and list the specific types of agents needed to create a complete team of autonomous AI agents.
Detail their roles, responsibilities, and capabilities.
Output Format: A list of a balanced, complete team of agent types with descriptions of their roles and ideal output formats, and arrange them in an 
order that makes logical sense for the workflow/task at had and formatted in bullet points or a numbered list.
"""

# Prompt for Agent Configuration
AGENT_CONFIGURATION_PROMPT = """
Given these identified agent roles: '{agent_roles}', write System Prompts for each agent in the team. Ensure that each prompt is 
tailored to the specific functionalities of the agent, considering the operational context and objectives of the team.
Output Format: A single Python file of the whole AI team's system prompts with capitalized constant names for each prompt, an equal sign between each 
agent name and their prompt, and triple quotes surrounding the prompt content. Follow best-practice prompting techqniques, being specfic about 
objectives and output formats.
"""

SCRIPT_PLANNING_PROMPT = """
Create a detailed plan for a multi-agent AI system Python file using the provided agent prompts: '{agent_prompts}'. The plan should detail 
the interactions, data flow, and error handling mechanisms for each agent. Consider how each agent's output can be 
utilized as input for others and how they collectively achieve the goal of '{user_idea}'.

Outline the following components:
- Data Exchange: How outputs from one agent are used as inputs for other agents.
- Error Handling: Strategies for dealing with unexpected inputs or failures.
- Execution Flow: Sequence of operations.
- The final output format (should it print to termnial or be stored in a file).

Output Format: A structured system architecture/tech spec, ready to be sent to a developer to be turned into a Python script.

"""

# Prompt for System Assembly
SYSTEM_ASSEMBLY_PROMPT = """
With the script plan '{script_plan}' and prompts '{agent_prompts}', develop a production-ready Python script to operationalize the 
multi-agent AI system. Ensure the script dynamically imports the most recent agent prompts file and 
utilizes its contents.

Output Format: A complete, FULLY FUNCTIONAL and PRODUCTION-READY Python script ready for deployment, with NO PLACEHOLDERS, complete logic, correct
numbers of positional arguments. REMEMBER: generate_content_with_gemini takes ONE positional argument. Take a deep breath and think step by step.

Here's an example skeleton structure for you to get a rough idea of what the first part of the python script might look like:

# Import necessary libraries
import os
import importlib
import sys
from datetime import datetime
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables for API keys
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

# Configure the Gemini AI model
genai.configure(api_key=google_api_key)
model = genai.GenerativeModel('gemini-pro')

# Function to dynamically import the latest agent prompts file
def import_latest_agent_prompts():
    prompt_files = [f for f in os.listdir() if f.startswith('agent_prompts_') and f.endswith('.py')]
    if not prompt_files:
        raise FileNotFoundError("No timestamped agent prompts files found.")
    latest_file = max(prompt_files, key=lambda f: os.path.getctime(f))
    latest_module_name = latest_file.split('.')[0]
    if latest_module_name not in sys.modules:
        return importlib.import_module(latest_module_name)
    else:
        return importlib.reload(sys.modules[latest_module_name])

# Function to generate text content using Gemini AI model
def generate_content_with_gemini(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text.strip()


"""
