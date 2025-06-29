import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, CallbackQueryHandler,
    ContextTypes
)
from handlers import order, delivery, stock, help as help_handler
from menus import get_entry_keyboard, get_customer_keyboard, get_admin_keyboard
from utils.session import set_user_mode, get_user_mode, clear_user_mode

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")


# === ENTRY SCREEN ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = get_entry_keyboard()
    await update.message.reply_text(
        "👋 Welcome to the Demo Bot!\nPlease choose your role:",
        reply_markup=keyboard
    )


# === MAIN ROUTER ===
async def callback_router(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    # Entry roles
    if data == "start_customer":
        await query.edit_message_text(
            "🧍 Customer Menu:\nPlease choose an option:",
            reply_markup=get_customer_keyboard()
        )
    elif data == "start_admin":
        await query.edit_message_text(
            "👨‍🍳 Admin Panel:\nSelect what you want to manage:",
            reply_markup=get_admin_keyboard()
        )
    elif data == "start_back":
        await query.edit_message_text(
            "👋 Welcome to the Demo Bot!\nPlease choose your role:",
            reply_markup=get_entry_keyboard()
        )

    # Customer routes
    elif data == "menu_view":
        await order.order_menu(update, context, from_callback=True)
    elif data == "delivery_track":
        await delivery.delivery_menu(update, context, from_callback=True)
    elif data == "customer_contact":
        await help_handler.help_menu(update, context, from_callback=True)

    elif data.startswith("order_"):
        await order.order_callback(update, context)
    elif data.startswith("delivery_"):
        await delivery.delivery_callback(update, context)
    elif data.startswith("help_"):
        await help_handler.help_callback(update, context)

    # Admin routes
    elif data == "admin_stock":
        await stock.stock_menu(update, context, from_callback=True)
    elif data == "admin_delivery":
        await delivery.delivery_menu(update, context, from_callback=True)
    elif data == "admin_orders":
        await order.order_menu(update, context, from_callback=True)
    elif data == "admin_settings":
        await query.edit_message_text("⚙️ Settings screen coming soon...")
    elif data.startswith("stock_"):
        await stock.stock_callback(update, context)


# === MAIN APP ===
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("order", order.order_menu))
    app.add_handler(CommandHandler("delivery", delivery.delivery_menu))
    app.add_handler(CommandHandler("stock", stock.stock_menu))
    app.add_handler(CommandHandler("help", help_handler.help_menu))

    app.add_handler(CallbackQueryHandler(callback_router))

    print("✅ Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
