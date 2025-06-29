from telegram import Update
from telegram.ext import ContextTypes
from menus import get_order_keyboard, get_order_back_keyboard
from handlers.cart import add_to_cart  # Optional if you're implementing cart interaction

# === Show Order Menu ===
async def order_menu(update: Update, context: ContextTypes.DEFAULT_TYPE, from_callback=False):
    keyboard = get_order_keyboard()
    message = "🧾 Order Menu:\nPlease choose an option below:"
    if from_callback:
        await update.callback_query.edit_message_text(message, reply_markup=keyboard)
    else:
        await update.message.reply_text(message, reply_markup=keyboard)


# === Handle Order Menu Callbacks ===
async def order_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data
    back_keyboard = get_order_back_keyboard()

    if data == "order_view_menu":
        menu_text = "📋 *Menu Preview:*\n\n"
        menu_items = [
            ("Margherita Pizza", "R85"),
            ("Chicken Mayo", "R95"),
            ("Garlic Bread", "R30"),
            ("Choc Cupcake", "R25"),
            ("Lemonade", "R15")
        ]

        buttons = []
        for name, price in menu_items:
            menu_text += f"- {name} – {price}\n"
            buttons.append([InlineKeyboardButton(f"➕ Add {name}", callback_data=f"cart_add_{name.replace(' ', '_')}")])
        buttons.append([InlineKeyboardButton("🔙 Back to Order Menu", callback_data="order_back")])

        await query.edit_message_text(
            text=menu_text,
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(buttons)
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


# === Optional: Start-related router (if separated from bot.py) ===
async def start_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "start_order":
        await order_menu(update, context, from_callback=True)
    elif data == "start_back":
        from bot import start  # Avoid circular import in real production; consider refactoring
        await start(update, context)
