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

@app.post("/convert/")
def convert(url: str = Form(...)):
    # Convert URL to audio
    audio_file = WebToPodcastConverter.convert(url)

    # Generate RSS feed
    rss_feed = RSSFeedGenerator.generate_feed(
        title='Podcast Title',
        link=url,
        description='Podcast Description',
        audio_url=f'http://yourdomain.com/{audio_file}'
    )

    return templates.TemplateResponse("result.html", {"request": "result", "audio_file": audio_file, "rss_feed": rss_feed})

@app.get("/download/{filename}")
def download(filename: str):
    return FileResponse(f"./{filename}", media_type='audio/mp3')
