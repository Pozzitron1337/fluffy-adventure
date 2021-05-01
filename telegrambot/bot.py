import telebot
from secret import token

bot = telebot.TeleBot(token)

def gen_keyboard_0():
    keyboard = telebot.types.InlineKeyboardMarkup()
    buy = telebot.types.InlineKeyboardButton("Купить", callback_data='buy')
    keyboard.add(buy)
    next = telebot.types.InlineKeyboardButton("Далее", callback_data='next')
    keyboard.add(prev,next)
    return keyboard

def gen_keyboard_1():
    keyboard = telebot.types.InlineKeyboardMarkup()
    buy = telebot.types.InlineKeyboardButton("Купить", callback_data='buy')
    keyboard.add(buy)
    prev = telebot.types.InlineKeyboardButton("Назад", callback_data='prev')
    next = telebot.types.InlineKeyboardButton("Далее", callback_data='next')
    keyboard.add(prev,next)
    return keyboard

def gen_keyboard_2():
    keyboard = telebot.types.InlineKeyboardMarkup()
    buy = telebot.types.InlineKeyboardButton("Купить", callback_data='buy')
    keyboard.add(buy)
    prev = telebot.types.InlineKeyboardButton("Назад", callback_data='prev')
    keyboard.add(prev,next)
    return keyboard

    
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет!')

@bot.message_handler(commands=['test'])
def start_message(message):
    bot.send_message(message.chat.id, text="Выбери шмот", reply_markup=keyboard)

bot.polling()