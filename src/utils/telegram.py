import os
import telebot


# Carrega o .env somente se estiver rodando localmente
token1 = '7294948712:AAEj57qIFRaXmS8ZB__'
token2 = '0nq6SETufOIb6hzQ'

token_final = token1 + token2


def enviar_mensagem(mensagem, CHAT_ID = '5588207726',BOT_TOKEN = token_final):

    bot = telebot.TeleBot(BOT_TOKEN)

    # Enviando a mensagem
    bot.send_message(CHAT_ID, mensagem)

