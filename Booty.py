import json
import telebot
import requests

TOKEN = '6880602647:AAEJFBAN2jnOblSJoing7AXjzZcqFCFQFNI'

bot = telebot.TeleBot(TOKEN)

keys = {
    'btc': 'BTC',
    'eth': 'ETH',
    'ltc': 'LTC',
    'usd': 'USD',
    'eur': 'EUR',
    'gbp': 'GBP',
}

fiats = ['USD - United States Dollar', 'EUR - Euro', 'GBP - Pound sterling']
crypto = ['BTC - Bitcoin', 'ETH - Ethereum', 'LTC - Litecoin', 'XRP -Ripple']

@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    print("Received /start or /help command.")
    print(f"Username: {message.chat.username}")
    text = (f"Hi {message.chat.username}!\n"
            "I am a bot and I can convert crypto real fast!\n"
            "You can control me using these commands:\n\n"
            "/start or /help for instructions\n"
            "/values for available currencies list\n\n"
            "Example: 1 BTC USD (spaces are mandatory)"
            )
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    print('Received /values command.')
    text = 'Available crypto:\n' + "\n".join(crypto) + '\n\nAvailable currencies: \n' + "\n".join(fiats)
    print('Printed values')
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    amount, quote, base = message.text.split()
    print(f'Quote: {quote}, Base: {base}')
    try:
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}')
        print('r', r)
        total_base = json.loads(r.content)[keys[base]]  #[keys[base]] extracts value from JSON response
        print('r.content', r.content)
        print('total_base', total_base)
        text = f'{amount} {quote} is {total_base} {base}'
        bot.send_message(message.chat.id, text)
    except Exception as e:
        error_text = f'An error occurred: {str(e)}'
        bot.send_message(message.chat.id, error_text)

# @bot.message_handler(content_types=['text'])
# def reply(message: telebot.types.Message):
#     text = 'Dont understand you!'
#     bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)
