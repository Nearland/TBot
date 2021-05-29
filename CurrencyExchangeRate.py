import telebot
from datetime import datetime
from pycbrf import ExchangeRates

bot = telebot.TeleBot("1644586994:AAGtW78FVpmDscoiV-ZRWAXNvFLrJ-aKjbo")  # апи бота


class Rate:
    def currency_exchange(self, message):
        send_mess = message.text.strip().lower()

        if send_mess in ['usd', 'eur', 'chf', 'gbp', 'jpy', 'uah', 'kzt', 'byn', 'try', 'cny', 'aud', 'cad', 'pln']:
            rates = ExchangeRates(datetime.now())
            bot.send_message(message.chat.id, f"<b>{send_mess.upper()} курс равен "
                                              f"{float(rates[send_mess.upper()].rate)}₽</b>", parse_mode="html")
