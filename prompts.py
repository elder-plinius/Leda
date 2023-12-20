# prompts.py
# This file contains the system prompts for building and configuring each agent in the multi-agent AI system.

# Prompt for Role Identification Agent
ROLE_IDENTIFICATION_PROMPT = """
Based on the following idea: '{user_idea}', identify and list the specific types of agents needed to create a complete team of autonomous AI agents. Detail their roles, responsibilities, and capabilities, being sure to play to the strengths of AI models.
Output Format: A list of a balanced, complete team of agent types with brief descriptions of their roles and capabilities, and arrange them in an order that makes logical sense for the workflow/task at had and formatted in bullet points or a numbered list.
"""

# Prompt for Agent Configuration
AGENT_CONFIGURATION_PROMPT = """
Given these identified agent roles: '{agent_roles}', write Custom Instructions/System Prompts for each agent type. Ensure that each prompt is tailored to the specific functionalities of the agent, considering the operational context and objectives of the team.
Output Format: A single Python file of the whole agent team with capitalized constant names for each prompt, an equal sign between each agent name and their prompt, and triple quotes surrounding the prompt content. Follow best-practice prompting standards.
"""

# Prompt for System Assembly
SYSTEM_ASSEMBLY_PROMPT = """
With the internal instructions for each agent type: '{agent_instructions}', develop a production-ready Python script to operationalize the multi-agent AI system. 
Ensure the script is complete and executable, allowing for direct deployment and usage.
Output Format: A comprehensive Python script ready for deployment, with complete logic, proper indentation, clear variable names, and comments.
"""
