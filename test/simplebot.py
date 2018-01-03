# -*- coding: utf-8 -*-
import telebot
bot = telebot.TeleBot("424475122:AAHZ8iO6KHSTmACSBVlpDH4YKHLwxuXPslc")

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, 'Привет! Я LetUsGo_bot!')

@bot.message_handler(commands=['auth'])
def send_auth(message):
    pass 

bot.polling()