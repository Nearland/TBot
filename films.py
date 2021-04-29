import requests
from bs4 import BeautifulSoup

URL = 'https://www.ivi.ru/new/movie-new'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 YaBrowser/21.3.2.193 Yowser/2.5 Safari/537.36'

}
HOST = 'https://www.ivi.ru'


def mm():
    def get_html(url, params=None):
        r = requests.get(url, headers=HEADERS, params=params)
        return r

    films = []

    def get_content(html):
        soup = BeautifulSoup(html, 'html.parser')

        items = soup.find_all('li', class_='gallery__item gallery__item_virtual')

        for item in items:
            films.append({

                'link': HOST + item.find('a', class_='nbl-slimPosterBlock_type_poster').get('href'),

            })
        print(films)

    def parse():
        html = get_html(URL)
        get_content(html.text)

    parse()

mm()


#
# import requests
# from bs4 import BeautifulSoup
#
# url сайта которого мы хоитм парсить
URL = 'https://www.ivi.ru/new/movie-new'
# заголовки
HEADERS = {
    # user-agent нужен чтобы сайт не посчитал нас ботами
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 YaBrowser/21.3.2.193 Yowser/2.5 Safari/537.36'

}
HOST = 'https://www.ivi.ru'


# функция для получения html кода
def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    # тут мы вытаскиваем знаения которые нам нужны
    items = soup.find_all('li', class_='gallery__item gallery__item_virtual')

    # список куда мы будем добавлять наши словари
    films = []
    for item in items:
        # mark_find = item.find('div', class_='nbl-poster__nbl-ratingCompact')
        # if mark_find:
        #     mark_find.get_text()
        # else:
        #     mark_find = 'нет оценки'

        films.append({
            #'title': item.find('div', class_='nbl-slimPosterBlock__title').get_text(strip=True),
            'link': HOST + item.find('a', class_='nbl-slimPosterBlock_type_poster').get('href'),
            #'janre': item.find('div', class_='nbl-slimPosterBlock__imageSection').
           #     find_next('div',class_='nbl-poster__propertiesRow').
           # get_text(strip=True),

        })
    print(films)
    # print(len(films))


def parse():
    html = get_html(URL)
    get_content(html.text)
    # print(html.text)


parse()
