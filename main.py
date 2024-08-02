from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext

TOKEN = "7311265297:AAH1FR-hC57hIW3IvfwlKFdAnZ-8tn_zv-w"

def start(update: Update, context: CallbackContext) -> None:
    message = ('I am Najibullo. Welcome to my Bot.' 
               '\n\n /contact - Send my contact\n'
               '/talk - Speak to me\n'
               '/quiz - Start the quiz')

    with open('125.jpg', 'rb') as file:
        update.message.reply_photo(file, caption=message)

def contact(update: Update, context: CallbackContext) -> None:
    message = "985 09 4218"
    update.message.reply_text(message)

def talk(update: Update, context: CallbackContext) -> None:
    message = "I will speak to you later"
    update.message.reply_text(message)

def quiz(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("What is the capital of France?", callback_data='capital_france')],
        [InlineKeyboardButton("What is 2 + 2?", callback_data='math')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Welcome to the quiz! Choose a question:', reply_markup=reply_markup)

def button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    if query.data == 'capital_france':
        keyboard = [
            [InlineKeyboardButton("1. Berlin", callback_data='wrong')],
            [InlineKeyboardButton("2. Paris", callback_data='correct')],
            [InlineKeyboardButton("3. Madrid", callback_data='wrong')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text="What is the capital of France?", reply_markup=reply_markup)

    elif query.data == 'math':
        keyboard = [
            [InlineKeyboardButton("1. 3", callback_data='wrong')],
            [InlineKeyboardButton("2. 4", callback_data='correct')],
            [InlineKeyboardButton("3. 5", callback_data='wrong')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text(text="What is 2 + 2?", reply_markup=reply_markup)

    elif query.data == 'correct':
        query.edit_message_text(text="Correct! 🎉")
    elif query.data == 'wrong':
        query.edit_message_text(text="Wrong answer. Try again!")

def main() -> None:
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("contact", contact))
    dp.add_handler(CommandHandler("talk", talk))
    dp.add_handler(CommandHandler("quiz", quiz))
    dp.add_handler(CallbackQueryHandler(button))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()