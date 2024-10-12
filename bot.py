from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# ضع التوكن الخاص بك هنا
TOKEN = '7138102548:AAFcY-t0XSHsAhPxGkyPHRlAL9Xxb8-0GPk'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am your bot.')

def main():
    # إعداد البوت باستخدام التوكن
    updater = Updater(TOKEN7138102548:AAFcY-t0XSHsAhPxGkyPHRlAL9Xxb8-0GPk)

    # الحصول على الموزع لإضافة معالجات الأوامر
    dispatcher = updater.dispatcher

    # إضافة معالج للأمر /start
    dispatcher.add_handler(CommandHandler("start", start))

    # بدء البوت
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
