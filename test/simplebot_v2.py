# -*- coding: utf-8 -*-
import telebot
import config

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, 'Привет! Я LetUsGo_bot!')

@bot.message_handler(commands=['auth'])
def send_auth(message):
    pass 

bot.polling()