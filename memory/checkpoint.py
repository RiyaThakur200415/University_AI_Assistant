# Creating the DataBase

from langgraph.checkpoint.sqlite import SqliteSaver
from contextlib import ExitStack
DB_PATH = "university_chatbot.db"         # Database Name

# Creating the object

_stack = ExitStack()             # We usually create variables starting with underscore when that variable is temporay and is not used. It is used for the internal private words inside the file, i.e., its a private internal variable.

# Creating the memory

memory = _stack.enter_context(                             # This will firstly build the connection between the sqllite package with the hepl of conn function.
    SqliteSaver.from_conn_string(DB_PATH)
)
