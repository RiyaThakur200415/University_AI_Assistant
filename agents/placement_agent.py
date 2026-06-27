from utils.llm import llm
from langchain_core.messages import SystemMessage
from knowledge_base.placement_kb import PLACEMENT_KB


def placement_agent(state):

    context = "\n".join(PLACEMENT_KB.values())

    messages = [
        SystemMessage(
            content=f"""
You are Placement Officer.

Knowledge Base:

{context}
"""
        ),
        *state["messages"]
    ]

    result = llm.invoke(messages)

    return {
        "messages": [result]
    }