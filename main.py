from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from googletrans import Translator
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
    translator = Translator()

    translated_list = []
    for p in data.pageText:
        if p.strip():
            translated_text = translator.translate(p, src=data.sourceLang, dest=data.targetLang).text
            translated_list.append(translated_text)
        else:
            translated_list.append("")

    print("Translated List:", translated_list)
    return JSONResponse(content={"translated": translated_list})

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
