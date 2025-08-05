from config import TOKEN
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from handlers import handler_photo, handler_main_menu, start, handler_text


def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler(['start', 'boshlash'], start))

    dispatcher.add_handler(MessageHandler(Filters.photo, handler_photo))
    dispatcher.add_handler(MessageHandler(Filters.text('Buyurtma berish'), handler_main_menu))
    dispatcher.add_handler(MessageHandler(Filters.text, handler_text))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

