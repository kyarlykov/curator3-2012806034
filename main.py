from telebot import TeleBot

bot = TeleBot('7581470494:AAGJ3DREVZl4vumNIfAEiX4hqW6QNeIg-Hc')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Посмотри, что я умею:\nКоманда /upscale — нейросеть для улучшения качества фото\nКоманда /remove — сервис для вырезания фона с фото\nКоманда /photo — ссылка на сайт для поиска фотографий\nКоманда /surprise — отправляет подарок :)')

@bot.message_handler(commands=['remove'])
def remove(message):
    bot.send_message(message.chat.id, 'https://www.photoroom.com/ru/instrumenty/ubrat-fon-onlayn')

@bot.message_handler(commands=['upscale'])
def upscale(message):
    bot.send_message(message.chat.id, 'https://problembo.com/ru/services/image-ai-upscale')

@bot.message_handler(commands=['photo'])
def photo(message):
    bot.send_message(message.chat.id, 'https://ru.freepik.com/')

# Этот код будет отправлять видео с песней never gonna give you up
@bot.message_handler(commands=['surprise'])
def surprise(message):
    bot.send_message(message.chat.id, 'https://rutube.ru/video/5b8160fb29edfb3b8043f0e462671d44/')

bot.infinity_polling()