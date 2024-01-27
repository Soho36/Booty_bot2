def get_price():
    r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}')
    total_base = round((json.loads(r.content)[keys[base]]) * amount,
                       2)  # [keys[base]] extracts value from JSON response
    print(total_base)
    text = f'{amount} {quote} is {total_base} {base}'
    bot.send_message(message.chat.id, text)