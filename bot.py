# Import and register your bot handlers and other code
from mainMenu import start_menu
from handlers.getAppealHandler import handle_appeal
from file_manager.constant import document_options, user_data
import logging
from dotenv import load_dotenv
import os
from pyrogram import Client, filters, idle
# from flask_app import app

# Load environment variables from .env file
load_dotenv()

import logging

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Add a stream handler to write logs to the console
stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

# # Add a file handler to write logs to a file
# file_handler = logging.FileHandler('bot.log')
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)

# Set Pyrogram logging level
logging.getLogger("pyrogram").setLevel(logging.DEBUG)

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")


def init_bot():
    return Client(
    "m21bot",
    bot_token=BOT_TOKEN, 
    api_id=2854217,
    api_hash="ac6df80f6d704e9164503dabe3dcded6"
)



# # Initialize the Telegram bot
# def init_bot():
#     return Client(
#         "yeshpal_bot",
#         bot_token=BOT_TOKEN,
#         api_id=2854217,
#         api_hash="ac6df80f6d704e9164503dabe3dcded6"
#     )

# Initialize the bot instance
bot = init_bot()

# Start command
@bot.on_message(filters.command("start") & filters.private)
def start_command(client, message):
    user_id = message.chat.id
    logger.info(f'Start button has been clicked by the user {user_id}')
    bot.send_message(user_id, f" BOT STARTED from Start BUTTON {user_id}")
    start_menu(client, message)

# Callback for language selection and back button
@bot.on_callback_query()
def callback(client, callback_query):
    handle_appeal(client, callback_query, document_options, user_data, bot)

# Handler for other text messages
@bot.on_message(~filters.command("start"))
def handle_messages(client, message):
    user_id = message.chat.id
    if user_data.get(user_id, {}).get("state") == "festival":
        bot.send_message(user_id, "Invalid choice. Please select a festival from the options.")
    else:
        bot.send_message(user_id, "Please enter /start to start the bot.")

if __name__ == "__main__":

    logger.info("Telegram bot started")
    # Run the Telegram bot
    bot.start()
    logger.info("Bot started, now running idle")
    idle()
    