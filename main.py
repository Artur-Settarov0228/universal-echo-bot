from config import TOKEN
from telegram.ext import Updater, MessageHandler, Filters
from handlers import hanler_photo, hanler_text


def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.photo, hanler_photo))
    dispatcher.add_handler(MessageHandler(Filters.text, hanler_text))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

