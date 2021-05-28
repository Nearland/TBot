import unittest
import feedparser


def parseRSS(rss_url):
    return feedparser.parse(rss_url)


def getHeadlines(rss_url, headlines=[]):

    feed = parseRSS(rss_url)
    for newsitem in feed['items']:
        headlines.append(newsitem['title'])

    return headlines


allheadlines = []

newsurls = {

    'googlenews': 'https://news.google.com/rss?hl=ru&gl=RU&ceid=RU:ru',

}


class TestHedLines(unittest.TestCase):
    def test_hedLines(self):
        self.assertTrue(getHeadlines(rss_url="https://news.google.com/rss?hl=ru&gl=RU&ceid=RU:ru", headlines=[])) # тест на содержание заголовков новостей


class TestRssParse(unittest.TestCase):
    def test_rssParse(self):
        self.assertTrue(parseRSS(
            rss_url="https://news.google.com/rss?hl=ru&gl=RU&ceid=RU:ru"))  # тест на проверку правильности rss-url адреса


if __name__ == "__main__":
    unittest.main()
