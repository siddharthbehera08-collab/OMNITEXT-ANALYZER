from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from dotenv import load_dotenv
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

load_dotenv()

app = FastAPI()

class SummaryRequest(BaseModel):
    text: str

# Mount the frontend directory to serve static assets
# Ensure the directory exists or this will fail on startup. 
# We created it, so it should be fine.
app.mount("/static", StaticFiles(directory="../frontend"), name="static")

@app.get("/")
def read_root():
    # Serve the index.html file directly for the root path
    return FileResponse("../frontend/index.html")

@app.post("/summarize")
def summarize_text(request: SummaryRequest):
    # TODO: Integration with 'Antigravity' (e.g., Gemini) model
    # For now, we will return a mock summary or use a library if configured
    
    api_key = os.getenv("AI_API_KEY")
    if not api_key:
        # Mock response for demonstration
        return {
            "summary": f"This is a simulated summary of the input text: {request.text[:50]}...",
            "model": "Simulated Antigravity Model"
        }
    
    # Placeholder for actual API call, uncomment to use if API key is present
    # import google.generativeai as genai
    # genai.configure(api_key=api_key)
    # model = genai.GenerativeModel('gemini-pro')
    # response = model.generate_content(f"Summarize this: {request.text}")
    # return {"summary": response.text}
