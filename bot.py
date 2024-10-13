from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import schedule
import time
import threading
from random import choice, randint
import colorama
import asyncio

colorama.init(autoreset=True)

TOKEN = '7138102548:AAFcY-t0XSHsAhPxGkyPHRlAL9Xxb8-0GPk'  
CHANNEL_USERNAME = '@walletveli' 
application = ApplicationBuilder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hello! I am your bot.')

def generate_visa():
    bin_number = '455225'
    numofvisa = 16
    nums = '0123456789'
    visa = bin_number + ''.join(choice(nums) for _ in range(numofvisa - len(bin_number)))

    expiry_year = randint(2024, 2030)
    expiry_month = randint(1, 12)
    expiry = f"{expiry_month:02d} l {expiry_year}"

    cvc = ''.join(choice('0123456789') for _ in range(3))

    message = (
        "Dev : @Makavael\n"
        "↳\n"
        f"Card: {visa} l {expiry} l {cvc}\n"
        "↳\n"
        f"Bin Information : (#{bin_number})\n"
        "↳ Vendor: Visa\n"
        "↳ Type: DEBIT\n"
        "↳ Level: CLASSIC\n"
        "↳ Bank:\n"
        " ↳ USA\n"
        "↳ Country:\n"
        " ↳ UNITED STATES - USD - 🇺🇸"
    )

    return message

async def post_to_channel(message):
    await application.bot.send_message(chat_id=CHANNEL_USERNAME, text=message)

def job():
    visa_message = generate_visa()
    loop = asyncio.new_event_loop()  
    asyncio.set_event_loop(loop)  
    loop.run_until_complete(post_to_channel(visa_message))  

def run_scheduler():
    schedule.every(5).seconds.do(job)  
    while True:
        schedule.run_pending()
        time.sleep(1)

def start_scheduler():
    scheduler_thread = threading.Thread(target=run_scheduler)
    scheduler_thread.start()

if __name__ == '__main__':
    application.add_handler(CommandHandler("start", start))
    start_scheduler()
    
    application.run_webhook(
        listen="0.0.0.0",
        port=8080,
        url_path=TOKEN,  
        webhook_url='https://7d30-41-45-152-143.ngrok-free.app/' + TOKEN
    )
