# Base Agent

A base agent implementation using Google ADK, designed to be easily extended with sub-agents and tools. This package provides a template for building advanced AI agents that can interact with users, delegate tasks to sub-agents, and utilize custom tools.

## Features
- **Google ADK Integration:** Leverages the `LlmAgent` from Google ADK for powerful language model capabilities.
- **Sub-Agent Support:** Easily add and manage sub-agents for modular task delegation.
- **Custom Tools:** Integrate Python functions as tools for the agent to use.
- **Vertex AI Ready:** Example deployment script for running the agent on Google Vertex AI.

## Directory Structure
```
base-agent/
├── base_agent/
│   ├── __init__.py
│   ├── agent.py           # Main agent definition
│   ├── tools/
│   │   └── hello_world_tool.py  # Example tool
│   └── sub_agents/
│       └── sub_agent/
│           └── agent.py   # Example sub-agent
├── deployment/
│   ├── deploy.py          # Deployment script
│   └── run.py             # Example run script
├── pyproject.toml         # Poetry project file
└── README.md
```

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd tag-agents/base-agent
   ```
2. **Install dependencies with Poetry:**
   ```bash
   poetry install
   ```
   Requires Python 3.11 or higher.

## Usage

The main agent is defined in `base_agent/agent.py`:
```python
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
```

### Example Tool
`hello_world_tool.py`:
```python
def hello_world_tool(name: str) -> str:
    """
    This tool prints "Hello, {name}!"
    """
    return f"Hello, {name}!"
```

### Example Sub-Agent
`sub_agent/agent.py`:
```python
from google.adk.agents import LlmAgent

sub_agent = LlmAgent(
    name="sub_agent",
    model='gemini-2.5-flash',
    description="You are a helpful assistant that can answer questions and help with tasks.",
    instruction="You are a helpful assistant that can answer questions and help with tasks.",
    output_key="sub_agent_output",
)
```

## Deployment

1. **Configure Environment Variables:**
   - Edit the `.env` file and replace the environment variables with your GCP project values:
     - `GOOGLE_CLOUD_PROJECT`
     - `GOOGLE_CLOUD_LOCATION`
     - `GOOGLE_API_KEY`
     - `STAGING_BUCKET`
   - **Note:** `AGENT_ENGINE_ID` is set automatically when the agent is deployed; you do not need to set it manually.

2. **Deploy the Agent to GCP Agent Engine:**
   ```bash
   python deployment/deploy.py
   ```

3. **Test the Deployed Agent:**
   - You can run a test to make sure the deployment works by calling the deployed agent and asking something:
   ```bash
   python deployment/run.py
   ```

## Customization
- **Add new tools:** Place Python functions in `base_agent/tools/` and add them to the agent's `tools` list.
- **Add sub-agents:** Define new sub-agents in `base_agent/sub_agents/` and include them in the main agent's `sub_agents` list.

## Author
Damian Martinez Carmona (<damian.martinez.carmona@gmail.com>)

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
