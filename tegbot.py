import telebot
from telebot import types

bot = telebot.TeleBot("5024907710:AAHoGgxByJpUqq4RvvqoeUWH6XOf2_HcluI", parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    image = open('image/Original_Doge_meme.jpg', 'rb')
    bot.send_photo(message.chat.id, image)

    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Ноутбуки')
    itembtn2 = types.KeyboardButton('Стационарки')

    markup.add(itembtn1, itembtn2)
    bot.send_message(message.chat.id,
                     "Выберите компьютер: ",
                     reply_markup=markup)

@bot.message_handler(content_types=['text'])
def answer(message):

    if message.text == 'Ноутбуки':
        markup = types.InlineKeyboardMarkup(row_width=2)
        nout1 = telebot.types.InlineKeyboardButton("Macbook",  callback_data = 'mac')
        nout2 = telebot.types.InlineKeyboardButton("Dell inspiron", callback_data = 'dell')
        nout3 = telebot.types.InlineKeyboardButton("Lenovo", callback_data = 'lenovo')
        nout4 = telebot.types.InlineKeyboardButton("Acer", callback_data = 'acer')
        nout5 = telebot.types.InlineKeyboardButton("HP", callback_data = 'hp')
        markup.add(nout1, nout2, nout5, nout4, nout3)
        bot.send_message(message.chat.id,
                         "Выберите какой нутбук",
                         reply_markup=markup)
    else:
        bot.send_message(message.chat.id,
                         "Обратитесь к консультанту")


@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == 'mac':
            bot.send_message(call.message.chat.id, '1050$')
        if call.data == 'dell':
            bot.send_message(call.message.chat.id, '850$')
        if call.data == 'lenovo':
            bot.send_message(call.message.chat.id, '500$')
        if call.data == 'acer':
            bot.send_message(call.message.chat.id, '350$')
        if call.data == 'hp':
            bot.send_message(call.message.chat.id, '150$')
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id
        )
bot.polling(none_stop=True)