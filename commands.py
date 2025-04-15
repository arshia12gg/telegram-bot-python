from telebot import TeleBot
from telebot.types import BotCommand
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

TOKEN = os.getenv('7659692029:AAFUc6aEkobCqdA8iQ4peCd2mT8BiCzAark')
bot = TeleBot(TOKEN)

def register_commands(bot: TeleBot):
    commands = [
        BotCommand("start", "Start the bot"),
        BotCommand("hello", "Hello"),
    ]
    
    bot.set_my_commands(commands)

register_commands(bot)
