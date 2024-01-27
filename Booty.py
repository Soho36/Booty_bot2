import json
import telebot
import requests
from config import TOKEN


bot = telebot.TeleBot(TOKEN)

#----------------------------------------------------------------

keys = {
    'btc': 'BTC',
    'eth': 'ETH',
    'ltc': 'LTC',
    'usd': 'USD',
    'eur': 'EUR',
    'gbp': 'GBP',
    'xrp': 'XRP'
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
    try:
        amount, quote, base = message.text.split()
        amount = float(amount)
        quote, base = quote.lower(), base.lower()
        print(quote)

    except ValueError:
        error_text = f'Invalid input format. Please see /help of info'
        bot.send_message(message.chat.id, error_text)
        return

    try:
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}')
        total_base = round((json.loads(r.content)[keys[base]]) * amount, 2)  #[keys[base]] extracts value from JSON response
        print(total_base)
        text = f'{amount} {quote} is {total_base} {base}'
        bot.send_message(message.chat.id, text)

    except requests.exceptions.RequestException as req_err:
        error_text = f'Request error occurred: {str(req_err)}'
        bot.send_message(message.chat.id, error_text)

    except json.JSONDecoder as json_err:
        error_text = f'Error decoding JSON response: {str(json_err)}'
        bot.send_message(message.chat.id, error_text)

    except KeyError as key_err:
        error_text = f'Error accessing data in the API response: {str(key_err)}'
        bot.send_message(message.chat.id, error_text)

    except Exception as e:
        error_text = f'An unexpected error occurred: {str(e)}'
        bot.send_message(message.chat.id, error_text)


bot.polling(none_stop=True)
