from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from deep_translator import GoogleTranslator
import uvicorn
from typing import List, Optional

app = FastAPI()

class PageTranslateRequest(BaseModel):
    pageText: List[str]
    targetLang: str
    sourceLang: Optional[str] = "auto"

@app.get("/")
async def index():
    return JSONResponse(content={"text": "server created"})

@app.post("/translate-page")
async def translate(data: PageTranslateRequest):
    translated_list = []

    for p in data.pageText:
        if p.strip():
            translated = GoogleTranslator(
                source=data.sourceLang,
                target=data.targetLang
            ).translate(p)
            translated_list.append(translated)
        else:
            translated_list.append("")

    return {"translated": translated_list}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
