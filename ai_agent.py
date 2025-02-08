# Step1: Setup API Keys for Groq, OpenAI, and Tavily
# Step2: Setup LLM & Tools
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage
from fastapi import HTTPException

# Preload models (default)
openai_llm = ChatOpenAI(model="gpt-4o-mini")
groq_llm = ChatGroq(model="llama-3.3-70b-versatile")

# Define default system prompt
DEFAULT_SYSTEM_PROMPT = "Act as an AI chatbot who is smart, friendly, and witty."


def get_response_from_ai_agent(
    llm_id: str,
    query: list,
    allow_search: bool,
    system_prompt: str = DEFAULT_SYSTEM_PROMPT,
    provider: str = "OpenAI",
):
    """
    Generates a response from the AI agent using the selected model and provider.

    Args:
        llm_id (str): The model name (e.g., "gpt-4o-mini", "llama-3.3-70b-versatile").
        query (list): A list of messages representing the chat history.
        allow_search (bool): Whether to enable web search.
        system_prompt (str): The prompt guiding the AI agent.
        provider (str): The provider name ("OpenAI" or "Groq").

    Returns:
        str: The AI-generated response.
    """

    # Validate provider
    if provider not in {"Groq", "OpenAI"}:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid provider '{provider}'. Choose 'Groq' or 'OpenAI'.",
        )

    # Initialize the correct LLM model
    try:
        llm = ChatGroq(model=llm_id) if provider == "Groq" else ChatOpenAI(model=llm_id)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error loading model '{llm_id}': {str(e)}"
        )

    # Setup tools if search is allowed
    tools = [TavilySearchResults(max_results=2)] if allow_search else []

    try:
        # Create AI agent
        agent = create_react_agent(model=llm, tools=tools, state_modifier=system_prompt)

        # AI agent execution
        state = {"messages": query}
        response = agent.invoke(state)
        messages = response.get("messages", [])

        # Extract AI's last message
        ai_messages = [
            message.content for message in messages if isinstance(message, AIMessage)
        ]
        return (
            ai_messages[-1]
            if ai_messages
            else "I'm sorry, I couldn't generate a response."
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI agent error: {str(e)}")
