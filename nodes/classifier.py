from utils.llm import llm
import re


def classify_query(state):

    question = state["messages"][-1].content.lower()

    # -------------------------
    # PROFILE
    # -------------------------

    if (
        re.search(r"\bmy name is\b", question)
        or re.search(r"\bi am\b", question)
        or re.search(r"\bi'm\b", question)
        or "register number" in question
        or "registration number" in question
        or "department" in question
    ):
        state["query_category"] = "profile"
        return state

    # -------------------------
    # MEMORY
    # -------------------------

    memory_keywords = [
        "what is my name",
        "who am i",
        "remember me",
        "my register number",
        "what do you know about me",
        "my department"
    ]

    if any(k in question for k in memory_keywords):
        state["query_category"] = "memory"
        return state

    # -------------------------
    # HOSTEL
    # -------------------------

    hostel_keywords = [
        "hostel",
        "room",
        "rooms",
        "mess",
        "curfew",
        "wifi",
        "laundry",
        "gym",
        "medical",
        "vacancy",
        "available",
        "availability"
    ]

    if any(k in question for k in hostel_keywords):
        state["query_category"] = "hostel"
        return state

    # -------------------------
    # ADMISSION
    # -------------------------

    admission_keywords = [
        "admission",
        "fees",
        "fee",
        "eligibility",
        "apply",
        "application",
        "vit",
        "viteee",
        "course",
        "courses"
    ]

    if any(k in question for k in admission_keywords):
        state["query_category"] = "admission"
        return state

    # -------------------------
    # PLACEMENT
    # -------------------------

    placement_keywords = [
        "placement",
        "package",
        "salary",
        "company",
        "companies",
        "internship",
        "recruitment"
    ]

    if any(k in question for k in placement_keywords):
        state["query_category"] = "placement"
        return state

    # -------------------------
    # ACADEMIC
    # -------------------------

    academic_keywords = [
        "attendance",
        "semester",
        "credits",
        "cgpa",
        "gpa",
        "grading",
        "backlog",
        "exam"
    ]

    if any(k in question for k in academic_keywords):
        state["query_category"] = "academic"
        return state

    # -------------------------
    # GENERAL
    # -------------------------

    general_keywords = [
        "hello",
        "hi",
        "hey",
        "thanks",
        "thank",
        "bye",
        "good morning",
        "good evening"
    ]

    if any(k in question for k in general_keywords):
        state["query_category"] = "general"
        return state

    # -------------------------
    # LLM FALLBACK
    # -------------------------

    prompt = f"""
Classify this question into ONE category.

Categories:
admission
hostel
placement
academic
memory
profile
general

Return ONLY one word.

Question:
{question}
"""

    result = llm.invoke(prompt)

    category = result.content.strip().lower()

    valid = [
        "admission",
        "hostel",
        "placement",
        "academic",
        "memory",
        "profile",
        "general"
    ]

    if category not in valid:
        category = "general"

    state["query_category"] = category

    return state