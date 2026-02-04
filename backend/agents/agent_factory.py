from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy

from backend.core.llm import get_gemini_model
from backend.projects.registry import get_project

def build_agent(*, project_id: str|None ,api_key:str):

    """
    Build a stateless MVP agent 
    """
    project = get_project(project_id)
    model = get_gemini_model(api_key=api_key)
    agent = create_agent(
        model= model,
        system_prompt=project.system_prompt,
        tools = project.tools,
        response_format=ToolStrategy(project.response_scheme)
    )

    return agent 