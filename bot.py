# bot.py

import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
)
from handlers import order
from utils.session import set_user_mode, get_user_mode, clear_user_mode

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to the Demo Bot!\n"
        "Choose a template type:\n"
        "/order - Order Menu\n"
        "/deliveries - Delivery Bot\n"
        "/stock - Stock Management\n"
        "/help - General Help"
    )

# Add routing logic
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("order", order.order_menu))

    print("✅ Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
