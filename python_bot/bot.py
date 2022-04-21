from telegram  import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
startcha = Updater("5266879331:AAHI5C_qtQfSDA0xElAY5-ztKF5R0R10cLQ")


def salom(update: Update, message: CallbackContext):
    print(message)
    update.message.reply_text("Salom")


def newfunc(update: Update, message: CallbackContext):
    update.message.reply_text("Salom")

print("Dastur ishladi")
startcha.dispatcher.add_handler(CommandHandler("hello",salom ))
startcha.dispatcher.add_handler(CommandHandler("chiqar", newfunc))
startcha.start_polling()
startcha.idle()