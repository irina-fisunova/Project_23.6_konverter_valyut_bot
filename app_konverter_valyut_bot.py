import telebot
from config import keys, TOKEN
from extensions import CryptoConverter, ConvertionException


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
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionException("Запрос введен некорректно. Слишком много/мало параметров.")
        quote, base, amount = values
        quote = quote.upper()
        base = base.upper()
        amount = amount.replace(",", ".")
        cost = CryptoConverter.convert(quote, base, amount)
    except ConvertionException as e:
        bot.reply_to(message, f"Ошибка пользователя. \n {e}")
    except Exception as e:
        bot.reply_to(message, f"Не удалось обработать команду. \n {e}")
    else:
        text = f"Цена 1 {quote} - {cost.get('single')} {base}.\n Стоимость {amount} {quote} = {cost.get('total')} {base}"
        bot.send_message(message.chat.id, text)


bot.polling()
