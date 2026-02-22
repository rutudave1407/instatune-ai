from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from typing import List, Optional
from PIL import Image
import io

from recommender import BollywoodRecommender

app = FastAPI()
model = BollywoodRecommender()


@app.post("/recommend")
async def recommend_song(
    images: List[UploadFile] = File(...),
    keywords: Optional[str] = Form(None),
    prompt: Optional[str] = Form(None),
    duration: int = Form(10),
):
    # ✅ Backend validation
    if len(images) == 0:
        raise HTTPException(status_code=400, detail="At least one image is required.")

    if len(images) > 5:
        raise HTTPException(
            status_code=400,
            detail="Maximum 5 images allowed."
        )

    pil_images = []

    for file in images:
        content = await file.read()
        image = Image.open(io.BytesIO(content)).convert("RGB")
        pil_images.append(image)

    keyword_list = keywords.split(",") if keywords else []

    result = model.recommend(
        pil_images,
        keyword_list,
        prompt,
        duration,
    )

    return result