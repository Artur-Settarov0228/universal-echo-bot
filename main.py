from config import TOKEN
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from handlers import handler_photo, handler_main_menu, start, handler_text, remove_keyboard, send_inline_keyboard, about_us, orqaga


def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler(['start', 'boshlash'], start))

    dispatcher.add_handler(MessageHandler(Filters.photo, handler_photo))
    dispatcher.add_handler(MessageHandler(Filters.text('Bosh Menu'), handler_main_menu))
    dispatcher.add_handler(MessageHandler(Filters.text, handler_text))
    dispatcher.add_handler(MessageHandler(Filters.text('Close'), remove_keyboard))
    dispatcher.add_handler(MessageHandler(Filters.text ('Buyurtma berish'), send_inline_keyboard))
    dispatcher.add_handler(MessageHandler(Filters.text ('Biz haqimizda'), about_us))
    dispatcher.add_handler(MessageHandler(Filters.text(' Orqaga'), orqaga))



    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

