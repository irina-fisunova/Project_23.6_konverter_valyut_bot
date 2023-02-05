import json

import telebot

TOKEN = '6103009775:AAE9yL2U_uCW-Fvk5zwujKRTjxtsvwGfcNo'

bot = telebot.TeleBot(TOKEN)

keys = {
    'Рубль':'RUB',
    'Доллар':'USD',
    'Евро':'EUR'
}

#@bot.message_handler()
#def echo_test(message: telebot.types.Message):
#    bot.send_message(message.chat.id, 'Hello')

@bot.message_handler(commands=['/start ', '/help'])
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

@bot.message_handler(commands=['text', ])
def convert(message: telebot.types.Message):
    доллар рубль 1
    quote, base, amount = message.text.splite('')
    r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote}&tsyms={base}')
    text = json.loads(r.content)[base]


bot.polling()