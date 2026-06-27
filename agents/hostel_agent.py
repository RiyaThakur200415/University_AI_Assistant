from utils.llm import llm
from langchain_core.messages import SystemMessage
from knowledge_base.hostel_kb import HOSTEL_KB


def hostel_agent(state):

    context = "\n".join(HOSTEL_KB.values())

    messages = [
        SystemMessage(
            content=f"""
You are Hostel Management Officer.

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
    

    