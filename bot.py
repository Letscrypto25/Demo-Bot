import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, CallbackQueryHandler,
    ContextTypes
)
from handlers import order, delivery, stock, help as help_handler
from menus import (
    get_entry_keyboard, get_customer_keyboard, get_admin_keyboard,
    get_admin_delivery_keyboard, get_settings_back_keyboard
)

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")


# === ENTRY SCREEN ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = get_entry_keyboard()
    await update.message.reply_text(
        "👋 Welcome to the Demo Bot!\nPlease choose your role:",
        reply_markup=keyboard
    )


# === MAIN CALLBACK ROUTER ===
async def callback_router(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    # Entry / Role Switching
    if data in ("start_customer", "back_to_entry"):
        await query.edit_message_text(
            "🧍 Customer Menu:\nPlease choose an option:",
            reply_markup=get_customer_keyboard()
        )
    elif data == "start_admin":
        await query.edit_message_text(
            "👨‍🍳 Admin Panel:\nSelect what you want to manage:",
            reply_markup=get_admin_keyboard()
        )

    # === CUSTOMER ROUTES ===
    elif data == "menu_view":
        await order.order_menu(update, context, from_callback=True)
    elif data == "cart_view":
        await query.edit_message_text("🛒 Cart is currently empty.")
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

    # === ADMIN ROUTES ===
    elif data == "admin_orders":
        await order.order_menu(update, context, from_callback=True)
    elif data == "admin_stock":
        await stock.stock_menu(update, context, from_callback=True)
    elif data == "admin_delivery":
        await query.edit_message_text(
            "🚚 Delivery Management Options:",
            reply_markup=get_admin_delivery_keyboard()
        )
    elif data == "admin_settings":
        await query.edit_message_text(
            "⚙️ Settings screen coming soon...",
            reply_markup=get_settings_back_keyboard()
        )

    elif data.startswith("stock_"):
        await stock.stock_callback(update, context)


# === MAIN APP INIT ===
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Command entry
    app.add_handler(CommandHandler("start", start))

    # Button handler
    app.add_handler(CallbackQueryHandler(callback_router))

    print("✅ Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
