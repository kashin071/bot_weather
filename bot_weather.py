import telebot
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

bot = telebot.TeleBot('token')
owm = OWM('token')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Этот бот умеет узнавать погоду. Введите город.')

@bot.message_handler(content_types=['text'])
def send_text(message):
    try:
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(message.text)
        w = observation.weather
        temperature = w.temperature('celsius')['temp']
        w1 = w.detailed_status
    
        bot.send_message(message.chat.id, 'В городе ' + message.text + ' сейчас '  + str(temperature) + ' градусов по Цельсию, ' + w1 + '.')
    except:
        bot.send_message(message.chat.id, 'Такого города еще нет.')

bot.polling()