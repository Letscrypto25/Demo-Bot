# bot.py
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, CallbackQueryHandler,
    ContextTypes, MessageHandler, filters
)
from handlers import order
from utils.session import set_user_mode, get_user_mode, clear_user_mode

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# === /start command ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to the Demo Bot!\n"
        "This is a modular bot with interactive buttons for different flows.\n\n"
        "Choose a template to get started:\n"
        "➡️ /order - Order Menu\n"
        "➡️ /deliveries - Delivery Bot\n"
        "➡️ /stock - Stock Management\n"
        "➡️ /help - General Help"
    )

# === Main setup ===
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # === Command triggers ===
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("order", order.order_menu))  # Button-based menu

    # === Callback button responses ===
    app.add_handler(CallbackQueryHandler(order.order_callback))

    print("✅ Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
