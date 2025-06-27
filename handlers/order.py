# handlers/order.py

from telegram import Update
from telegram.ext import ContextTypes

async def order_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📦 Order Menu:\n"
        "1. 🧁 Place Order\n"
        "2. 📋 View Past Orders\n"
        "3. 🔙 Back to Main"
    )
