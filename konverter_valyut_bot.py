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

@bot.message_handler()
def echo_test(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'Hello')

bot.polling()