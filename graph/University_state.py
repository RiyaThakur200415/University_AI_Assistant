from langgraph.graph.message import add_messages
from typing import TypedDict , Annotated , Optional       # Here we are using optional cause in this we don't know anything about the user.

class UniversityState(TypedDict):
    messages:Annotated[list , add_messages]

    student_name:Optional[str]      # Initially we won't be knowing what's the name of the student and any of the details.
    register_no:Optional[str]
    department:Optional[str]
    
    query_category: str
    kb_context:str
    



# Why are we using optional in python?
# Because initially we don't know the name of the student or any orther details of the student. Thus, to make sure when we run the code it should not throw any error cause initially the values for the fields will be null.