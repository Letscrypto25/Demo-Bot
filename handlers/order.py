# handlers/order.py

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackQueryHandler

# Main order menu
async def order_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🧁 Place Order", callback_data="place_order")],
        [InlineKeyboardButton("📋 View Past Orders", callback_data="view_orders")],
        [InlineKeyboardButton("🔙 Back to Main", callback_data="back_main")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("📦 *Order Menu:*", reply_markup=reply_markup, parse_mode="Markdown")

# Callback query logic
async def order_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "place_order":
        await query.edit_message_text("🍰 What would you like to order?\n(This is a demo. Type your item.)")

    elif query.data == "view_orders":
        await query.edit_message_text("📋 You have no past orders. (Demo mode)")

    elif query.data == "back_main":
        await query.edit_message_text("🔙 Back to main menu.\nUse /start to choose a new path.")
