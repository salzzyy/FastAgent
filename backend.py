# Uncomment this if you're not using pipenv
# from dotenv import load_dotenv
# load_dotenv()

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from ai_agent import get_response_from_ai_agent

# Allowed AI models
ALLOWED_MODEL_NAMES = {
    "llama3-70b-8192",
    "mixtral-8x7b-32768",
    "llama-3.3-70b-versatile",
    "gpt-4o-mini",
}


# Request schema
class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool


# Initialize FastAPI app
app = FastAPI(title="LangGraph AI Agent")

# Add CORS middleware (optional but useful for frontend integration)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/chat")
def chat_endpoint(request: RequestState):
    """
    API Endpoint to interact with the AI Agent using LangGraph and search tools.
    It dynamically selects the AI model specified in the request.
    """
    if request.model_name not in ALLOWED_MODEL_NAMES:
        raise HTTPException(
            status_code=400,
            detail="Invalid model name. Please choose a supported AI model.",
        )

    # Extract request parameters
    response = get_response_from_ai_agent(
        llm_id=request.model_name,
        query=request.messages,
        allow_search=request.allow_search,
        system_prompt=request.system_prompt,
        provider=request.model_provider,
    )

    return {"response": response}


# Run app & expose Swagger UI docs
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=10000)
