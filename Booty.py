import json
import telebot
import requests
from config import TOKEN, keys, fiats, crypto


bot = telebot.TeleBot(TOKEN)

# ----------------------------------------------------------------


@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    print("Received /start or /help command.")
    print(f"Username: {message.chat.username}")
    text = (f"Hi {message.chat.username}!\n"
            "I am a bot and I can convert forex and crypto real fast!\n"
            "You can control me using these commands:\n\n"
            "/start or /help for instructions\n"
            "/values for available currencies list\n\n"
            "Examples:\n"
            "1 BTC USD\n"
            "1 USD GBP (spaces are mandatory)"
            )
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    print('Received /values command.')
    text = 'Available crypto:\n' + "\n".join(crypto) + '\n\nAvailable currencies: \n' + "\n".join(fiats)
    print('Values printed')
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        amount, quote, base = message.text.split()
        amount = float(amount)
        quote, base = quote.lower(), base.lower()
        print(f"Message received:{amount} {quote} {base}")

    except ValueError:
        error_text = f'Wrong input. Please check /help for info'
        bot.send_message(message.chat.id, error_text)
        print("Error message: Value error")
        return

    try:
        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}')
        total_base = round((json.loads(r.content)[keys[base]]) * amount, 4)  # [keys[base]] extracts value
        # from JSON response
        text = f'{amount} {quote} = {total_base} {base}'.upper()
        bot.send_message(message.chat.id, text)
        print("Converted value message sent")

    except requests.exceptions.RequestException as req_err:
        error_text = f'Request error occurred: {str(req_err)}'
        bot.send_message(message.chat.id, error_text)
        print("Error message: request exception")

    except json.JSONDecodeError as json_err:
        error_text = f'Error decoding JSON response: {str(json_err)}'
        bot.send_message(message.chat.id, error_text)
        print("Error message: JSON response error")

    except KeyError as key_err:
        error_text = (f'Looks like there is a typo in your input: {str(key_err)}\n'
                      f'Please try again or check /help!')
        bot.send_message(message.chat.id, error_text)
        print("Error message: Key error")

    except Exception as e:
        error_text = f'An unexpected error occurred: {str(e)}'
        bot.send_message(message.chat.id, error_text)
        print("Error message: unexpected error")


bot.polling(none_stop=True)
