from utils.llm import llm
from langchain_core.messages import SystemMessage
from knowledge_base.acdemic_kb import ACADEMIC_KB


def acdemic_agent(state):

    context = "\n".join(ACADEMIC_KB.values())

    messages = [
        SystemMessage(
            content=f"""
You are the Academic Officer.

Answer ONLY academic questions.

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