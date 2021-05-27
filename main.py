from horoscope import HOROSCOPE
from films import FILMS
from news import Newser
from telebot import types
import telebot
import COVID19Py
import datetime
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot("1644586994:AAGtW78FVpmDscoiV-ZRWAXNvFLrJ-aKjbo")  # апи бота

token = "797385fc66158e63cb61ac82a7d4ee8c"  # токен погоды

HEADERS = {
    # user-agent нужен чтобы сайт не посчитал нас ботами
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 YaBrowser/21.3.2.193 Yowser/2.5 Safari/537.36'

}


# Новости
@bot.message_handler(commands=['news'])
def Newss(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)  # быстрые кнопки
    btn1 = types.KeyboardButton('Местные')
    btn2 = types.KeyboardButton('Всероссийские')

    markup.add(btn1, btn2)
    send_message = f"<b>Привет {message.from_user.first_name}!</b>\nВыбери новости и читай!"
    bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)
    bot.register_next_step_handler(message, answer_news)  # после команды вызов функции answer_news


def answer_news(message):
    bot.send_message(message.chat.id, 'Доброго времени суток уважаемый читатель!', reply_markup=types.ReplyKeyboardRemove())

    final_message = ""
    get_message_bot = message.text.strip().lower()  # делаю только нижние регистры
    if get_message_bot == "местные":
        Newser.Local_news(final_message, message)
    elif get_message_bot == "всероссийские":
        Newser.All_news(final_message, message)
    else:
        bot.send_message(message.chat.id, "Ошибка! Не верно выбранны новости")


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
    bot.send_message(message.chat.id, 'Не болей!', reply_markup=types.ReplyKeyboardRemove())


@bot.message_handler(commands=['films'])
def films(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)  # быстрые кнопки
    btn1 = types.KeyboardButton('Новинки')
    btn2 = types.KeyboardButton('Артхаус')
    btn3 = types.KeyboardButton('Боевики')
    btn4 = types.KeyboardButton('Военные')
    btn5 = types.KeyboardButton('Детектив')
    btn6 = types.KeyboardButton('Драма')
    btn7 = types.KeyboardButton('Комедия')
    btn8 = types.KeyboardButton('Криминал')
    btn9 = types.KeyboardButton('Мелодрама')
    btn10 = types.KeyboardButton('Мистика')
    btn11 = types.KeyboardButton('Приключения')
    btn12 = types.KeyboardButton('Триллер')
    btn13 = types.KeyboardButton('Ужасы')
    btn14 = types.KeyboardButton('Фантастика')
    btn15 = types.KeyboardButton('Фэнтези')

    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15)
    send_message = f"<b>Привет {message.from_user.first_name}!</b>\nВыбери интересующий жанр фильмов и наслаждайся!"
    bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)
    bot.register_next_step_handler(message, answer_films)  # после команды вызов функции answer_films


def answer_films(message):
    bot.send_message(message.chat.id, 'Доброго времени суток!', reply_markup=types.ReplyKeyboardRemove())

    final_message = ""
    get_message_bot = message.text.strip().lower()  # делаю только нижние регистры
    if get_message_bot == "новинки":
        FILMS.new_films(final_message, message)
    elif get_message_bot == "артхаус":
        FILMS.art_house(final_message, message)
    elif get_message_bot == "боевики":
        FILMS.boeviki(final_message, message)
    elif get_message_bot == "военные":
        FILMS.voennye(final_message, message)
    elif get_message_bot == "детектив":
        FILMS.detective(final_message, message)
    elif get_message_bot == "драма":
        FILMS.drama(final_message, message)
    elif get_message_bot == "комедия":
        FILMS.comedy(final_message, message)
    elif get_message_bot == "криминал":
        FILMS.crime(final_message, message)
    elif get_message_bot == "мелодрама":
        FILMS.melodrama(final_message, message)
    elif get_message_bot == "мистика":
        FILMS.mystic(final_message, message)
    elif get_message_bot == "приключения":
        FILMS.adventure(final_message, message)
    elif get_message_bot == "триллер":
        FILMS.thriller(final_message, message)
    elif get_message_bot == "ужасы":
        FILMS.horror(final_message, message)
    elif get_message_bot == "фантастика":
        FILMS.fantastic(final_message, message)
    elif get_message_bot == "фэнтези":
        FILMS.fantasy(final_message, message)
    else:
        bot.send_message(message.chat.id, "Такого жанра нет!")


