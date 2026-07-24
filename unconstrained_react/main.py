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

# Define the tools array
tools = [
    get_soil_moisture_tool,
    get_weather_forecast_tool,
    get_crop_and_soil_data_tool,
    irrigate_tool,
    suspend_irrigation_tool
]

# 2. Initialize the Groq LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile", 
    temperature=0.0
).bind_tools(tools, parallel_tool_calls=False)



# prompt
domain_knowledge = """
You are the lead Smart Irrigation AI Agent for Greenfield AgroWorks.

Your goal is to make safe and efficient irrigation decisions that:
- Keep crops adequately hydrated.
- Minimize unnecessary water usage.
- Avoid over-irrigation and flooding.
- Consider upcoming rainfall before initiating irrigation.

You have access to tools that provide information about soil moisture,
weather conditions, crop and soil characteristics, and irrigation controls.

You should reason about the available information and decide which tools
are necessary to accomplish the user's request. You are not required to
use every available tool, and you may choose the order in which tools are
used based on the situation.

Before taking any irrigation action, make sure you have sufficient and
relevant information to make a safe decision.

Use irrigation control tools only when they are appropriate for the
situation and the user's request.

After completing the task, provide a concise final answer explaining:
- What you determined.
- What action, if any, you took.
- Why you took that action.

Once the task has been completed and you have enough information to answer
the user, stop using tools and provide the final answer.
"""

# Agent
agent = create_react_agent(llm, tools, prompt=domain_knowledge)


# Testing
if __name__ == "__main__":
    print("\n--- Running UNCONSTRAINED ReAct Agent ---")

    test_input = (
        "Evaluate the irrigation needs for Zone 2. "
        "Use your tools to make the final decision."
    )

    for chunk in agent.stream(
        {"messages": [("user", test_input)]},
        stream_mode="values"
    ):
        chunk["messages"][-1].pretty_print()
