import requests
from bs4 import BeautifulSoup
import telebot

# url сайта которого мы хоитм парсить
URL_new_films = 'https://www.ivi.ru/new/movie-new'
URL_art_house_films = 'https://www.ivi.ru/movies/arthouse'
URL_boeviki_films = 'https://www.ivi.ru/movies/boeviki'
URL_voennye_films = 'https://www.ivi.ru/movies/voennye'
URL_detective_films = 'https://www.ivi.ru/movies/detective'
URL_drama_films = 'https://www.ivi.ru/movies/drama'
URL_comedy_films = 'https://www.ivi.ru/movies/comedy'
URL_crime_films = 'https://www.ivi.ru/movies/crime'
URL_melodramy_films = 'https://www.ivi.ru/movies/melodramy'
URl_mystic_films = 'https://www.ivi.ru/movies/misticheskie'
URL_adventures_films = 'https://www.ivi.ru/movies/adventures'
URl_thriller_films = 'https://www.ivi.ru/movies/thriller'
URL_horror_films = 'https://www.ivi.ru/movies/horror'
URL_fantastic_films = 'https://www.ivi.ru/movies/fantastika'
URL_fantasy_films = 'https://www.ivi.ru/movies/fentezi'
# заголовки
HEADERS = {
    # user-agent нужен чтобы сайт не посчитал нас ботами
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 YaBrowser/21.3.2.193 Yowser/2.5 Safari/537.36'

}
HOST = 'https://www.ivi.ru'

bot = telebot.TeleBot("1644586994:AAGtW78FVpmDscoiV-ZRWAXNvFLrJ-aKjbo")  # апи бота


# функция для получения html кода
def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


