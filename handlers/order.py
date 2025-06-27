from telegram import Update
from telegram.ext import ContextTypes
from menus import get_order_keyboard, get_order_back_keyboard
from bot import start  # only if necessary, else avoid import to reduce coupling

async def order_menu(update: Update, context: ContextTypes.DEFAULT_TYPE, from_callback=False):
    keyboard = get_order_keyboard()
    if from_callback:
        await update.callback_query.edit_message_text(
            "🧾 Order Menu:\nPlease choose an option below:",
            reply_markup=keyboard
        )
    else:
        await update.message.reply_text(
            "🧾 Order Menu:\nPlease choose an option below:",
            reply_markup=keyboard
        )

async def order_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    back_keyboard = get_order_back_keyboard()

    if data == "order_view_menu":
        await query.edit_message_text(
            "📋 *Menu Preview:*\n\n"
            "- Margherita Pizza – R85\n"
            "- Chicken Mayo – R95\n"
            "- Garlic Bread – R30\n"
            "- Choc Cupcake – R25\n"
            "- Lemonade – R15",
            parse_mode="Markdown",
            reply_markup=back_keyboard
        )

    elif data == "order_place":
        await query.edit_message_text(
            "📝 *Place Order:*\n\nSend your order like:\n`1x Pizza + 2x Lemonade`",
            parse_mode="Markdown",
            reply_markup=back_keyboard
        )

    elif data == "order_my_orders":
        await query.edit_message_text(
            "📦 You currently have no active orders.",
            reply_markup=back_keyboard
        )

    elif data == "order_wait_time":
        await query.edit_message_text(
            "⏱ Average wait time: *15–25 minutes*",
            parse_mode="Markdown",
            reply_markup=back_keyboard
        )

    elif data == "order_contact":
        await query.edit_message_text(
            "📞 *Contact Us:*\n- Phone: 065 982 1883\n- Telegram: @Letscrypto_bot",
            parse_mode="Markdown",
            reply_markup=back_keyboard
        )

    elif data == "order_back":
        await order_menu(update, context, from_callback=True)

async def start_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "start_back":
        await start(update, context)

    elif data == "start_order":
        await order_menu(update, context, from_callback=True)

    # You can add handlers for start_delivery, start_stock, start_help here too
