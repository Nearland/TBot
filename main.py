import feedparser
from telebot import types
import telebot
import COVID19Py
import datetime
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot("1644586994:AAGtW78FVpmDscoiV-ZRWAXNvFLrJ-aKjbo")  # апи бота

token = "797385fc66158e63cb61ac82a7d4ee8c"  # токен погоды


# Новости
@bot.message_handler(commands=['news'])
def news(message):
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
    for hl in allheadlines:
        bot.send_message(message.chat.id, hl)


# Погода
@bot.message_handler(commands=['weather'])
def weather(message):  # дублирует
    send_message = f"Привет {message.from_user.first_name}!\n Напиши название города, где ты хочешь кзнать погоду!"
    bot.send_message(message.chat.id, send_message, parse_mode='html')
    bot.register_next_step_handler(message, answer_weather)


def answer_weather(message):
    # иконки погоды
    weather_icons = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Слабый дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B",
        "Shower rain": "Ливень \U000026C6"
    }
    try:
        city_name = message.text  # отправка в сообщениия в ТГ

        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={token}&units=metric"
        )
        data = r.json()

        weather_description = data["weather"][0]["main"]
        if weather_description in weather_icons:  # проверка если совпадает значение словаря то мы заберем его значение
            wd = weather_icons[weather_description]
        else:
            wd = "Посмотри в окно, у меня нет иконки на этот день XD!"

        # тут берем данные из ключей json
        city_name = data["name"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset = datetime.datetime.fromtimestamp(data["sys"]["sunset"])

        weather_send = (f"**{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}**\n"
                        f"Погода в городе: {city_name}\nТемпература: {temperature}C° {wd}\n"
                        f"Влажность: {humidity}%\nДавление: {pressure} мм.рт.ст\n"
                        f"Скорость ветра: {wind} м/с\nВосход: {sunrise}\n"
                        f"Закат: {sunset}")

        bot.send_message(message.chat.id, weather_send, parse_mode='html')
    except Exception as ex:
        bot.send_message(message.chat.id, "Вы ввели не верный город!")


covid19 = COVID19Py.COVID19()


# Информация о ковид
@bot.message_handler(commands=['covid'])
def cov(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)  # быстрые кнопки
    btn1 = types.KeyboardButton('Мир')
    btn2 = types.KeyboardButton('Украина')
    btn3 = types.KeyboardButton('Россия')
    btn4 = types.KeyboardButton('Беларусь')
    markup.add(btn1, btn2, btn3, btn4)

    send_message = f"<b>Привет {message.from_user.first_name}!</b>\nЧтобы узнать данные про коронавируса напишите " \
                   f"название страны, например: США, Украина, Россия и так далее\n"
    bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)
    bot.register_next_step_handler(message, answer_covid)  # после команды вызов функции answer_covid


def answer_covid(message):
    final_message = ""
    get_message_bot = message.text.strip().lower()  # делаю только нижние регистры
    if get_message_bot == "сша":
        location = covid19.getLocationByCountryCode("US")
    elif get_message_bot == "украина":
        location = covid19.getLocationByCountryCode("UA")
    elif get_message_bot == "россия":
        location = covid19.getLocationByCountryCode("RU")
    elif get_message_bot == "беларусь":
        location = covid19.getLocationByCountryCode("BY")
    elif get_message_bot == "казакхстан":
        location = covid19.getLocationByCountryCode("KZ")
    elif get_message_bot == "италия":
        location = covid19.getLocationByCountryCode("IT")
    elif get_message_bot == "франция":
        location = covid19.getLocationByCountryCode("FR")
    elif get_message_bot == "германия":
        location = covid19.getLocationByCountryCode("DE")
    elif get_message_bot == "япония":
        location = covid19.getLocationByCountryCode("JP")
    elif get_message_bot == "норвегия":
        location = covid19.getLocationByCountryCode("NO")
    elif get_message_bot == "австралия":
        location = covid19.getLocationByCountryCode("AU")
    elif get_message_bot == "швеция":
        location = covid19.getLocationByCountryCode("SE")
    elif get_message_bot == "великобритания":
        location = covid19.getLocationByCountryCode("GB")
    elif get_message_bot == "канада":
        location = covid19.getLocationByCountryCode("CA")
    else:
        location = covid19.getLatest()
        final_message = f"<u>Данные по всему миру:</u>\n<b>Заболевших: </b>{location['confirmed']:,}" \
                        f"\n<b>Сметрей: </b>{location['deaths']:,}"

    if final_message == "":
        date = location[0]['last_updated'].split("T")
        time = date[1].split(".")
        final_message = f"<u>Данные по стране:</u>\nНаселение: {location[0]['country_population']:,}\n" \
                        f"Последнее обновление: {date[0]} {time[0]}\nПоследние данные:\n<b>" \
                        f"Заболевших: </b>{location[0]['latest']['confirmed']:,}\n<b>Сметрей: </b>" \
                        f"{location[0]['latest']['deaths']:,}"
    bot.send_message(message.chat.id, final_message, parse_mode='html')


# url сайта которого мы хоитм парсить
URL = 'https://www.ivi.ru/new/movie-new'
# заголовки
HEADERS = {
    # user-agent нужен чтобы сайт не посчитал нас ботами
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 YaBrowser/21.3.2.193 Yowser/2.5 Safari/537.36'

}
HOST = 'https://www.ivi.ru'


@bot.message_handler(commands=['films'])
def films(message):
    parse_films(message)


# парсинг фильмов
def parse_films(message):
    # функция для получения html кода
    def get_html(url, params=None):
        r = requests.get(url, headers=HEADERS, params=params)
        return r

    def get_content(html):
        soup = BeautifulSoup(html, 'html.parser')
        # тут мы вытаскиваем знаения которые нам нужны
        items = soup.find_all('li', class_='gallery__item gallery__item_virtual')

        # список куда мы будем добавлять наши словари
        film = []

        for item in items:
            film.append({
                # 'title': item.find('div', class_='nbl-slimPosterBlock__title').get_text(strip=True),
                'link': HOST + item.find('a', class_='nbl-slimPosterBlock_type_poster').get('href'),

            })
        for movie in film:
            bot.send_message(message.chat.id, movie)

    def parse():
        html = get_html(URL)
        get_content(html.text)

    parse()


bot.polling(none_stop=True)
