import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, CallbackQueryHandler,
    ContextTypes
)
from handlers import order, delivery
from menus import get_start_keyboard
from utils.session import set_user_mode, get_user_mode, clear_user_mode

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")


# === START SCREEN ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("▶️ Start Bot", callback_data="start_main")]
    ])
    await update.message.reply_text(
        "👋 Welcome to the Demo Bot!\nClick below to begin:",
        reply_markup=keyboard
    )


# === MAIN MENU ===
async def start_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = get_start_keyboard()
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(
        "🚀 Choose a template to get started:",
        reply_markup=keyboard
    )


# === CALLBACK ROUTER ===
async def callback_router(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    # Main start routing
    if data == "start_main":
        await start_main_menu(update, context)

    elif data == "start_order":
        await order.order_menu(update, context, from_callback=True)

    elif data == "start_delivery":
        await delivery.delivery_menu(update, context, from_callback=True)

    elif data == "start_back":
        await start_main_menu(update, context)

    # Pass to modules
    elif data.startswith("order_"):
        await order.order_callback(update, context)

    elif data.startswith("delivery_"):
        await delivery.delivery_callback(update, context)


# === MAIN APP ===
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("order", order.order_menu))
    app.add_handler(CommandHandler("delivery", delivery.delivery_menu))

    app.add_handler(CallbackQueryHandler(callback_router))  # Unified callback router

    print("✅ Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
