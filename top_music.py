import requests
from bs4 import BeautifulSoup

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 YaBrowser/21.3.2.193 Yowser/2.5 Safari/537.36'

}
URL = 'https://hitmo.me/songs/top-today'
Host = 'https://ruv.hotmo.org'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


list_songs = []


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')

    songs = soup.find_all('li', class_='tracks__item track mustoggler')

    for song in songs:
        list_songs.append({
            #'title': song.find('div', class_='track__title').get_text(strip=True),
            #'singer': song.find('div', class_='track__desc').get_text(strip=True),
            'link': Host + song.find('a', class_='track__info-l').get('href')

        })
    #print(list_songs)


def parse():
    html = get_html(URL)
    get_content(html.text)


parse()
