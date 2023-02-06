import telebot
from config_konverter_valyut_bot import keys, TOKEN
from utils_konverter_valyut_bot import CryptoConverter, ConvertionException


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def hepl(message: telebot.types.Message):
    text = "Чтобы начать работу введите команду боту в следующем формате: \n <имя валюты цену которой хотите узнать> \
    <имя валюты в которой надо узнать цену первой валюты> \
    <количество первой валюты> \n Увидеть список всех возможных влют: /values"
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

    if len(values) != 3:
        raise ConvertionException("Слишком много параметров.")

    quote, base, amount = values
    total_base = CryptoConverter.convert(quote, base, amount)

    text = f"Цена {amount} {quote} в {base} - {total_base}"
    bot.send_message(message.chat.id, text)


bot.polling()

# quote_ticker, base_ticker = keys[quote], keys[base]