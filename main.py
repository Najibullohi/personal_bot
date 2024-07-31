from telegram.ext import Updator, CommandHandler

TOKEN = "7311265297:AAH1FR-hC57hIW3IvfwlKFdAnZ-8tn_zv-w"

def start(update, context):
    message = "I am Najibullo Welcome to my Bot"

    with open('125.jpg','rb') as file:
        update.message.replay_photo(file,message)
      

def main():
    updater = Updator(TOKEN)
    dispatcher = updater.dispatcher 

    dispatcher.add_handler(CommandHandler('start',start))

    updater.start_polling()
    updater.idle()
    
if __name__=='__main__':
    main()