@bot.message_handler(commands=['horoscope'])
def horoscope(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)  # быстрые кнопки
    btn1 = types.KeyboardButton('Рыбы')
    btn2 = types.KeyboardButton('Овен')
    btn3 = types.KeyboardButton('Рак')
    btn4 = types.KeyboardButton('Лев')

    markup.add(btn1, btn2, btn3, btn4)

    send_message = f"<b>Привет {message.from_user.first_name}!</b>\nХочешь узнать свой гороскоп? <b>Тогда напиши свой " \
                   f"знак!</b>" \
                   f"например: Рак, Овен, Рыбы и так далее\n"
    bot.send_message(message.chat.id, send_message, parse_mode='html', reply_markup=markup)
    bot.register_next_step_handler(message, answer_horoscope)  # после команды вызов функции answer_horoscope


def answer_horoscope(message):
    # ночь с 00:00 до 6:00
    # утро с 6:00 до 12:00
    # день с 12:00 до 18:00
    # вечер с 18:00 до 00:00
    date = datetime.datetime.today()
    day = ""

    if 0 < date.hour <= 6:
        day = "Хорошей ночи"
    elif 6 < date.hour <= 12:
        day = "Хорошего утра."
    elif 12 < date.hour <= 18:
        day = "Хорошего дня."
    elif 18 < date.hour <= 24:
        day = "Хорошего вечера."

    final_message = day
    bot.send_message(message.chat.id, "Удачи!", reply_markup=types.ReplyKeyboardRemove())

    get_message_bot = message.text.strip().lower()  # делаю только нижние регистры
    if get_message_bot == "близнецы":
        HOROSCOPE.gemini(final_message, message)
    elif get_message_bot == "рак":
        HOROSCOPE.cancer(final_message, message)
    elif get_message_bot == "козерог":
        HOROSCOPE.capricorn(final_message, message)
    elif get_message_bot == "дева":
        HOROSCOPE.virgo(final_message, message)
    elif get_message_bot == "водолей":
        HOROSCOPE.aquarius(final_message, message)
    elif get_message_bot == "телец":
        HOROSCOPE.taurus(final_message, message)
    elif get_message_bot == "лев":
        HOROSCOPE.leo(final_message, message)
    elif get_message_bot == "овен":
        HOROSCOPE.aries(final_message, message)
    elif get_message_bot == "рыбы":
        HOROSCOPE.pisces(final_message, message)
    elif get_message_bot == "стрелец":
        HOROSCOPE.sagittarius(final_message, message)
    elif get_message_bot == "весы":
        HOROSCOPE.libra(final_message, message)
    elif get_message_bot == "скорпион":
        HOROSCOPE.scorpio(final_message, message)
    else:
        final_message = f"<b>Такого знака нет!</b>"

    bot.send_message(message.chat.id, final_message, parse_mode='html')


@bot.message_handler(commands=['top_music_today'])
def horoscope(message):
    parse_music(message)


urL = 'https://hitmo.me/songs/top-today'
Host = 'https://ruv.hotmo.org'


def parse_music(message):
    def get_html(url, params=None):
        r = requests.get(url, headers=HEADERS, params=params)
        return r

    list_songs = []

    def get_content(html):
        soup = BeautifulSoup(html, 'html.parser')

        songs = soup.find_all('li', class_='tracks__item track mustoggler')

        for song in songs:
            list_songs.append({
                # song.find('div', class_='track__title').get_text(strip=True),
                # song.find('div', class_='track__desc').get_text(strip=True),
                song.find('div', class_='track__info').get_text(),
                # Host + song.find('a', class_='track__info-l').get('href')
            })

        for music in list_songs:
            bot.send_message(message.chat.id, music)

    def parse():
        html = get_html(urL)
        get_content(html.text)

    parse()


bot.polling(none_stop=True)
