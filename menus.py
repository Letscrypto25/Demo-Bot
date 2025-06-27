# menus.py
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def get_start_keyboard():
    keyboard = [
        [InlineKeyboardButton("🧾 Order Menu", callback_data="start_order")],
        [InlineKeyboardButton("🚚 Delivery Bot", callback_data="start_delivery")],
        [InlineKeyboardButton("📦 Stock Management", callback_data="start_stock")],
        [InlineKeyboardButton("❓ General Help", callback_data="start_help")]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_order_keyboard():
    keyboard = [
        [InlineKeyboardButton("🍕 View Menu", callback_data="order_view_menu")],
        [InlineKeyboardButton("📝 Place Order", callback_data="order_place")],
        [InlineKeyboardButton("📦 My Orders", callback_data="order_my_orders")],
        [InlineKeyboardButton("⏱ Wait Time", callback_data="order_wait_time")],
        [InlineKeyboardButton("📞 Contact", callback_data="order_contact")],
        [InlineKeyboardButton("🔙 Back to Main Menu", callback_data="start_back")]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_order_back_keyboard():
    keyboard = [
        [InlineKeyboardButton("🔙 Back to Order Menu", callback_data="order_back")]
    ]
    return InlineKeyboardMarkup(keyboard)
