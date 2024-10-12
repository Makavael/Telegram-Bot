from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import schedule
import time
import threading
from random import choice
import colorama
import asyncio

colorama.init(autoreset=True)

TOKEN = '7138102548:AAFcY-t0XSHsAhPxGkyPHRlAL9Xxb8-0GPk'
CHANNEL_USERNAME = '@walletveli' 

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hello! I am your bot.')

def generate_visa():
    numofvisa = 16
    nums = '123456789'
    visa = ''.join(choice(nums) for _ in range(numofvisa))
    visacr = '123456789'
    visas = 1
    viscr = ''.join(choice(visacr) for _ in range(visas))
    visacr = '5'
    visas = 2
    vissadata = '02'.join(choice(visacr) for _ in range(visas))
    visacvcn = '123456789'
    visacvch = 3
    visacvc = ''.join(choice(visacvcn) for _ in range(visacvch))
    
    return f"{visa}|{viscr}/{vissadata}|{visacvc}"

async def post_to_channel(message):
    await application.bot.send_message(chat_id=CHANNEL_USERNAME, text=message)

def job():
    visa_message = generate_visa()
    asyncio.run(post_to_channel(visa_message))

def run_scheduler():
    while True:
        schedule.run_pending()
        time.sleep(1)

def start_scheduler():
    scheduler_thread = threading.Thread(target=run_scheduler)
    scheduler_thread.start()

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))

    
    start_scheduler()
    
    application.run_polling()

