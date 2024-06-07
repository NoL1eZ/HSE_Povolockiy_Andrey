from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Define the sections of the directory
MAIN_MENU, SECTION_1, SECTION_2, SECTION_3 = range(4)

def start(update: Update, context: CallbackContext) -> None:
    reply_markup = ReplyKeyboardMarkup(main_menu_keyboard(), resize_keyboard=True)
    update.message.reply_text("Добро пожаловать в бот-справочник! Выберите раздел:", reply_markup=reply_markup)

def main_menu_keyboard():
    return [
        [KeyboardButton("Раздел 1")],
        [KeyboardButton("Раздел 2")],
        [KeyboardButton("Раздел 3")]
    ]

def section_keyboard():
    return [
        [KeyboardButton("Главное меню")],
        [KeyboardButton("Дополнительная информация")]
    ]

def section_1(update: Update, context: CallbackContext) -> None:
    reply_markup = ReplyKeyboardMarkup(section_keyboard(), resize_keyboard=True)
    update.message.reply_text("Вы выбрали Раздел 1. Здесь будет информация по Разделу 1.", reply_markup=reply_markup)

def section_2(update: Update, context: CallbackContext) -> None:
    reply_markup = ReplyKeyboardMarkup(section_keyboard(), resize_keyboard=True)
    update.message.reply_text("Вы выбрали Раздел 2. Здесь будет информация по Разделу 2.", reply_markup=reply_markup)

def section_3(update: Update, context: CallbackContext) -> None:
    reply_markup = ReplyKeyboardMarkup(section_keyboard(), resize_keyboard=True)
    update.message.reply_text("Вы выбрали Раздел 3. Здесь будет информация по Разделу 3.", reply_markup=reply_markup)

def handle_message(update: Update, context: CallbackContext) -> None:
    text = update.message.text

    if text == "Главное меню":
        reply_markup = ReplyKeyboardMarkup(main_menu_keyboard(), resize_keyboard=True)
        update.message.reply_text("Вы вернулись в главное меню. Выберите раздел:", reply_markup=reply_markup)
    elif text == "Раздел 1":
        section_1(update, context)
    elif text == "Раздел 2":
        section_2(update, context)
    elif text == "Раздел 3":
        section_3(update, context)
    elif text == "Дополнительная информация":
        update.message.reply_text("Здесь будет дополнительная информация.")
    else:
        update.message.reply_text("Пожалуйста, выберите один из доступных разделов.")

def main() -> None:
    updater = Updater("YOUR_TELEGRAM_BOT_TOKEN")

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()