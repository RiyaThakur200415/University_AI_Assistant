import re


def extract_profile(state):

    message = state["messages"][-1].content

    lower_msg = message.lower()

    # ----------------------------
    # Extract Name
    # ----------------------------

    name_patterns = [
        r"my name is ([a-zA-Z ]+)",
        r"i am ([a-zA-Z ]+)",
        r"i'm ([a-zA-Z ]+)"
    ]

    for pattern in name_patterns:

        match = re.search(pattern, lower_msg)

        if match:

            name = match.group(1).strip().title()

            state["student_name"] = name

            break

    # ----------------------------
    # Extract Register Number
    # ----------------------------

    reg_patterns = [
        r"register number is ([a-zA-Z0-9]+)",
        r"registration number is ([a-zA-Z0-9]+)",
        r"reg(?:ister)? no\.? is ([a-zA-Z0-9]+)",
        r"reg(?:ister)? number is ([a-zA-Z0-9]+)"
    ]

    for pattern in reg_patterns:

        match = re.search(pattern, lower_msg)

        if match:

            state["register_no"] = match.group(1).upper()

            break

    # ----------------------------
    # Extract Department
    # ----------------------------

    departments = [

        "cse",
        "ece",
        "eee",
        "civil",
        "mechanical",
        "ai",
        "ai&ds",
        "aids",
        "it",
        "csbs"

    ]

    for dept in departments:

        if f"from {dept}" in lower_msg:

            state["department"] = dept.upper()

            break

        if f"department is {dept}" in lower_msg:

            state["department"] = dept.upper()

            break

    return state                          







# We will be converting json to dictionary cause state uses dictionary format to get itself updated.