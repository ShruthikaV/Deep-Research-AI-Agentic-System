from langgraph.graph import StateGraph
from langchain_core.tools import Tool
from Agents.research_agent import fetch_information
from Agents.drafting_agent import draft_answer
from pydantic import BaseModel

class AgentState(BaseModel):
    query: str
    research: str = ""  # Default empty string
    response: str = "" 

# Initialize LangGraph workflow
workflow = StateGraph(AgentState)

# Define nodes
workflow.add_node("research_agent", fetch_information)
workflow.add_node("drafting_agent", draft_answer)

# Define edges
workflow.add_edge("research_agent", "drafting_agent")

# Set entry and finish points
workflow.set_entry_point("research_agent")
workflow.set_finish_point("drafting_agent")

# Compile the graph
graph = workflow.compile()


def process_query(user_input):
    if isinstance(user_input, tuple):  # Fix potential tuple issue
        user_input = user_input[1]  # Extract actual query string
    state = AgentState(query=user_input)  # Ensure correct initialization
    updated_state = graph.invoke(dict(state))  # Ensure it's a pure dictionary
    return updated_state.strip() # Ensure it's returning correct results


def process_query(user_input):
    state = {
        "query": user_input,
        "research": "",
        "response": ""
    }
    print("DEBUG: State before invoke:", state)  # Debugging line
    updated_state = graph.invoke(state)  # Ensure state is valid
    return updated_state.get("response", "")

