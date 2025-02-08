# Uncomment if not using pipenv
# from dotenv import load_dotenv
# load_dotenv()

# Step 1: Setup UI with Streamlit
import streamlit as st
import requests

st.set_page_config(page_title="LangGraph Agent UI", layout="centered")
st.title("🤖 AI Chatbot Agents")
st.write("Create and Interact with AI Agents powered by LangGraph!")

# System Prompt Input
system_prompt = st.text_area(
    "📝 Define your AI Agent:", height=70, placeholder="Type your system prompt here..."
)

# Model Selection
MODEL_NAMES_GROQ = ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]
MODEL_NAMES_OPENAI = ["gpt-4o-mini"]

provider = st.radio("🔹 Select AI Provider:", ("Groq", "OpenAI"), horizontal=True)

if provider == "Groq":
    selected_model = st.selectbox("🔍 Select Groq Model:", MODEL_NAMES_GROQ)
else:
    selected_model = st.selectbox("🔍 Select OpenAI Model:", MODEL_NAMES_OPENAI)

# Additional Options
allow_web_search = st.checkbox("🌐 Allow Web Search")

# User Query
user_query = st.text_area(
    "💬 Enter your query:", height=150, placeholder="Ask anything!"
)

# API URL
API_URL = "https://fastagent.onrender.com/chat"


# Step 2: Connect with Backend via API
if st.button("🚀 Ask Agent!"):
    if not user_query.strip():
        st.warning("⚠️ Please enter a query before submitting.")
    else:
        payload = {
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt.strip(),
            "messages": [user_query.strip()],
            "allow_search": allow_web_search,
        }

        try:
            response = requests.post(API_URL, json=payload)

            if response.status_code == 200:
                response_data = response.json()
                if "error" in response_data:
                    st.error(f"❌ Error: {response_data['error']}")
                else:
                    st.subheader("🧠 Agent Response")
                    st.success(f"**Final Response:**\n{response_data}")
            else:
                st.error(f"❌ API Error: {response.status_code} - {response.text}")

        except requests.exceptions.RequestException as e:
            st.error(f"⚠️ Connection Error: {str(e)}")
