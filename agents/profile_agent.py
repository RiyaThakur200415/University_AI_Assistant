from langchain_core.messages import AIMessage


def profile_agent(state):

    name = state.get("student_name")
    reg = state.get("register_no")
    dept = state.get("department")

    response = []

    # Greeting
    if name:
        response.append(f"Hello, {name}! 👋")
        response.append("Nice to meet you.")
        response.append("I'll remember your name during this conversation. 😊")

    # Register Number
    if reg:
        response.append(f"✅ I've saved your register number: {reg}")

    # Department
    if dept:
        response.append(f"🎓 I'll remember that you're from the {dept} department.")

    # Nothing extracted
    if not response:
        response.append("Your information has been updated successfully.")

    return {
        **state,
        "messages": [
            AIMessage(
                content="\n\n".join(response)
            )
        ]
    }