# This will called the build_graph

from graph.workflow import build_graph
from langchain_core.messages import HumanMessage

graph = build_graph()

# Creating the ThreadID

thread_id = input(
    "Session ID"
).strip() or "student_001"

config = {
    "configurable": {
        "thread_id": thread_id
    }
}

# getting the input for the user

while True:

    query = input("\nYou: ")

    if query.lower() == "quit":
        break
    result = graph.invoke(
        {
            "messages": [
                HumanMessage(content = query)
            ]
        },
        config=config
    )

    # print("\nDEBUG STATE")
    # print(result)

    print(
        "\nAssistant:",
        result["messages"][-1].content
    )

