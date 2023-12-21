# Leda: Mother of Agents

Overview

Leda is an innovative application built with OpenAI's Gemini AI, designed to autonomously generate and operationalize teams of specialized agents from a single user prompt. It not only crafts detailed system prompts for each agent in the team but also generates the necessary Python script to run the system, streamlining the process from conception to execution.

Key Features

    Sequential Agent Execution: Orchestrates agents in a logical sequence, where the output of one chains to the input for another.
    Automated Script Generation: Produces a ready-to-deploy Python script that operationalizes the planned multi-agent system.
    Adaptive Chain Prompting: Each agent adapts its strategy based on the context provided by its predecessors, ensuring a cohesive solution.

Quick Start Guide

    Set Up:
        Ensure Python 3.7+ is installed.
        Obtain a Gemini API key.

    Installation:
        Clone the repository and install dependencies.
        Place your Gemini API key in a .env file as GOOGLE_API_KEY=your_api_key_here.

    Run Leda:
        Execute python main.py and input your idea for the AI system.

Outputs

    Agent Prompts File (agent_prompts_timestamp.py): Contains custom prompts for each agent.
    System Script (system_script_timestamp.py): A ready-to-execute Python script embodying the multi-agent system.

Value Proposition

Leda dramatically simplifies the creation of complex, multi-agent AI systems. By generating both the system prompts and the executable script, it allows developers and innovators to focus on the conceptual side of AI system design while Leda takes care of the technical execution. Whether you're scaling up a system or experimenting with new ideas, Leda offers a fast, flexible, and user-friendly solution.
