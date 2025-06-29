# handlers/help.py

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes
from menus import get_help_keyboard, get_help_back_keyboard

async def help_menu(update: Update, context: ContextTypes.DEFAULT_TYPE, from_callback=False):
    if from_callback:
        await update.callback_query.edit_message_text(
            "🧠 General Help:\nSelect a topic for more info:",
            reply_markup=get_help_keyboard()
        )
    else:
        await update.message.reply_text(
            "🧠 General Help:\nSelect a topic for more info:",
            reply_markup=get_help_keyboard()
        )

async def help_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "help_how_to_use":
        await query.edit_message_text(
            "❓ *How to Use This Bot:*\n\nJust follow the buttons to interact with each module (Orders, Delivery, Stock).",
            parse_mode="Markdown",
            reply_markup=get_help_back_keyboard()
        )

    elif data == "help_features":
        await query.edit_message_text(
            "🛠 *Features:*\n\n- Modular design\n- Reusable structure\n- Inline button navigation\n- Ready for deployment",
            parse_mode="Markdown",
            reply_markup=get_help_back_keyboard()
        )

    elif data == "help_support":
        await query.edit_message_text(
            "📞 *Support:*\n\n- Dev: @Letscrypto_bot\n- GitHub: https://github.com/Letscrypto25",
            parse_mode="Markdown",
            reply_markup=get_help_back_keyboard()
        )

    elif data == "help_back":
        await help_menu(update, context, from_callback=True)
