import telebot

from telebot import types

bot = telebot.TeleBot("5096783252:AAE3fg4Eo-I0nGnLpbM4hSdNP5KJj-DlOzI")

@bot.message_handler(commands=['start','я люблю тебя'])
def send_welcome(message):
    bot.reply_to(message,"I love you")
    image = open("/home/kachigos/Загрузки/photo_2021-12-22_04-16-55.jpg",'rb')

    bot.send_photo(message.chat.id, image)

bot.polling(none_stop=True,interval=0)
