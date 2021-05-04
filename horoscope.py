import requests
from bs4 import BeautifulSoup
import telebot

#  URL сайта которого мы хоитм парсить
URL_today_gemini = 'https://horo.mail.ru/prediction/gemini/today/'
URL_tomorrow_gemini = 'https://horo.mail.ru/prediction/gemini/tomorrow/'
URL_today_cancer = 'https://horo.mail.ru/prediction/cancer/today/'
URL_tomorrow_cancer = 'https://horo.mail.ru/prediction/cancer/tomorrow/'
URL_today_capricorn = 'https://horo.mail.ru/prediction/capricorn/today/'
URL_tomorrow_capricorn = 'https://horo.mail.ru/prediction/capricorn/tomorrow/'
URL_today_virgo = 'https://horo.mail.ru/prediction/virgo/today/'
URL_tomorrow_virgo = 'https://horo.mail.ru/prediction/virgo/tomorrow/'
URL_today_aquarius = 'https://horo.mail.ru/prediction/aquarius/today/'
URL_tomorrow_aquarius = 'https://horo.mail.ru/prediction/aquarius/tomorrow/'
URL_today_taurus = 'https://horo.mail.ru/prediction/taurus/today/'
URL_tomorrow_taurus = 'https://horo.mail.ru/prediction/taurus/tomorrow/'
URL_today_leo = 'https://horo.mail.ru/prediction/leo/today/'
URL_tomorrow_leo = 'https://horo.mail.ru/prediction/leo/tomorrow/'
URl_today_aries = 'https://horo.mail.ru/prediction/aries/today/'
URl_tomorrow_aries = 'https://horo.mail.ru/prediction/aries/tomorrow/'
URL_today_pisces = 'https://horo.mail.ru/prediction/pisces/today/'
URL_tomorrow_pisces = 'https://horo.mail.ru/prediction/pisces/tomorrow/'
URL_today_sagittarius = 'https://horo.mail.ru/prediction/sagittarius/today/'
URL_tomorrow_sagittarius = 'https://horo.mail.ru/prediction/sagittarius/tomorrow/'
URL_today_libra = 'https://horo.mail.ru/prediction/libra/today/'
URL_tomorrow_libra = 'https://horo.mail.ru/prediction/libra/tomorrow/'
URL_today_scorpio = 'https://horo.mail.ru/prediction/scorpio/today/'
URL_tomorrow_scorpio = 'https://horo.mail.ru/prediction/scorpio/tomorrow/'

bot = telebot.TeleBot("1644586994:AAGtW78FVpmDscoiV-ZRWAXNvFLrJ-aKjbo")  # апи бота

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 YaBrowser/21.3.2.193 Yowser/2.5 Safari/537.36'
}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


