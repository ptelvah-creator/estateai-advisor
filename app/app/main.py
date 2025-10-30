from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "google_maps_api_key": os.getenv("GOOGLE_MAPS_API_KEY", "")
    })

@app.get("/healthz")
async def healthz():
    return {"status": "ok"}