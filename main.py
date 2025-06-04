from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

welcome_messages = {
    'fa': "سلام! خوش آمدید.",
    'en': "Hello! Welcome.",
    'ar': "مرحبا! أهلاً وسهلاً.",
    'ru': "Привет! Добро пожаловать."
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_lang = update.message.from_user.language_code
    msg = welcome_messages.get(user_lang, welcome_messages['en'])
    await update.message.reply_text(msg)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_lang = update.message.from_user.language_code
    msg = welcome_messages.get(user_lang, welcome_messages['en'])
    await update.message.reply_text(msg)

async def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    print("Bot is running...")
    await app.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
