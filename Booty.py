import telebot

TOKEN = '6880602647:AAEJFBAN2jnOblSJoing7AXjzZcqFCFQFNI'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help', 'run'])
def start(message: telebot.types.Message):
    print("Received /start or /help command.")
    print(f"Username: {message.chat.username}")
    bot.reply_to(message, f"Welcome my dear friend {message.chat.username} or whatever")


@bot.message_handler(content_types=['text'])
def reply(message: telebot.types.Message):
    bot.send_message(message.chat.id, 'Dont understand you!')


bot.polling(none_stop=True)
