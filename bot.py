from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import schedule
import time
import threading
from random import choice, randint
import colorama
import asyncio
import emoji

colorama.init(autoreset=True)

TOKEN = '7138102548:AAFcY-t0XSHsAhPxGkyPHRlAL9Xxb8-0GPk'  
CHANNEL_USERNAME = '@walletveli'  
application = ApplicationBuilder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hello! I am your bot.')

def generate_visa():
    bin_numbers = ['455225', '537410', '414763', '434257', '519699']
    bin_number = choice(bin_numbers)
    numofvisa = 16
    nums = '0123456789'
    
    
    visa = bin_number + ''.join(choice(nums) for _ in range(numofvisa - len(bin_number)))

    
    expiry_year = randint(2024, 2030)
    expiry_month = randint(1, 12)
    expiry = f"{expiry_month:02d}|{expiry_year}"  

    cvc = ''.join(choice('0123456789') for _ in range(3))

    countries = {
        "USA": "🇺🇸",
        "Canada": "🇨🇦",
        "UK": "🇬🇧",
        "Germany": "🇩🇪",
        "France": "🇫🇷",
        "Italy": "🇮🇹",
        "Spain": "🇪🇸",
        "Australia": "🇦🇺",
        "Egypt": "🇪🇬",
        "Saudi Arabia": "🇸🇦",
        "United Arab Emirates": "🇦🇪",
        "Japan": "🇯🇵",
        "China": "🇨🇳",
        "India": "🇮🇳",
    }

    country_name = choice(list(countries.keys()))
    country_flag = countries[country_name]

    message = (
        "Approved!✅\n\n"
        f"• 𝗖𝗔𝗥𝗗 : {visa}|{expiry}|{cvc}\n"
        "• 𝐆𝐚𝐭𝐞𝐰𝐚𝐲 : Stripe Auth 2!!\n"
        "• 𝗥𝗘𝗦𝗣𝗢𝗡𝗦𝗘 : [CVV CARD - Status -> Succeeded!]\n\n"
        "• 𝗜𝗡𝗙𝗢: : VISA - DEBIT - VISA CLASSIC\n"
        f"• 𝗜𝗦𝗦𝗨𝗘𝗥 : Green Dot Bank Dba Bonneville Bank\n"
        f"• 𝗖𝗼𝘂𝗻𝘁𝗿𝘆 : {country_name} {country_flag}"
    )

    return message

async def post_to_channel(message):
    try:
        await asyncio.wait_for(application.bot.send_message(chat_id=CHANNEL_USERNAME, text=message), timeout=10)  
    except asyncio.TimeoutError:
        print("The request timed out!")
    except Exception as e:
        print(f"An error occurred: {e}")

def job():
    visa_message = generate_visa()
    asyncio.run(post_to_channel(visa_message))  

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
