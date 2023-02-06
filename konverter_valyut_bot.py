import json

import requests
import telebot

TOKEN = '6103009775:AAE9yL2U_uCW-Fvk5zwujKRTjxtsvwGfcNo'

bot = telebot.TeleBot(TOKEN)

keys = {
    'рубль':'RUB',
    'доллар':'USD',
    'евро':'EUR'
}

class ConvertionException(Exception):
    pass

@bot.message_handler(commands=['start', 'help'])
def hepl(message: telebot.types.Message):
    text = "Чтобы начать работу введите команду боту в следующем формате: \n <имя валюты цену которой хотите узнать> \
    <имя валюты в которой надо узнать цену первой валюты> \
    <количество первой валюты> \n Увидеть список всех возможных влют: /валюта"
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = "Доступные валюты"
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text',])
def convert(message: telebot.types.Message):
    values = message.text.split(' ')

    if len(values) > 3:
        raise ConvertionException("Слишком много параметров.")

    quote, base, amount = values

    if quote == base:
        raise ConvertionException(f"Невозможно перевести одинаковые валюты {quote}.")

    try:
        quote_ticker = keys[quote]
    except KeyError:
        raise ConvertionException(f"Не удалось обработать валюту {quote}")
    try:
        base_ticker = keys[quote]
    except KeyError:
        raise ConvertionException(f"Не удалось обработать валюту {base}")
    try:
        amount = float(amount)
    except ValueError:
        raise ConvertionException(f"Не удалось обработать количество {amount}.")

    quote_ticker, base_ticker = keys[quote], keys[base]

    r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
    total_base = str(round((float(json.loads(r.content)[keys[base]]) * float(amount)),2))
    text = f"Цена {amount} {quote} в {base} - {total_base}"
    bot.send_message(message.chat.id, text)



bot.polling()