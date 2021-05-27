import requests
from bs4 import BeautifulSoup
import telebot
import feedparser

URL = 'https://pg11.ru/articles/list'

HEADERS = {
    # user-agent нужен чтобы сайт не посчитал нас ботами
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 YaBrowser/21.3.2.193 Yowser/2.5 Safari/537.36'

}
HOST = 'https://pg11.ru'

bot = telebot.TeleBot("1644586994:AAGtW78FVpmDscoiV-ZRWAXNvFLrJ-aKjbo")  # апи бота


# функция для получения html кода
def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


class Newser:
    def Local_news(self, message):
        loc_news = []

        def get_content(html):
            soup = BeautifulSoup(html, 'html.parser')
            # тут мы вытаскиваем знаения которые нам нужны
            items = soup.find_all('div', class_='article-list__item-left')

            # список куда мы будем добавлять наши словари
            for item in items:
                loc_news.append({
                    HOST + item.find('a', class_='article-list__item-image linked-box').get('href')

                })
            # print(loc_news)
            for l_news in range(len(loc_news)):
                if l_news <= 9:
                    bot.send_message(message.chat.id, loc_news[l_news])

        def local_news_parse():
            html = get_html(URL)
            get_content(html.text)

        local_news_parse()

    def All_news(self, message):
        #  функция для извлечения RSS-каналов
        def parseRSS(rss_url):
            return feedparser.parse(rss_url)

        #  функция предназначена для захвата заголовка и ссылки RSS-канала
        #  и возвращает в виде списка
        def getHeadlines(rss_url):
            headlines = []

            feed = parseRSS(rss_url)
            for newsitem in feed['items']:
                # headlines.append(newsitem['title'])
                headlines.append(newsitem['link'])
                # headlines.append(newsitem['id'])
                # headlines.append(newsitem['summary'])
                # headlines.append(newsitem['published'])

            return headlines

        allheadlines = []

        newsurls = {
            'googlenews': 'https://news.google.com/rss?hl=ru&gl=RU&ceid=RU:ru',  # сайт с новостями
        }

        # Здесь мы перебираем URL-адреса каналов и вызываем getHeadlines (),
        # чтобы объединить возвращенные заголовки со всеми заголовками
        for key, url in newsurls.items():
            allheadlines.extend(getHeadlines(url))

        # здесь мы повторяем список allheadlines и отправляем каждый заголовок нашему боту в TG
        for hl in range(len(allheadlines)):
            if hl <= 9:
                bot.send_message(message.chat.id, allheadlines[hl])
                if hl == 9:
                    bot.send_message(message.chat.id, "ещё больше новостей тут!!! 'https://news.google.com/topstories?hl=ru&gl=RU&ceid=RU:ru'")