class HOROSCOPE:
    # БЛИЗНЕЦЫ GEMINI
    def gemini(self, message):
        # списки для хранения информации
        horoscope_today_gemini = []
        horoscope_tomorrow_gemini = []

        def get_content_today(html):
            soup = BeautifulSoup(html, 'html.parser')

            items = soup.find_all('div', class_='article__text')

            for item in items:
                horoscope_today_gemini.append({
                    item.find('div', class_='article__item article__item_alignment_left '
                                            'article__item_html').get_text(strip=True)
                })
            bot.send_message(message.chat.id, "Гороскоп на сегодня.")
            bot.send_message(message.chat.id, horoscope_today_gemini)

        def get_content_tomorrow(html):
            soup = BeautifulSoup(html, 'html.parser')

            items = soup.find_all('div', class_='article__text')

            for item in items:
                horoscope_tomorrow_gemini.append({
                    item.find('div', class_='article__item article__item_alignment_left '
                                            'article__item_html').get_text(strip=True)
                })
            bot.send_message(message.chat.id, "Гороскоп на завтра.")
            bot.send_message(message.chat.id, horoscope_tomorrow_gemini)

        def parse_gemini():
            html_gem_tod = get_html(URL_today_gemini)
            html_gem_tom = get_html(URL_tomorrow_gemini)
            get_content_today(html_gem_tod.text)
            get_content_tomorrow(html_gem_tom.text)

        parse_gemini()

    # РАК CANCER
    def cancer(self, message):
        # списки для хранения информации
        horoscope_today_cancer = []
        horoscope_tomorrow_cancer = []

        def get_content_today(html):
            soup = BeautifulSoup(html, 'html.parser')

            items = soup.find_all('div', class_='article__text')

            for item in items:
                horoscope_today_cancer.append({
                    item.find('div',
                              class_='article__item article__item_alignment_left '
                                     'article__item_html').get_text(strip=True)
                })
            bot.send_message(message.chat.id, "Гороскоп на сегодня.")
            bot.send_message(message.chat.id, horoscope_today_cancer)

        def get_content_tomorrow(html):
            soup = BeautifulSoup(html, 'html.parser')

            items = soup.find_all('div', class_='article__text')

            for item in items:
                horoscope_tomorrow_cancer.append({
                    item.find('div', class_='article__item article__item_alignment_left '
                                            'article__item_html').get_text(strip=True)
                })
            bot.send_message(message.chat.id, "Гороскоп на завтра.")
            bot.send_message(message.chat.id, horoscope_tomorrow_cancer)

        def parse_cancer():
            html_can_tod = get_html(URL_today_cancer)
            html_can_tom = get_html(URL_tomorrow_cancer)
            get_content_today(html_can_tod.text)
            get_content_tomorrow(html_can_tom.text)

        parse_cancer()

    # КОЗЕРОГ CAPRICORN
    def capricorn(self, message):
        # списки для хранения информации
        horoscope_today_capricorn = []
        horoscope_tomorrow_capricorn = []

        def get_content_today(html):
            soup = BeautifulSoup(html, 'html.parser')

            items = soup.find_all('div', class_='article__text')

            for item in items:
                horoscope_today_capricorn.append({
                    item.find('div',
                              class_='article__item article__item_alignment_left '
                                     'article__item_html').get_text(strip=True)
                })
            bot.send_message(message.chat.id, "Гороскоп на сегодня.")
            bot.send_message(message.chat.id, horoscope_today_capricorn)

        def get_content_tomorrow(html):
            soup = BeautifulSoup(html, 'html.parser')

            items = soup.find_all('div', class_='article__text')

            for item in items:
                horoscope_tomorrow_capricorn.append({
                    item.find('div', class_='article__item article__item_alignment_left '
                                            'article__item_html').get_text(strip=True)
                })
            bot.send_message(message.chat.id, "Гороскоп на завтра.")
            bot.send_message(message.chat.id, horoscope_tomorrow_capricorn)

        def parse_capricorn():
            html_cap_tod = get_html(URL_today_capricorn)
            html_cap_tom = get_html(URL_tomorrow_capricorn)
            get_content_today(html_cap_tod.text)
            get_content_tomorrow(html_cap_tom.text)

        parse_capricorn()

    # ДЕВА VIRGO
    def virgo(self, message):
        # списки для хранения информации
        horoscope_today_virgo = []
        horoscope_tomorrow_virgo = []

        def get_content_today(html):
            soup = BeautifulSoup(html, 'html.parser')

            items = soup.find_all('div', class_='article__text')

            for item in items:
                horoscope_today_virgo.append({
                    item.find('div',
                              class_='article__item article__item_alignment_left '
                                     'article__item_html').get_text(strip=True)
                })
            bot.send_message(message.chat.id, "Гороскоп на сегодня.")
            bot.send_message(message.chat.id, horoscope_today_virgo)

        def get_content_tomorrow(html):
            soup = BeautifulSoup(html, 'html.parser')

            items = soup.find_all('div', class_='article__text')

            for item in items:
                horoscope_tomorrow_virgo.append({
                    item.find('div', class_='article__item article__item_alignment_left '
                                            'article__item_html').get_text(strip=True)
                })
            bot.send_message(message.chat.id, "Гороскоп на завтра.")
            bot.send_message(message.chat.id, horoscope_tomorrow_virgo)

        def parse_virgo():
            html_vir_tod = get_html(URL_today_virgo)
            html_vir_tom = get_html(URL_tomorrow_virgo)
            get_content_today(html_vir_tod.text)
            get_content_tomorrow(html_vir_tom.text)

        parse_virgo()

    # ВОДОЛЕЙ AQUARIUS
    def aquarius(self, message):
        # списки для хранения информации
        horoscope_today_aquarius = []
        horoscope_tomorrow_aquarius = []

        def get_content_today(html):
            soup = BeautifulSoup(html, 'html.parser')

            items = soup.find_all('div', class_='article__text')

            for item in items:
                horoscope_today_aquarius.append({
                    item.find('div',
                              class_='article__item article__item_alignment_left '
                                     'article__item_html').get_text(strip=True)
                })
            bot.send_message(message.chat.id, "Гороскоп на сегодня.")
            bot.send_message(message.chat.id, horoscope_today_aquarius)

        def get_content_tomorrow(html):
            soup = BeautifulSoup(html, 'html.parser')

            items = soup.find_all('div', class_='article__text')

            for item in items:
                horoscope_tomorrow_aquarius.append({
                    item.find('div', class_='article__item article__item_alignment_left '
                                            'article__item_html').get_text(strip=True)
                })
            bot.send_message(message.chat.id, "Гороскоп на завтра.")
            bot.send_message(message.chat.id, horoscope_tomorrow_aquarius)

        def parse_aquarius():
            html_aqu_tod = get_html(URL_today_aquarius)
            html_aqu_tom = get_html(URL_tomorrow_aquarius)
            get_content_today(html_aqu_tod.text)
            get_content_tomorrow(html_aqu_tom.text)

        parse_aquarius()

    # ТЕЛЕЦ TAURUS
    def taurus(self, message):
        # списки для хранения информации
        horoscope_today_taurus = []
        horoscope_tomorrow_taurus = []

        def get_content_today(html):
            soup = BeautifulSoup(html, 'html.parser')

            items = soup.find_all('div', class_='article__text')

            for item in items:
                horoscope_today_taurus.append({
                    item.find('div',
                              class_='article__item article__item_alignment_left '
                                     'article__item_html').get_text(strip=True)
                })
            bot.send_message(message.chat.id, "Гороскоп на сегодня.")
            bot.send_message(message.chat.id, horoscope_today_taurus)

        def get_content_tomorrow(html):
            soup = BeautifulSoup(html, 'html.parser')

            items = soup.find_all('div', class_='article__text')

            for item in items:
                horoscope_tomorrow_taurus.append({
                    item.find('div', class_='article__item article__item_alignment_left '
                                            'article__item_html').get_text(strip=True)
                })
            bot.send_message(message.chat.id, "Гороскоп на завтра.")
            bot.send_message(message.chat.id, horoscope_tomorrow_taurus)

        def parse_taurus():
            html_tau_tod = get_html(URL_today_taurus)
            html_tau_tom = get_html(URL_tomorrow_taurus)
            get_content_today(html_tau_tod.text)
            get_content_tomorrow(html_tau_tom.text)

        parse_taurus()

    # ЛЕВ LEO
    def leo(self, message):
        # списки для хранения информации
        horoscope_today_leo = []
        horoscope_tomorrow_leo = []

        def get_content_today(html):
            soup = BeautifulSoup(html, 'html.parser')

            items = soup.find_all('div', class_='article__text')

            for item in items:
                horoscope_today_leo.append({
                    item.find('div',
                              class_='article__item article__item_alignment_left '
                                     'article__item_html').get_text(strip=True)
                })
            bot.send_message(message.chat.id, "Гороскоп на сегодня.")
            bot.send_message(message.chat.id, horoscope_today_leo)

        def get_content_tomorrow(html):
            soup = BeautifulSoup(html, 'html.parser')

            items = soup.find_all('div', class_='article__text')

            for item in items:
                horoscope_tomorrow_leo.append({
                    item.find('div', class_='article__item article__item_alignment_left '
                                            'article__item_html').get_text(strip=True)
                })
            bot.send_message(message.chat.id, "Гороскоп на завтра.")
            bot.send_message(message.chat.id, horoscope_tomorrow_leo)

        def parse_leo():
            html_leo_tod = get_html(URL_today_leo)
            html_leo_tom = get_html(URL_tomorrow_leo)
            get_content_today(html_leo_tod.text)
            get_content_tomorrow(html_leo_tom.text)

        parse_leo()

    # ОВЕН ARIES
    def aries(self, message):
        # списки для хранения информации
        horoscope_today_aries = []
        horoscope_tomorrow_aries = []

        def get_content_today(html):
            soup = BeautifulSoup(html, 'html.parser')

            items = soup.find_all('div', class_='article__text')

            for item in items:
                horoscope_today_aries.append({
                    item.find('div',
                              class_='article__item article__item_alignment_left '
                                     'article__item_html').get_text(strip=True)
                })
            bot.send_message(message.chat.id, "Гороскоп на сегодня.")
            bot.send_message(message.chat.id, horoscope_today_aries)

        def get_content_tomorrow(html):
            soup = BeautifulSoup(html, 'html.parser')

            items = soup.find_all('div', class_='article__text')

            for item in items:
                horoscope_tomorrow_aries.append({
                    item.find('div', class_='article__item article__item_alignment_left '
                                            'article__item_html').get_text(strip=True)
                })
            bot.send_message(message.chat.id, "Гороскоп на завтра.")
            bot.send_message(message.chat.id, horoscope_tomorrow_aries)

        def parse_aries():
            html_ari_tod = get_html(URl_today_aries)
            html_ari_tom = get_html(URl_tomorrow_aries)
            get_content_today(html_ari_tod.text)
            get_content_tomorrow(html_ari_tom.text)

        parse_aries()

    # РЫБЫ PISCES
    def pisces(self, message):
        # списки для хранения информации
        horoscope_today_pisces = []
        horoscope_tomorrow_pisces = []

        def get_content_today(html):
            soup = BeautifulSoup(html, 'html.parser')

            items = soup.find_all('div', class_='article__text')

            for item in items:
                horoscope_today_pisces.append({
                    item.find('div',
                              class_='article__item article__item_alignment_left '
                                     'article__item_html').get_text(strip=True)
                })
                bot.send_message(message.chat.id, "Гороскоп на сегодня.")
                bot.send_message(message.chat.id, horoscope_today_pisces)

        def get_content_tomorrow(html):
            soup = BeautifulSoup(html, 'html.parser')

            items = soup.find_all('div', class_='article__text')

            for item in items:
                horoscope_tomorrow_pisces.append({
                    item.find('div', class_='article__item article__item_alignment_left '
                                            'article__item_html').get_text(strip=True)
                })
                bot.send_message(message.chat.id, "Гороскоп на завтра.")
                bot.send_message(message.chat.id, horoscope_tomorrow_pisces)

        def parse_pisces():
            html_pis_tod = get_html(URL_today_pisces)
            html_pis_tom = get_html(URL_tomorrow_pisces)
            get_content_today(html_pis_tod.text)
            get_content_tomorrow(html_pis_tom.text)

        parse_pisces()

    # СТРЕЛЕЦ SAGITTARIUS
    def sagittarius(self, message):
        # списки для хранения информации
        horoscope_today_sagittarius = []
        horoscope_tomorrow_sagittarius = []

        def get_content_today(html):
            soup = BeautifulSoup(html, 'html.parser')

            items = soup.find_all('div', class_='article__text')

            for item in items:
                horoscope_today_sagittarius.append({
                    item.find('div',
                              class_='article__item article__item_alignment_left '
                                     'article__item_html').get_text(strip=True)
                })
            bot.send_message(message.chat.id, "Гороскоп на сегодня.")
            bot.send_message(message.chat.id, horoscope_today_sagittarius)

        def get_content_tomorrow(html):
            soup = BeautifulSoup(html, 'html.parser')

            items = soup.find_all('div', class_='article__text')

            for item in items:
                horoscope_tomorrow_sagittarius.append({
                    item.find('div', class_='article__item article__item_alignment_left '
                                            'article__item_html').get_text(strip=True)
                })
            bot.send_message(message.chat.id, "Гороскоп на завтра.")
            bot.send_message(message.chat.id, horoscope_tomorrow_sagittarius)

        def parse_sagittarius():
            html_sag_tod = get_html(URL_today_sagittarius)
            html_sag_tom = get_html(URL_tomorrow_sagittarius)
            get_content_today(html_sag_tod.text)
            get_content_tomorrow(html_sag_tom.text)

        parse_sagittarius()

    # ВЕСЫ LIBRA
    def libra(self, message):
        # списки для хранения информации
        horoscope_today_libra = []
        horoscope_tomorrow_libra = []

        def get_content_today(html):
            soup = BeautifulSoup(html, 'html.parser')

            items = soup.find_all('div', class_='article__text')

            for item in items:
                horoscope_today_libra.append({
                    item.find('div',
                              class_='article__item article__item_alignment_left '
                                     'article__item_html').get_text(strip=True)
                })
            bot.send_message(message.chat.id, "Гороскоп на сегодня.")
            bot.send_message(message.chat.id, horoscope_today_libra)

        def get_content_tomorrow(html):
            soup = BeautifulSoup(html, 'html.parser')

            items = soup.find_all('div', class_='article__text')

            for item in items:
                horoscope_tomorrow_libra.append({
                    item.find('div', class_='article__item article__item_alignment_left '
                                            'article__item_html').get_text(strip=True)
                })
            bot.send_message(message.chat.id, "Гороскоп на завтра.")
            bot.send_message(message.chat.id, horoscope_tomorrow_libra)

        def parse_libra():
            html_lib_tod = get_html(URL_today_libra)
            html_lib_tom = get_html(URL_tomorrow_libra)
            get_content_today(html_lib_tod.text)
            get_content_tomorrow(html_lib_tom.text)

        parse_libra()

    # СКОРПИОН SCORPIO
    def scorpio(self, message):
        # списки для хранения информации
        horoscope_today_scorpio = []
        horoscope_tomorrow_scorpio = []

        def get_content_today(html):
            soup = BeautifulSoup(html, 'html.parser')

            items = soup.find_all('div', class_='article__text')

            for item in items:
                horoscope_today_scorpio.append({
                    item.find('div',
                              class_='article__item article__item_alignment_left '
                                     'article__item_html').get_text(strip=True)
                })
            bot.send_message(message.chat.id, "Гороскоп на сегодня.")
            bot.send_message(message.chat.id, horoscope_today_scorpio)

        def get_content_tomorrow(html):
            soup = BeautifulSoup(html, 'html.parser')

            items = soup.find_all('div', class_='article__text')

            for item in items:
                horoscope_tomorrow_scorpio.append({
                    item.find('div', class_='article__item article__item_alignment_left '
                                            'article__item_html').get_text(strip=True)
                })
            bot.send_message(message.chat.id, "Гороскоп на завтра.")
            bot.send_message(message.chat.id, horoscope_tomorrow_scorpio)

        def parse_scorpio():
            html_sco_tod = get_html(URL_today_scorpio)
            html_sco_tom = get_html(URL_tomorrow_scorpio)
            get_content_today(html_sco_tod.text)
            get_content_tomorrow(html_sco_tom.text)

        parse_scorpio()

    # gemini(self)  # близнец 1
    # cancer()  # рак 2
    # capricorn()  # козерог 3
    # virgo()  # дева 4
    # aquarius()  # водолей 5
    # taurus()  # телец 6
    # leo()  # лев 7
    # aries()  # овен 8
    # pisces()  # рыбы 9
    # sagittarius()  # стрелец 10
    # libra()  # весы 11
    # scorpio()  # скорпион 12
