from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from app.web_to_podcast_converter import WebToPodcastConverter
from app.rss_feed_generator import RSSFeedGenerator

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")

@app.get("/")
def read_form():
    return templates.TemplateResponse("index.html", {"request": "form"})