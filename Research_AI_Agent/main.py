import streamlit as st
from langchain_setup import process_query

# Streamlit Page Config
st.set_page_config(page_title="AI Assistant", layout="wide")

# App Header
st.title("🧠 Deep-Research-AI-Agentic-System")
st.write("Enter a question, and the AI system will research and draft a response.")

with st.sidebar:
    st.header("ℹ️ How to Use")
    st.write("💡 Ask the agent on research topics to generate")
    st.write("📝 Your conversation research topics is saved in this session.")
    st.write("🔄 Refreshing will clear the chat history.")

st.sidebar.markdown("<br>" * 8, unsafe_allow_html=True)  # Push contact details lower

# Sidebar for Contact Details
st.sidebar.title("📞 Contact Details")
st.sidebar.write("**Support Email:** support@example.com")
st.sidebar.write("**Helpline:** +1-800-123-4567")
st.sidebar.write("**Website:** [Visit Us](https://www.example.com)")



# User Input
user_input = st.text_area("Enter your query:", placeholder="Type something...", height=100)


if st.button("Submit"):
    if user_input.strip():
        with st.spinner("Processing..."):
            response_text = process_query(user_input)  # Get processed text
        st.subheader("Response:")
        st.write(response_text)  # Display the extracted response
    else:
        st.warning("Please enter a query before submitting.")

