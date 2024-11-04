import telebot
from config import TOKEN, keys
from extensions import APIException, CryptoConverter

bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следующем формате: \n<имя валюты> \
<в какую валюту перевести> <количество переводимой валюты>\nУвидеть список всех доступных валют: /values\n'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) != 3:
            raise APIException('Слишком много параметров')
        quote, base, amount = values
        text=CryptoConverter.get_price(quote, base, amount)
        if amount <= '0':
            raise APIException('Количество должно быть больше нуля')
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя:\n{e}.')
    else:
        if amount == '1':
            text = f'Цена {amount} {quote} в {base} - {text}.\n{amount} {keys[quote]} = {text} {keys[base]}'
        else:
            finally_amount = float(text) * float(amount)
            text = f'Цена {amount} {quote} в {base} - {finally_amount}.\n{amount} {keys[quote]} = {finally_amount} {keys[base]}'
        bot.send_message(message.chat.id, text)

bot.polling()