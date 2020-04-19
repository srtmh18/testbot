import telebot
 
bot = telebot.TeleBot('1290751821:AAHFnZmCoVm4GqpNsj7PelhHW3Hbhh1t2b8')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'все блять, теперь я твое проклятье...')

@bot.message_handler(content_types=['text'])
def handle_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "иди в пизду)")
    elif message.text == "Кто ты?":
        bot.send_message(message.from_user.id, "Я твой папа ;)")
    elif message.text == "Как тебя зовут?":
        bot.send_message(message.from_user.id, "сверху написано же придурок)")
    elif message.text == "Что ты умеешь?":
        bot.send_message(message.from_user.id, "Я очень люблю трахать твою маму)")
    else:
        bot.send_message(message.from_user.id, "нахуй иди шиза блядская)")

@bot.message_handler(content_types=['photo'])
def text_handler(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'жил был на свете один кукоолд, имя его димоон...кстати у меня был друг дима он сдох')

bot.polling(none_stop=True, interval=0)