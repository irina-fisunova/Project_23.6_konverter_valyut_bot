import telebot

TOKEN = '6103009775:AAE9yL2U_uCW-Fvk5zwujKRTjxtsvwGfcNo'

bot = telebot.TeleBot(TOKEN)

keys = {
    'Рубль':'RUB',
    'Доллар':'USD',
    'Евро':'EUR',
    'Фунт':'GBP',
    'Иена':'JPY'
}

#@bot.message_handler()
#def echo_test(message: telebot.types.Message):
#    bot.send_message(message.chat.id, 'Hello')

@bot.message_handler(commands=['начать', 'помощь'])
def hepl(message: telebot.types.Message):
    text = "Чтобы начать работу введите команду боту в следующем формате: \n <имя валюты> \
            <в какую валюту перевести> \
            <количество переводимой валюты>"
    bot.reply_to(message, text)

@bot.message_handler(commands=['валюта'])
def values(message: telebot.types.Message):
    text = "Доступные валюты"
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)



bot.polling()