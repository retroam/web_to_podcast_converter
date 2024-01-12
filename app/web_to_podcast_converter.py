from .article_extractor import ArticleExtractor
from .summarizer import Summarizer
from .audio_generator import AudioGenerator
from .rss_feed_generator import RSSFeedGenerator

class WebToPodcastConverter:
    @staticmethod
    def convert(url):
        content = ArticleExtractor.extract_content(url)
        summary = Summarizer.summarize(content)
        audio_file = AudioGenerator.generate_audio(summary)
        return audio_file