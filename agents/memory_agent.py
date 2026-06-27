from langchain_core.messages import AIMessage

def memory_agent(state):

    name = state.get("student_name")

    if name:
        answer = f"Your name is {name.title()}."

    else:
        answer = "I don't know your name yet."

    return {
    "messages": [
        AIMessage(content=answer)
    ]
}