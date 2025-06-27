import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, CallbackQueryHandler,
    ContextTypes
)
from handlers import order
from utils.session import set_user_mode, get_user_mode, clear_user_mode
from menus import get_start_keyboard

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = get_start_keyboard()
    if update.message:
        await update.message.reply_text(
            "👋 Welcome to the Demo Bot!\n"
            "This is a modular bot with interactive buttons for different flows.\n\n"
            "Choose a template to get started:",
            reply_markup=keyboard
        )
    else:
        # Called from callback query
        await update.callback_query.edit_message_text(
            "👋 Welcome to the Demo Bot!\n"
            "This is a modular bot with interactive buttons for different flows.\n\n"
            "Choose a template to get started:",
            reply_markup=keyboard
        )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("order", order.order_menu))
    app.add_handler(CallbackQueryHandler(order.order_callback))
    app.add_handler(CallbackQueryHandler(order.start_callback, pattern="^start_"))

    print("✅ Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
