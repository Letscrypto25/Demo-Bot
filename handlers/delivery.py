from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes
from menus import get_delivery_keyboard, get_admin_delivery_keyboard

# === Called by /delivery or customer callback ===
async def delivery_menu(update: Update, context: ContextTypes.DEFAULT_TYPE, from_callback=False):
    keyboard = get_delivery_keyboard()
    text = "🚚 *Delivery Menu:*\nChoose an option below:"

    if from_callback:
        await update.callback_query.edit_message_text(text=text, parse_mode="Markdown", reply_markup=keyboard)
    else:
        await update.message.reply_text(text=text, parse_mode="Markdown", reply_markup=keyboard)


# === Called by /admin_delivery or admin callback ===
async def admin_delivery_menu(update: Update, context: ContextTypes.DEFAULT_TYPE, from_callback=False):
    keyboard = get_admin_delivery_keyboard()
    text = "👨‍🍳 *Delivery Admin Panel:*\nChoose what you want to manage:"

    if from_callback:
        await update.callback_query.edit_message_text(text=text, parse_mode="Markdown", reply_markup=keyboard)
    else:
        await update.message.reply_text(text=text, parse_mode="Markdown", reply_markup=keyboard)


# === Callback Handler ===
async def delivery_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    data = query.data
    await query.answer()

    if data == "delivery_track_status":
        await query.edit_message_text(
            text="📍 *Tracking:* Order #1234 is 6 minutes away.",
            parse_mode="Markdown",
            reply_markup=get_delivery_keyboard()
        )

    elif data == "delivery_history":
        await query.edit_message_text(
            text="📜 *Delivery History:*\n- #1235: Delivered 2 days ago\n- #1233: Delivered last week",
            parse_mode="Markdown",
            reply_markup=get_delivery_keyboard()
        )

    elif data == "delivery_contact":
        await query.edit_message_text(
            text="📞 *Delivery Contact:*\n- Phone: 065 982 1883\n- Telegram: @Letscrypto_bot",
            parse_mode="Markdown",
            reply_markup=get_delivery_keyboard()
        )

    elif data == "admin_delivery_incoming":
        await query.edit_message_text(
            text="📦 *Incoming Deliveries:*\n- #1236: 10 minutes away\n- #1237: Preparing...",
            parse_mode="Markdown",
            reply_markup=get_admin_delivery_keyboard()
        )

    elif data == "admin_delivery_schedule":
        await query.edit_message_text(
            text="🗓 *Schedule Pickup:*\nSend format:\n`Tomorrow 3PM – Pickup 2x Boxes`",
            parse_mode="Markdown",
            reply_markup=get_admin_delivery_keyboard()
        )

    elif data == "admin_delivery_drivers":
        await query.edit_message_text(
            text="👨‍✈️ *Drivers List:*\n- John (Online)\n- Kate (Offline)",
            parse_mode="Markdown",
            reply_markup=get_admin_delivery_keyboard()
        )

    elif data == "start_customer":
        await delivery_menu(update, context, from_callback=True)

    elif data == "start_admin":
        await admin_delivery_menu(update, context, from_callback=True)
