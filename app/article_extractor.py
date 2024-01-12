import requests
from bs4 import BeautifulSoup

class ArticleExtractor:
    @staticmethod
    def extract_content(url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.final_all('p')
        content = ' '.join([p.get_text() for p in paragraphs])
        return content