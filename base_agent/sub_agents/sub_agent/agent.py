from google.adk.agents import LlmAgent

sub_agent = LlmAgent(
    name="sub_agent",
    model='gemini-2.5-flash',
    description="You are a helpful assistant that can answer questions and help with tasks.",
    instruction="You are a helpful assistant that can answer questions and help with tasks.",
    output_key="sub_agent_output",
)