import pyowm
from pyowm.exceptions import api_response_error, api_call_error
import telebot

bot = telebot.TeleBot("1644586994:AAGtW78FVpmDscoiV-ZRWAXNvFLrJ-aKjbo")  # апи бота

owm = pyowm.OWM('797385fc66158e63cb61ac82a7d4ee8c', language="ru")  # ключ и язык


# @bot.message_handler(content_types=['text'])  # отвечает на тип текст
def send_echo(message):  # дублирует
    try:
        city_name = message.text[9:]
        bot.send_message(message.chat.id, "Погода в городе " + city_name)
        observation = owm.weather_at_place(city_name)  # Место где будет показывавть погоду
        w = observation.get_weather()
        temp = w.get_temperature('celsius')["temp"]  # получение температуры
        wind = w.get_wind()["speed"]  # Скрость ветра
        answer = "В городе/стране " + city_name + " сейчас " + w.get_detailed_status() + "\n"
        answer += "Сейчас примерно " + str(temp) + " °C" + "\n"
        answer += "Ветер " + str(wind) + " м/c" + "\n"
        bot.send_message(message.chat.id, answer)  # ввывод в телеграмм
    except api_response_error.NotFoundError:
        bot.send_message(message.chat.id, "Неправильный город/страна")
        pass


@bot.message_handler(commands=['weather'])
def helpp(message):
    bot.send_message(message.chat.id, "Вы перешли в режим просмотра погоды")
    send_echo(message)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Начало работы")


bot.polling(none_stop=True)
