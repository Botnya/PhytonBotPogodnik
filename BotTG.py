import telebot
from telebot import types
import requests

API_TOKEN = "API TOKEN"
api_weather = 'a9f1a99918d0e85934826f6155e026a6'

my_bot = telebot.TeleBot(token=API_TOKEN)  # регистрация бота


@my_bot.message_handler(commands=['start'])  # ограничитель для команды старт
def send_welcome(message):
    mes = 'Привет! Напиши мне город, и я скажу погоду в нем.'
    my_bot.send_message(message.chat.id, mes)


@my_bot.message_handler(content_types=['text'])  # ограничитель для текста
def send_text(message):
    cur_city = message.text.lower()
    url = f'http://api.openweathermap.org/data/2.5/weather?q={cur_city}&APPID={api_weather}&units=metric&lang=RU'
    url2 = f'http://api.openweathermap.org/data/2.5/forecast/daily?q={cur_city}&cnt=7&APPID={api_weather}&units=metric&lang=RU'

    response = requests.get(url)
    data = response.json()
    # print(data)
    city = data['name']
    temp = data['main']['temp']
    speed = data['wind']['speed']
    # print(city, temp)
    asnswer = f'Город: {city}\n\nТемпература: {temp} °C\nСкорость ветра: {speed} м/с'
    my_bot.send_message(message.chat.id, asnswer)


my_bot.infinity_polling()