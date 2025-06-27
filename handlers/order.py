# handlers/order.py

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

# Direct callback from button
async def order_menu_callback(query, context):
    keyboard = [
        [InlineKeyboardButton("🧁 Place Order", callback_data="place_order")],
        [InlineKeyboardButton("📋 View Past Orders", callback_data="view_orders")],
        [InlineKeyboardButton("🔙 Back to Main", callback_data="back_main")]
    ]
    markup = InlineKeyboardMarkup(keyboard)
    await query.edit_message_text("📦 *Order Menu:*", reply_markup=markup, parse_mode="Markdown")

# Existing fallback for command-based (optional)
async def order_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await order_menu_callback(update.message, context)
