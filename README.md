# 🌐 **AI Chatbot Agent – Project Setup Guide**
🔗 **Live Demo**: [AI Chatbot App](https://deepretrive-hjojxkskkm9pqxfsbpvrsv.streamlit.app/)  

---

## 📝 **About the Project**  
This project is an **AI-powered chatbot** built using **LangGraph**, **FastAPI**, and **Streamlit**. It allows users to interact with AI models from **Groq** and **OpenAI**, with an optional **web search** functionality for enhanced responses.  

### 🔹 **Tech Stack**  
✅ **Frontend**: Streamlit (for UI)  
✅ **Backend**: FastAPI (for API handling)  
✅ **LLMs**: OpenAI (GPT-4o-mini), Groq (Llama-3.3-70B, Mixtral)  
✅ **Search**: Tavily Search API (for web-enhanced AI responses)  

### 🛠 **How It Works**  
1️⃣ **Select AI Model** – Choose between Groq and OpenAI.  
2️⃣ **Enter Query** – The chatbot processes user input with **LLMs** and **web search (optional)**.  
3️⃣ **Get Smart AI Responses** – The agent responds with intelligence, wit, and precision.  

---

## 📌 **Table of Contents**  
1️⃣ [Setting Up a Python Virtual Environment](#setting-up-a-python-virtual-environment)  
   - [Using Pipenv](#using-pipenv)  
   - [Using pip and venv](#using-pip-and-venv)  
   - [Using Conda](#using-conda)  
2️⃣ [Running the Application](#running-the-application)  

---

## ⚙️ **Setting Up a Python Virtual Environment**  

### **1️⃣ Using Pipenv**  
🔹 **Install Pipenv (if not installed):**  
```bash
pip install pipenv

🔹 Install Dependencies:

```bash
pipenv install
```

🔹 **Activate the Virtual Environment:**


```bash
pipenv shell
```

### **2️⃣ Using pip and venv**
**🔹 Create a Virtual Environment:**

```bash

python -m venv venv
```

**🔹 Activate the Virtual Environment:**
For macOS/Linux:

```bash
source venv/bin/activate
```
For Windows:

```bash
venv\Scripts\activate
```
**🔹 Install Dependencies:**

```bash
pip install -r requirements.txt
```

**3️⃣ Using Conda**
**🔹 Create a Conda Environment:**

```bash

conda create --name myenv python=3.11
```
**🔹 Activate the Conda Environment:**

```bash
conda activate myenv
```
**🔹 Install Dependencies:**

```bash
pip install -r requirements.txt
```

**🚀 Running the Application**
**🔹 Phase 1: Run AI Agent**
```bash
python ai_agent.py
```
**🔹 Phase 2: Start the Backend (FastAPI)**
```bash
python backend.py
```
**🔹 Phase 3: Start the Frontend (Streamlit)**
```bash
streamlit run frontend.py
```

✅ Make sure the backend is running before starting the frontend!
🎯 Final Steps – Deployment
1️⃣ Deploy Backend on Render
Push your FastAPI backend.py to GitHub.
Go to Render and create a new Web Service.
Connect your GitHub repo, select Python as the runtime, and set backend.py as the entry file.
Deploy and copy the Backend URL (e.g., https://your-backend.onrender.com).
2️⃣ Deploy Frontend on Streamlit Cloud
Push your frontend.py file to GitHub.
Go to Streamlit Cloud and create a new app.
Connect your GitHub repo and select frontend.py as the main file.
Deploy and get your Live App URL.
🚀 Your AI Chatbot is Now Live! Enjoy! 🎉
```vbnet


This `.md` file is **well-structured, visually appealing, and easy to follow**. 🚀 Let me know if you want any modifications! 🎯

```





