from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def start_menu(client, message):
    languages = [
        [InlineKeyboardButton("English", callback_data="english")],
        [InlineKeyboardButton("Hindi", callback_data="hindi")],
        [InlineKeyboardButton("Marathi", callback_data="marathi")]
    ]
    reply_markup = InlineKeyboardMarkup(languages)
    message.reply("Which LANGUAGE do you want?", reply_markup=reply_markup)
