import telebot

TOKEN = '6880602647:AAEJFBAN2jnOblSJoing7AXjzZcqFCFQFNI'

bot = telebot.TeleBot(TOKEN)

keys = {
    'bitcoin': 'BTC',
    'ether': 'ETH',
    'dollar': 'USD'
}

slovar = ['usd', 'eur', 'chf']

@bot.message_handler(commands=['start', 'help', 'run'])
def start(message: telebot.types.Message):
    # print("Received /start or /help command.")
    # print(f"Username: {message.chat.username}")
    text = f"Welcome my dear friend {message.chat.username} or whatever"
    bot.reply_to(message, text)


# @bot.message_handler(commands=['values'])
# def values(message: telebot.types.Message):
#     text = 'Available currencies: '
#     for key in keys.keys():
#         text = '\n'.join((text, key))
#     bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Available currenciese:\n' + "\n".join(slovar)
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def reply(message: telebot.types.Message):
    text = 'Dont understand you!'
    bot.send_message(message.chat.id, text)




bot.polling(none_stop=True)
