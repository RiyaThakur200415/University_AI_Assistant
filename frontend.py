import streamlit as st
from graph.workflow import build_graph
from langchain_core.messages import HumanMessage

# ------------------------------
# PAGE CONFIG
# ------------------------------

st.set_page_config(
    page_title="University AI Assistant",
    page_icon="🎓",
    layout="wide"
)

# ------------------------------
# CSS
# ------------------------------

st.markdown("""
<style>

.main{
    background-color:#f6f8fc;
}

.block-container{
    padding-top:2rem;
}

[data-testid="stSidebar"]{
    background:#14213d;
}

[data-testid="stSidebar"] *{
    color:white;
}

</style>
""", unsafe_allow_html=True)

# ------------------------------
# LOAD GRAPH
# ------------------------------

graph = build_graph()

# ------------------------------
# SESSION STATE
# ------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "thread_id" not in st.session_state:
    st.session_state.thread_id = "student001"

# ------------------------------
# SIDEBAR
# ------------------------------

with st.sidebar:

    st.title("🎓 University AI")

    st.markdown("---")

    st.session_state.thread_id = st.text_input(
        "Session ID",
        value=st.session_state.thread_id
    )

    st.markdown("---")

    st.subheader("Services")

    st.write("📘 Admission")

    st.write("🏠 Hostel")

    st.write("🎓 Academic")

    st.write("💼 Placement")

    st.write("🧠 Memory")

    st.markdown("---")

    if st.button("Clear Chat"):

        st.session_state.messages = []

        st.rerun()

# ------------------------------
# HEADER
# ------------------------------

st.title("🎓 University AI Assistant")

st.caption("Powered by LangGraph + Ollama + SQLite Memory")

st.divider()

# ------------------------------
# CHAT HISTORY
# ------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# ------------------------------
# USER INPUT
# ------------------------------

question = st.chat_input("Ask your question...")

if question:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":question
        }
    )

    with st.chat_message("user"):

        st.markdown(question)

    config = {
        "configurable":{
            "thread_id":st.session_state.thread_id
        }
    }

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            result = graph.invoke(
                {
                    "messages":[
                        HumanMessage(content=question)
                    ]
                },
                config=config
            )

            answer = result["messages"][-1].content

            st.markdown(answer)

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":answer
        }
    )