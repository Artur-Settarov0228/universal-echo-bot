from telegram import Update, ParseMode
from telegram.ext import CallbackContext

def hanler_photo(update : Update, context : CallbackContext):
    photo = update.message.photo[-1]
    update.message.reply_photo(
        photo=photo,
        caption="siz <b> yuborgan rasm</b>",
        parse_mode=ParseMode.HTML
    )

def hanler_text(update : Update , context : CallbackContext):
    update.message.reply_markdown_v2(
        text= f"linkni ustiga bosing [inline URL](http://www.example.com/)"
    )
