import os
import sys
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from shared_tools.agent_tools import (
    get_soil_moisture_tool,
    get_weather_forecast_tool,
    get_crop_and_soil_data_tool,
    irrigate_tool,
    suspend_irrigation_tool
)

load_dotenv()
if not os.environ.get("GROQ_API_KEY"):
    raise ValueError("GROQ_API_KEY is missing! Check your .env file.")

# 2. Initialize the Groq LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile", 
    temperature=0.0
)

# Define the tools array
tools = [
    get_soil_moisture_tool,
    get_weather_forecast_tool,
    get_crop_and_soil_data_tool,
    irrigate_tool,
    suspend_irrigation_tool
]

# prompt
domain_knowledge = """You are the lead Smart Irrigation AI Agent for Greenfield AgroWorks. 
Your goal is to optimize water usage, prevent crops from dying of thirst, and avoid flooding if rain is imminent. 
You must logically combine data from soil and weather before taking any irrigation action.
"""

# Agent
agent = create_react_agent(llm, tools, prompt=domain_knowledge)


# Testing
if __name__ == "__main__":
    print("\n--- Running UNCONSTRAINED ReAct Agent ---")

    test_input = "Evaluate the irrigation needs for Zone 2. Use your tools to make the final decision."
    
    response = agent.invoke({"messages": [("user", test_input)]})
    print("\n[FINAL OUTPUT]:\n", response["messages"][-1].content)