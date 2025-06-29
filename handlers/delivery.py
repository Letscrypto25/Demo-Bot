# handlers/delivery.py
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes
from menus import get_delivery_keyboard, get_delivery_back_keyboard
from handlers.order import order_menu  # optional if needed

# === Called by /deliveries or callback ===
async def delivery_menu(update: Update, context: ContextTypes.DEFAULT_TYPE, from_callback=False):
    keyboard = get_delivery_keyboard()

    if from_callback:
        await update.callback_query.edit_message_text(
            "🚚 *Delivery Menu:*\nSelect an option:",
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    else:
        await update.message.reply_text(
            "🚚 *Delivery Menu:*\nSelect an option:",
            parse_mode="Markdown",
            reply_markup=keyboard
        )


# === Callback handler ===
async def delivery_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    data = query.data
    await query.answer()

    if data == "delivery_view":
        await query.edit_message_text(
            text="📦 *Your Deliveries:*\n- #1234: Out for delivery\n- #1235: Delivered ✅",
            parse_mode="Markdown",
            reply_markup=get_delivery_back_keyboard()
        )

    elif data == "delivery_track":
        await query.edit_message_text(
            text="📍 *Tracking:* Order #1234 is 6 minutes away.",
            parse_mode="Markdown",
            reply_markup=get_delivery_back_keyboard()
        )

    elif data == "delivery_history":
        await query.edit_message_text(
            text="📜 *Delivery History:*\n- #1235: Delivered 2 days ago\n- #1233: Delivered last week",
            parse_mode="Markdown",
            reply_markup=get_delivery_back_keyboard()
        )

    elif data == "delivery_schedule":
        await query.edit_message_text(
            text="🗓 *Schedule a Delivery:*\n\nSend a message like:\n`Tomorrow 2PM - 1x Cake + 1x Soda`",
            parse_mode="Markdown",
            reply_markup=get_delivery_back_keyboard()
        )

    elif data == "delivery_contact":
        await query.edit_message_text(
            text="📞 *Delivery Contact:*\n- Phone: 065 982 1883\n- Telegram: @Letscrypto_bot",
            parse_mode="Markdown",
            reply_markup=get_delivery_back_keyboard()
        )

    elif data == "delivery_back":
        await delivery_menu(update, context, from_callback=True)

    elif data == "start_back":
        from bot import start
        await start(update, context)
