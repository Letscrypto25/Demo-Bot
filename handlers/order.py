from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes
from bot import start  # To go back to main menu
from handlers.order import order_menu  # To go back to order menu

async def order_menu(update: Update, context: ContextTypes.DEFAULT_TYPE, from_callback=False):
    keyboard = [
        [InlineKeyboardButton("🍕 View Menu", callback_data="order_view_menu")],
        [InlineKeyboardButton("📝 Place Order", callback_data="order_place")],
        [InlineKeyboardButton("📦 My Orders", callback_data="order_my_orders")],
        [InlineKeyboardButton("⏱ Wait Time", callback_data="order_wait_time")],
        [InlineKeyboardButton("📞 Contact", callback_data="order_contact")],
        [InlineKeyboardButton("🔙 Back to Main Menu", callback_data="start_back")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    if from_callback:
        await update.callback_query.edit_message_text(
            "🧾 Order Menu:\nPlease choose an option below:",
            reply_markup=reply_markup
        )
    else:
        await update.message.reply_text(
            "🧾 Order Menu:\nPlease choose an option below:",
            reply_markup=reply_markup
        )


async def order_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    back_button = [[InlineKeyboardButton("🔙 Back to Order Menu", callback_data="order_back")]]

    if data == "order_view_menu":
        await query.edit_message_text(
            text="📋 *Menu Preview:*\n\n"
                 "- Margherita Pizza – R85\n"
                 "- Chicken Mayo – R95\n"
                 "- Garlic Bread – R30\n"
                 "- Choc Cupcake – R25\n"
                 "- Lemonade – R15",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(back_button)
        )

    elif data == "order_place":
        await query.edit_message_text(
            text="📝 *Place Order:*\n\nSend your order like:\n`1x Pizza + 2x Lemonade`",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(back_button)
        )

    elif data == "order_my_orders":
        await query.edit_message_text(
            text="📦 You currently have no active orders.",
            reply_markup=InlineKeyboardMarkup(back_button)
        )

    elif data == "order_wait_time":
        await query.edit_message_text(
            text="⏱ Average wait time: *15–25 minutes*",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(back_button)
        )

    elif data == "order_contact":
        await query.edit_message_text(
            text="📞 *Contact Us:*\n- Phone: 065 982 1883\n- Telegram: @Letscrypto_bot",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(back_button)
        )

    elif data == "order_back":
        # Go back to order menu
        await order_menu(update, context, from_callback=True)

    elif data == "start_back":
        # Go back to main /start menu
        await start(update, context)
