import telebot
from telebot import types
from secret import token

bot = telebot.TeleBot(token)

messages = {} #need for storing message id`s ,chat_id -> message_id
currentState = {} 

def gen_keyboard_0():
    keyboard = types.InlineKeyboardMarkup()
    buy = types.InlineKeyboardButton("Купить", callback_data = 'buy')
    keyboard.add(buy)
    #prev = types.InlineKeyboardButton("Назад", callback_data = 'prev')
    next = types.InlineKeyboardButton("Далее", callback_data = 'next')
    keyboard.add(next)
    next_item = types.InlineKeyboardButton("Следующий товар",callback_data = 'next_item')
    keyboard.add(next_item)
    return keyboard

def gen_keyboard_1():
    keyboard = types.InlineKeyboardMarkup()
    buy = types.InlineKeyboardButton("Купить", callback_data = 'buy')
    keyboard.add(buy)
    prev = types.InlineKeyboardButton("Назад", callback_data = 'prev')
    next = types.InlineKeyboardButton("Далее", callback_data = 'next')
    keyboard.add(prev,next)
    next_item = types.InlineKeyboardButton("Следующий товар",callback_data = 'next_item')
    keyboard.add(next_item)
    return keyboard

def gen_keyboard_2():
    keyboard = types.InlineKeyboardMarkup()
    buy = types.InlineKeyboardButton("Купить", callback_data = 'buy')
    keyboard.add(buy)
    prev = types.InlineKeyboardButton("Назад", callback_data = 'prev')
    #next = types.InlineKeyboardButton("Далее", callback_data = 'next')
    keyboard.add(prev)
    next_item = types.InlineKeyboardButton("Следующий товар",callback_data = 'next_item')
    keyboard.add(next_item)
    return keyboard

keyboard = types.InlineKeyboardMarkup()
buy = types.InlineKeyboardButton("Купить", callback_data = 'buy')
keyboard.add(buy)
prev = types.InlineKeyboardButton("Назад", callback_data = 'prev')
next = types.InlineKeyboardButton("Далее", callback_data = 'next')
keyboard.add(prev,next)
next_item = types.InlineKeyboardButton("Следующий товар",callback_data = 'next_item')
keyboard.add(next_item)



@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет!')

@bot.message_handler(commands=['test'])
def start_message(message):
    f1 = open("sur.jpg",'rb');
    chat_id = message.chat.id
    sended_photo = bot.send_photo(chat_id, photo = f1,reply_markup=keyboard)
    messages[chat_id] = sended_photo.message_id
    currentState[chat_id] = 'init'
    print(f'chat_id: {chat_id}, message_id: {messages[chat_id]}')

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Абракадабра')
    if call.data == 'buy':
        #buy logic
        bot.send_message(call.message.chat.id, "C вами свяжется продавец!")
    elif call.data == 'prev':
        #prev logic
        chat_id = call.message.chat.id
        currentState[chat_id] = 'prev'
        f2 = open("sur2.jpg",'rb');
        bot.edit_message_media(media=types.InputMedia(type='photo', media=f2),chat_id = chat_id, message_id = messages[chat_id],reply_markup=keyboard)
    elif call.data == 'next':
        #next logic
        chat_id = call.message.chat.id
        currentState[chat_id] = 'next'
        f3 = open("sur3.jpg",'rb');
        bot.edit_message_media(media=types.InputMedia(type='photo', media=f3),chat_id = chat_id, message_id = messages[chat_id],reply_markup=keyboard)
        print(f'chat_id: {chat_id}, message_id: {messages[chat_id]}')
    elif call.data == 'next_item':
        #next item logic
        f1 = open("sur2.jpg",'rb');
        chat_id = call.message.chat.id
        sended_photo = bot.send_photo(chat_id, photo = f1,reply_markup=keyboard)
        messages[chat_id] = sended_photo.message_id
        currentState[chat_id] = 'init'
        print(f'chat_id: {chat_id}, message_id: {messages[chat_id]}')

bot.polling()