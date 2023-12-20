# prompts.py
# This file contains the system prompts for building and configuring each agent in the multi-agent AI system.

# Prompt for Role Identification Agent
ROLE_IDENTIFICATION_PROMPT = """
Based on the user's input idea: '{user_idea}', identify and list the specific types of agents needed for the multi-agent AI system. Describe their roles, responsibilities, and capabilities, emphasizing the strengths of AI models.
Output Format: A detailed list of agent types with descriptions of their roles and capabilities, formatted in bullet points or a numbered list.
"""

# Prompt for Agent Configuration
AGENT_CONFIGURATION_PROMPT = """
Given the identified agent roles: '{agent_roles}', create internal instructions for each agent type. These instructions should be specific to the agent's functions, considering the context and objectives of the multi-agent system.
Output Format: A Python script section with constant names for each set of internal instructions, formatted with triple quotes surrounding each instruction set.
"""

# Prompt for System Assembly
SYSTEM_ASSEMBLY_PROMPT = """
With the internal instructions for each agent type: '{agent_instructions}', develop a production-ready Python script to operationalize the multi-agent AI system. 
Ensure the script is complete and executable, allowing for direct deployment and usage.
Output Format: A comprehensive Python script ready for deployment, with complete logic, proper indentation, clear variable names, and comments.
"""
