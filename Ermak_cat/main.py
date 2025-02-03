import os
import random
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from responses import ANSWERS
from utils.errors import ERROR_PHRASES

load_dotenv()
TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = "Привет! Я твой друг-Почемучка! 🎉 Задай мне вопрос, например: 'Почему небо голубое?' 🌌"
    await update.message.reply_text(welcome_text)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.lower()
    response = ANSWERS.get(user_text, random.choice(ERROR_PHRASES))
    await update.message.reply_text(response)

async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    error_msg = "🔧 Упс! Мои шестерёнки застряли... Попробуй позже! 💖"
    await update.message.reply_text(error_msg)

if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    # app.add_handler(CommandHandler("start", start))
    # app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    # app.add_error_handler(error_handler)
    app.run_polling()