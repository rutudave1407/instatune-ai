import os, json, io
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from PIL import Image
import google.generativeai as genai
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# 2026 Model: Using the latest stable Gemini 3 Flash
GENAI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GENAI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

genai.configure(api_key=GENAI_API_KEY)
model = genai.GenerativeModel('gemini-3-flash-preview') 

class SongResponse(BaseModel):
    song_name: str
    vibe_analysis: str
    lyrics: str
    suggested_segment: str # Feature: Part of the song that fits the duration

@app.post("/suggest-song", response_model=SongResponse)
async def suggest_song(
    keywords: str = Form(""),
    user_context: str = Form(""),
    duration: str = Form("15 sec"), # New duration parameter
    files: List[UploadFile] = File(...)
):
    if len(files) > 5:
        raise HTTPException(status_code=400, detail="Max 5 images allowed.")

    try:
        images = [Image.open(io.BytesIO(await f.read())) for f in files]
        
        # Enhanced prompt for actual Bollywood song retrieval
        prompt = f"""
        Act as a Bollywood cinema expert. Suggest one REAL released Bollywood song.
        Vibe Keywords: {keywords}
        Additional Context: {user_context}
        Target Video Duration: {duration}
        
        STRICT OUTPUT RULES:
        1. Only suggest actual released songs (no AI-generated lyrics).
        2. Identify the specific part of the song (e.g., 'Chorus' or 'Bridge') that fits the {duration} duration.
        3. Response must be RAW JSON: {{"song_name": "", "vibe_analysis": "", "lyrics": "", "suggested_segment": ""}}
        """

        response = model.generate_content([prompt] + images)
        clean_text = response.text.strip().replace('```json', '').replace('```', '')
        return json.loads(clean_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))