from langchain_core.messages import AIMessage


def general_agent(state):

    question = state["messages"][-1].content.lower().strip()

    # -------------------------------
    # Greetings
    # -------------------------------

    if any(word in question for word in [
        "hi",
        "hello",
        "hey",
        "good morning",
        "good afternoon",
        "good evening"
    ]):

        answer = (
            "👋 Hello!\n\n"
            "Welcome to the **University AI Assistant**.\n\n"
            "I can help you with:\n\n"
            "📘 Admission\n"
            "🏠 Hostel\n"
            "🎓 Academics\n"
            "💼 Placements\n"
            "🧠 Remembering your details\n\n"
            "How can I assist you today?"
        )

    # -------------------------------
    # Thank You
    # -------------------------------

    elif any(word in question for word in [
        "thank",
        "thanks",
        "thankyou",
        "thank you"
    ]):

        answer = (
            "😊 You're most welcome!\n\n"
            "I'm glad I could help.\n\n"
            "If you have any more questions about admissions, hostels, academics, or placements, feel free to ask."
        )

    # -------------------------------
    # Goodbye
    # -------------------------------

    elif any(word in question for word in [
        "bye",
        "goodbye",
        "see you",
        "see ya"
    ]):

        answer = (
            "👋 Goodbye!\n\n"
            "It was nice chatting with you.\n\n"
            "Have a wonderful day and best of luck with your studies! 🎓"
        )

    # -------------------------------
    # Appreciation
    # -------------------------------

    elif any(word in question for word in [
        "awesome",
        "great",
        "nice",
        "cool",
        "good job",
        "excellent"
    ]):

        answer = (
            "😄 Thank you! That means a lot.\n\n"
            "I'm always here whenever you need help."
        )

    # -------------------------------
    # Okay / Fine
    # -------------------------------

    elif any(word in question for word in [
        "ok",
        "okay",
        "okk",
        "okkk",
        "fine",
        "alright"
    ]):

        answer = (
            "👍 Great!\n\n"
            "Let me know if you have any other university-related questions."
        )

    # -------------------------------
    # Default
    # -------------------------------

    else:

        answer = (
            "😊 I'm here to help with university-related queries.\n\n"
            "You can ask me about:\n\n"
            "• Admissions\n"
            "• Hostel\n"
            "• Academics\n"
            "• Placements\n"
            "• Your saved profile information"
        )

    return {
        **state,
        "messages": [
            AIMessage(content=answer)
        ]
    }