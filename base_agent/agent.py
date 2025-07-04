from google.adk.agents import LlmAgent
from .tools.hello_world_tool import hello_world_tool
from .sub_agents.sub_agent.agent import sub_agent

root_agent = LlmAgent(
    name="root_agent",
    model='gemini-2.5-flash',
    description="You are a helpful assistant that can answer questions and help with tasks.",
    instruction="You are a helpful assistant that can answer questions and help with tasks.",
    sub_agents=[sub_agent],
    tools=[hello_world_tool],
)