from langgraph.graph import StateGraph, END
from graph.University_state import UniversityState
from graph.router import agent_router

from nodes.extractor_profile import extract_profile
from nodes.classifier import classify_query

from agents.admission_agent import admission_agent
from agents.hostel_agent import hostel_agent
from agents.placement_agent import placement_agent
from agents.acdemic_agent import acdemic_agent
from agents.memory_agent import memory_agent
from agents.profile_agent import profile_agent
from agents.general_agent import general_agent

from memory.checkpoint import memory


def build_graph():

    builder = StateGraph(UniversityState)

    # -------------------------
    # Nodes
    # -------------------------

    builder.add_node("extract_profile", extract_profile)

    builder.add_node("classify_query", classify_query)

    builder.add_node("admission", admission_agent)

    builder.add_node("hostel", hostel_agent)

    builder.add_node("placement", placement_agent)

    builder.add_node("academic", acdemic_agent)

    builder.add_node("memory", memory_agent)

    builder.add_node("profile", profile_agent)

    builder.add_node("general", general_agent)

    # -------------------------
    # Entry Point
    # -------------------------

    builder.set_entry_point("extract_profile")

    builder.add_edge(
        "extract_profile",
        "classify_query"
    )

    # -------------------------
    # Routing
    # -------------------------

    builder.add_conditional_edges(
        "classify_query",
        agent_router,
        {
            "admission": "admission",
            "hostel": "hostel",
            "placement": "placement",
            "academic": "academic",
            "memory": "memory",
            "profile": "profile",
            "general": "general"
        }
    )

    # -------------------------
    # End Nodes
    # -------------------------

    builder.add_edge("admission", END)

    builder.add_edge("hostel", END)

    builder.add_edge("placement", END)

    builder.add_edge("academic", END)

    builder.add_edge("memory", END)

    builder.add_edge("profile", END)

    builder.add_edge("general", END)

    return builder.compile(
        checkpointer=memory
    )
