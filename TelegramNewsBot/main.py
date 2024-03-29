import Constants as keys
from telegram.ext import *
import Responses as R


def start_command(update, context):
    update.message.reply_text('you can do /news to get the latest news.')


def help_command(update, context):
    update.message.reply_text('To get the latest news you can use /news')


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.get_news_responses(text)

    update.message.reply_text(response, parse_mode='HTML')


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    print('Bot started..')
    updater = Updater(keys.API_KEY)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('start', help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
