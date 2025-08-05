from telegram import Update, ParseMode, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from telegram.ext import CallbackContext



def handler_main_menu(update: Update, context: CallbackContext):
    update.message.reply_markdown_v2(
        text="> Siz *Bosh Menu* ni tanladingiz",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton('Mahsulotlar'), KeyboardButton('Texnikalar')],
                [KeyboardButton('Modellari')]
            ],
            resize_keyboard=True,
            one_time_keyboard=True,
        )
    )

def start(update: Update, context: CallbackContext):
    bot = context.bot
    user = update.effective_user
    bot.send_message(
        chat_id=user.id,
        text='Menu tanlang:',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(
                                'Bosh Menu',
                                web_app=WebAppInfo(url="https://kun.uz")
                                ),
                  KeyboardButton('Buyurtma berish')
                  ],

                [KeyboardButton('Location', request_location=True), KeyboardButton('Contact', request_contact=True)],
                
                [
                    KeyboardButton('My gov',
                                   web_app=WebAppInfo(url="https://my.gov.uz/")
                        )
                ]
            ],
            resize_keyboard=True
        )
    )


def handler_photo(update : Update, context : CallbackContext):
    photo = update.message.photo[-1]
    update.message.reply_photo(
        photo=photo,
        caption="siz <b> yuborgan rasm</b>",
        parse_mode=ParseMode.HTML
    )

def handler_text(update : Update , context : CallbackContext):
    update.message.reply_markdown_v2(
        text= f"linkni ustiga bosing [inline URL](http://www.example.com/)"
    )
