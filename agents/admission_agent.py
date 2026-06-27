from utils.llm import llm
from langchain_core.messages import SystemMessage
from knowledge_base.admission_kb import ADMISSION_KB


def admission_agent(state):

    context = "\n".join(ADMISSION_KB.values())

    messages = [
        SystemMessage(
            content=f"""
You are the University Admission Officer.

Answer ONLY admission-related questions.

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