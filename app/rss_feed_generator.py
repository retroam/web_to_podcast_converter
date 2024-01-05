from feedgen.feed import FeedGenerator

class RSSFeedGenerator:
    @staticmethod 
    def generate_feed(title, link, description, audio_url):
        fg = FeedGenerator()
        fg.id(link)
        fg.title(title)
        fg.link(href=link,rel='alternate')
        fg.description(description)

        fe = fg.add_entry()
        fe.title(title)
        fe.link(href=audio_url)
        fe.description(description)

        rss_feed = fg.rss_str(pretty=True)
        return rss_feed