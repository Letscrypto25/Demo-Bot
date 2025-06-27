# handlers/order.py
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

# Main menu buttons under /order
async def order_menu_callback(query, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🍕 View Menu", callback_data="order_view_menu")],
        [InlineKeyboardButton("📝 Place Order", callback_data="order_place")],
        [InlineKeyboardButton("📦 My Orders", callback_data="order_my_orders")],
        [InlineKeyboardButton("⏱ Estimated Wait Time", callback_data="order_wait_time")],
        [InlineKeyboardButton("📞 Contact Us", callback_data="order_contact")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(
        text="🧾 Order Menu:\nPlease choose an option below:",
        reply_markup=reply_markup
    )


# Handle button interactions for /order
async def order_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "order_view_menu":
        await query.edit_message_text(
            text="📋 *Menu Preview:*\n\n"
                 "- Margherita Pizza – R85\n"
                 "- Chicken Mayo – R95\n"
                 "- Garlic Bread – R30\n"
                 "- Choc Cupcake – R25\n"
                 "- Lemonade – R15",
            parse_mode="Markdown"
        )

    elif data == "order_place":
        await query.edit_message_text(
            text="📝 *Order Placement:*\n\nPlease type your order in the format:\n\n`1x Chicken Mayo + 2x Lemonade`",
            parse_mode="Markdown"
        )

    elif data == "order_my_orders":
        await query.edit_message_text(
            text="📦 You have no active orders.\n\n(You’ll see your order summary here once placed.)"
        )

    elif data == "order_wait_time":
        await query.edit_message_text(
            text="⏱ Current average wait time: *15–25 minutes*.\n(Subject to change based on order volume.)",
            parse_mode="Markdown"
        )

    elif data == "order_contact":
        await query.edit_message_text(
            text="📞 *Contact Info:*\n\n"
                 "- Phone: 065 982 1883\n"
                 "- Email: letscrypto25@gmail.com\n"
                 "- Telegram: @Letscrypto_bot",
            parse_mode="Markdown"
        )
