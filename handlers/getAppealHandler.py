from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


from pyrogram import types
 

def handle_appeal(client, callback_query, document_options, user_data, bot):
    user_id = callback_query.from_user.id
    selected_option = callback_query.data

    if selected_option in ["english", "hindi", "marathi"]:
        # Language selection scenario
        user_data[user_id] = {"language": selected_option, "state": "festival"}
        festivals = document_options[selected_option]
        festival_buttons = [
            #showing json key as option for festival
            [InlineKeyboardButton(festival, callback_data=festival)] for festival in festivals
        ]
        festival_buttons.append([InlineKeyboardButton("Back", callback_data="back")])
        reply_markup = InlineKeyboardMarkup(festival_buttons)
        callback_query.message.reply(f"Selected language: {selected_option.capitalize()}\nSelect a festival:", reply_markup=reply_markup)

    elif selected_option == "back":
        # Always go back to language selection menu when the back button is pressed
        user_data[user_id]["state"] = "language"
        languages = [
            [InlineKeyboardButton("English", callback_data="english")],
            [InlineKeyboardButton("Hindi", callback_data="hindi")],
            [InlineKeyboardButton("Marathi", callback_data="marathi")]
        ]
        reply_markup = InlineKeyboardMarkup(languages)
        callback_query.message.reply("Which language do you want?", reply_markup=reply_markup)

    elif selected_option in document_options.get(user_data.get(user_id, {}).get("language", ""), {}):
        # User selected a festival
        user_language = user_data[user_id]["language"]
        dropbox_link = document_options[user_language][selected_option]

        # Generate a direct download link
        direct_download_link = dropbox_link.replace("www.dropbox.com", "dl.dropboxusercontent.com")

        # Send the direct download link as a message
        bot.send_message(
            callback_query.message.chat.id,
            f"Here is the direct download link to {user_language} {selected_option} document: {direct_download_link}"
        )