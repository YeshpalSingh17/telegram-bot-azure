from bot import bot, logger
from flask_app import app
import threading

def run_bot():
    logger.info("Telegram bot started")
    bot.start()
    logger.info("Bot started, now running idle")
    bot.idle()

def run_flask():
    logger.info("Flask app started")
    app.run(host='0.0.0.0', port=8000)

if __name__ == "__main__":
    bot_thread = threading.Thread(target=run_bot)
    flask_thread = threading.Thread(target=run_flask)

    bot_thread.start()
    flask_thread.start()

    bot_thread.join()
    flask_thread.join()