class FILMS:
    def new_films(self, message):
        new_films = []

        def get_content(html):
            soup = BeautifulSoup(html, 'html.parser')
            # тут мы вытаскиваем знаения которые нам нужны
            items = soup.find_all('li', class_='gallery__item gallery__item_virtual')

            # список куда мы будем добавлять наши словари
            for item in items:
                new_films.append({
                    HOST + item.find('a', class_='nbl-slimPosterBlock_type_poster').get('href')

                })
            for movie in range(len(new_films)):
                if movie <= 9:
                    bot.send_message(message.chat.id, new_films[movie])

        def new_films_parse():
            html = get_html(URL_new_films)
            get_content(html.text)

        new_films_parse()

    def art_house(self, message):
        art_house_films = []

        def get_content(html):
            soup = BeautifulSoup(html, 'html.parser')
            # тут мы вытаскиваем знаения которые нам нужны
            items = soup.find_all('li', class_='gallery__item gallery__item_virtual')

            # список куда мы будем добавлять наши словари
            for item in items:
                art_house_films.append({
                    HOST + item.find('a', class_='nbl-slimPosterBlock_type_poster').get('href')

                })
            for movie in range(len(art_house_films)):
                if movie <= 9:
                    bot.send_message(message.chat.id, art_house_films[movie])

        def art_house_parse():
            html = get_html(URL_art_house_films)
            get_content(html.text)

        art_house_parse()

    def boeviki(self, message):
            boeviki_films = []

            def get_content(html):
                soup = BeautifulSoup(html, 'html.parser')
                # тут мы вытаскиваем знаения которые нам нужны
                items = soup.find_all('li', class_='gallery__item gallery__item_virtual')

                # список куда мы будем добавлять наши словари
                for item in items:
                    boeviki_films.append({
                        HOST + item.find('a', class_='nbl-slimPosterBlock_type_poster').get('href')

                    })
                for movie in range(len(boeviki_films)):
                    if movie <= 9:
                        bot.send_message(message.chat.id, boeviki_films[movie])

            def boeviki_parse():
                html = get_html(URL_boeviki_films)
                get_content(html.text)

            boeviki_parse()

    def voennye(self, message):
        voennye_films = []

        def get_content(html):
            soup = BeautifulSoup(html, 'html.parser')
            # тут мы вытаскиваем знаения которые нам нужны
            items = soup.find_all('li', class_='gallery__item gallery__item_virtual')

            # список куда мы будем добавлять наши словари
            for item in items:
                voennye_films.append({
                    HOST + item.find('a', class_='nbl-slimPosterBlock_type_poster').get('href')

                })
            for movie in range(len(voennye_films)):
                if movie <= 9:
                    bot.send_message(message.chat.id, voennye_films[movie])

        def voennye_parse():
            html = get_html(URL_voennye_films)
            get_content(html.text)

        voennye_parse()

    def detective(self, message):
        detective_films = []

        def get_content(html):
            soup = BeautifulSoup(html, 'html.parser')
            # тут мы вытаскиваем знаения которые нам нужны
            items = soup.find_all('li', class_='gallery__item gallery__item_virtual')

            # список куда мы будем добавлять наши словари
            for item in items:
                detective_films.append({
                    HOST + item.find('a', class_='nbl-slimPosterBlock_type_poster').get('href')

                })
            for movie in range(len(detective_films)):
                if movie <= 9:
                    bot.send_message(message.chat.id, detective_films[movie])

        def detective_parse():
            html = get_html(URL_detective_films)
            get_content(html.text)

        detective_parse()

    def drama(self, message):
        drama_films = []

        def get_content(html):
            soup = BeautifulSoup(html, 'html.parser')
            # тут мы вытаскиваем знаения которые нам нужны
            items = soup.find_all('li', class_='gallery__item gallery__item_virtual')

            # список куда мы будем добавлять наши словари
            for item in items:
                drama_films.append({
                    HOST + item.find('a', class_='nbl-slimPosterBlock_type_poster').get('href')

                })
            for movie in range(len(drama_films)):
                if movie <= 9:
                    bot.send_message(message.chat.id, drama_films[movie])

        def drama_parse():
            html = get_html(URL_drama_films)
            get_content(html.text)

        drama_parse()

    def comedy(self, message):
        comedy_films = []

        def get_content(html):
            soup = BeautifulSoup(html, 'html.parser')
            # тут мы вытаскиваем знаения которые нам нужны
            items = soup.find_all('li', class_='gallery__item gallery__item_virtual')

            # список куда мы будем добавлять наши словари
            for item in items:
                comedy_films.append({
                    HOST + item.find('a', class_='nbl-slimPosterBlock_type_poster').get('href')

                })
            for movie in range(len(comedy_films)):
                if movie <= 9:
                    bot.send_message(message.chat.id, comedy_films[movie])

        def comedy_parse():
            html = get_html(URL_comedy_films)
            get_content(html.text)

        comedy_parse()

    def crime(self, message):
        crime_films = []

        def get_content(html):
            soup = BeautifulSoup(html, 'html.parser')
            # тут мы вытаскиваем знаения которые нам нужны
            items = soup.find_all('li', class_='gallery__item gallery__item_virtual')

            # список куда мы будем добавлять наши словари
            for item in items:
                crime_films.append({
                    HOST + item.find('a', class_='nbl-slimPosterBlock_type_poster').get('href')

                })
            for movie in range(len(crime_films)):
                if movie <= 9:
                    bot.send_message(message.chat.id, crime_films[movie])

        def crime_parse():
            html = get_html(URL_crime_films)
            get_content(html.text)

        crime_parse()

    def melodrama(self, message):
        melodrama_films = []

        def get_content(html):
            soup = BeautifulSoup(html, 'html.parser')
            # тут мы вытаскиваем знаения которые нам нужны
            items = soup.find_all('li', class_='gallery__item gallery__item_virtual')

            # список куда мы будем добавлять наши словари
            for item in items:
                melodrama_films.append({
                    HOST + item.find('a', class_='nbl-slimPosterBlock_type_poster').get('href')

                })
            for movie in range(len(melodrama_films)):
                if movie <= 9:
                    bot.send_message(message.chat.id, melodrama_films[movie])

        def melodrama_parse():
            html = get_html(URL_melodramy_films)
            get_content(html.text)

        melodrama_parse()

    def mystic(self, message):
        mystic_films = []

        def get_content(html):
            soup = BeautifulSoup(html, 'html.parser')
            # тут мы вытаскиваем знаения которые нам нужны
            items = soup.find_all('li', class_='gallery__item gallery__item_virtual')

            # список куда мы будем добавлять наши словари
            for item in items:
                mystic_films.append({
                    HOST + item.find('a', class_='nbl-slimPosterBlock_type_poster').get('href')

                })
            for movie in range(len(mystic_films)):
                if movie <= 9:
                    bot.send_message(message.chat.id, mystic_films[movie])

        def mystic_parse():
            html = get_html(URl_mystic_films)
            get_content(html.text)

        mystic_parse()

    def adventure(self, message):
        adventure_films = []

        def get_content(html):
            soup = BeautifulSoup(html, 'html.parser')
            # тут мы вытаскиваем знаения которые нам нужны
            items = soup.find_all('li', class_='gallery__item gallery__item_virtual')

            # список куда мы будем добавлять наши словари
            for item in items:
                adventure_films.append({
                    HOST + item.find('a', class_='nbl-slimPosterBlock_type_poster').get('href')

                })
            for movie in range(len(adventure_films)):
                if movie <= 9:
                    bot.send_message(message.chat.id, adventure_films[movie])

        def adventure_parse():
            html = get_html(URL_adventures_films)
            get_content(html.text)

        adventure_parse()

    def thriller(self, message):
        thriller_films = []

        def get_content(html):
            soup = BeautifulSoup(html, 'html.parser')
            # тут мы вытаскиваем знаения которые нам нужны
            items = soup.find_all('li', class_='gallery__item gallery__item_virtual')

            # список куда мы будем добавлять наши словари
            for item in items:
                thriller_films.append({
                    HOST + item.find('a', class_='nbl-slimPosterBlock_type_poster').get('href')

                })
            for movie in range(len(thriller_films)):
                if movie <= 9:
                    bot.send_message(message.chat.id, thriller_films[movie])

        def thriller_parse():
            html = get_html(URl_thriller_films)
            get_content(html.text)

        thriller_parse()

    def horror(self, message):
        horror_films = []

        def get_content(html):
            soup = BeautifulSoup(html, 'html.parser')
            # тут мы вытаскиваем знаения которые нам нужны
            items = soup.find_all('li', class_='gallery__item gallery__item_virtual')

            # список куда мы будем добавлять наши словари
            for item in items:
                horror_films.append({
                    HOST + item.find('a', class_='nbl-slimPosterBlock_type_poster').get('href')

                })
            for movie in range(len(horror_films)):
                if movie <= 9:
                    bot.send_message(message.chat.id, horror_films[movie])

        def horror_parse():
            html = get_html(URL_horror_films)
            get_content(html.text)

        horror_parse()

    def fantastic(self, message):
        fantastic_films = []

        def get_content(html):
            soup = BeautifulSoup(html, 'html.parser')
            # тут мы вытаскиваем знаения которые нам нужны
            items = soup.find_all('li', class_='gallery__item gallery__item_virtual')

            # список куда мы будем добавлять наши словари
            for item in items:
                fantastic_films.append({
                    HOST + item.find('a', class_='nbl-slimPosterBlock_type_poster').get('href')

                })
            for movie in range(len(fantastic_films)):
                if movie <= 9:
                    bot.send_message(message.chat.id, fantastic_films[movie])

        def fantastic_parse():
            html = get_html(URL_fantastic_films)
            get_content(html.text)

        fantastic_parse()

    def fantasy(self, message):
        fantasy_films = []

        def get_content(html):
            soup = BeautifulSoup(html, 'html.parser')
            # тут мы вытаскиваем знаения которые нам нужны
            items = soup.find_all('li', class_='gallery__item gallery__item_virtual')

            # список куда мы будем добавлять наши словари
            for item in items:
                fantasy_films.append({
                    HOST + item.find('a', class_='nbl-slimPosterBlock_type_poster').get('href')

                })
            for movie in range(len(fantasy_films)):
                if movie <= 9:
                    bot.send_message(message.chat.id, fantasy_films[movie])

        def fantasy_parse():
            html = get_html(URL_fantasy_films)
            get_content(html.text)

        fantasy_parse()
