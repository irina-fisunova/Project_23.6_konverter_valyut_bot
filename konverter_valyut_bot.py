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

#@bot.message_handler()
#def echo_test(message: telebot.types.Message):
#    bot.send_message(message.chat.id, 'Hello')

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
    quote, base, amount = message.text.split(' ')
    r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}')
    text = round((float(json.loads(r.content)[keys[base]]) * float(amount)),2)
    bot.send_message(message.chat.id, text)



bot.polling()