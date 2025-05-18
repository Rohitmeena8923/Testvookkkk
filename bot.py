import telebot
from config import BOT_TOKEN
import threading

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "Testbook Extractor Bot is running!")

def run_bot():
    bot.polling(non_stop=True)
