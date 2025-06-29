# handlers/stock.py

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

# === Show stock management menu ===
async def stock_menu(update: Update, context: ContextTypes.DEFAULT_TYPE, from_callback=False):
    keyboard = [
        [InlineKeyboardButton("📦 View Stock", callback_data="stock_view")],
        [InlineKeyboardButton("➕ Add Stock", callback_data="stock_add")],
        [InlineKeyboardButton("➖ Remove Stock", callback_data="stock_remove")],
        [InlineKeyboardButton("🧾 Stock Report", callback_data="stock_report")],
        [InlineKeyboardButton("🔙 Back to Main Menu", callback_data="start_back")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if from_callback and update.callback_query:
        await update.callback_query.edit_message_text(
            "📊 Stock Management Menu:",
            reply_markup=reply_markup
        )
    elif update.message:
        await update.message.reply_text(
            "📊 Stock Management Menu:",
            reply_markup=reply_markup
        )

# === Handle button presses ===
async def stock_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    back_button = [[InlineKeyboardButton("🔙 Back to Stock Menu", callback_data="stock_back")]]

    if data == "stock_view":
        await query.edit_message_text(
            text="📦 Current Stock:\n\n- Pizza Dough: 20\n- Tomato Sauce: 15\n- Cheese: 12\n- Boxes: 40",
            reply_markup=InlineKeyboardMarkup(back_button)
        )

    elif data == "stock_add":
        await query.edit_message_text(
            text="➕ To add stock, reply like:\n`+5 Cheese`\n(Feature simulated for demo)",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(back_button)
        )

    elif data == "stock_remove":
        await query.edit_message_text(
            text="➖ To remove stock, reply like:\n`-2 Boxes`\n(Feature simulated for demo)",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(back_button)
        )

    elif data == "stock_report":
        await query.edit_message_text(
            text="🧾 Stock Report:\n\n- Low on Cheese\n- Tomato Sauce OK\n- Boxes Sufficient",
            reply_markup=InlineKeyboardMarkup(back_button)
        )

    elif data == "stock_back":
        await stock_menu(update, context, from_callback=True)
