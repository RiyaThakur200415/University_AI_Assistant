def agent_router(state):
    """
    Routes the query to the appropriate agent
    based on the category assigned by the classifier.
    """

    category = state.get("query_category", "general")

    valid_categories = {
        "admission",
        "hostel",
        "placement",
        "academic",
        "memory",
        "profile",
        "general",
    }

    if category not in valid_categories:
        return "general"

    return category