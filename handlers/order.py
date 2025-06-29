from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes
from menus import get_order_keyboard, get_order_back_keyboard
from handlers import cart  # Import the cart handler you created

MENU_ITEMS = {
    "Margherita Pizza": 85,
    "Chicken Mayo": 95,
    "Garlic Bread": 30,
    "Choc Cupcake": 25,
    "Lemonade": 15,
}

# Main order menu (shows your original order menu options)
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

# Extended order callback handler (handles both your original and cart features)
async def order_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data
    user_id = query.from_user.id

    back_keyboard = get_order_back_keyboard()

    # Original options
    if data == "order_view_menu":
        # Show the menu with prices
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
        # Prompt user to send order text manually (can extend later)
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

    # New cart-related callbacks
    elif data == "cart_view":
        user_cart = cart.get_user_cart(user_id)
        if not user_cart:
            await query.edit_message_text("🛒 Your cart is empty.", reply_markup=back_keyboard)
            return
        
        lines = []
        total = 0
        for item, qty in user_cart.items():
            price = MENU_ITEMS.get(item, 0)
            lines.append(f"{item} x{qty} — R{price*qty}")
            total += price * qty
        lines.append(f"\n*Total: R{total}*")

        # Buttons to remove items + checkout
        keyboard = [
            [InlineKeyboardButton(f"➖ Remove 1 {item}", callback_data=f"cart_remove_{item}")]
            for item in user_cart
        ]
        keyboard.append([InlineKeyboardButton("✅ Checkout", callback_data="cart_checkout")])
        keyboard.append([InlineKeyboardButton("🔙 Back to Order Menu", callback_data="order_back")])
        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.edit_message_text(
            "*Your Cart:*\n" + "\n".join(lines),
            parse_mode="Markdown",
            reply_markup=reply_markup
        )

    elif data.startswith("cart_remove_"):
        item = data[len("cart_remove_"):]
        cart.remove_item(user_id, item, quantity=1)
        await query.answer(text=f"Removed 1 {item} from your cart.", show_alert=False)
        # Refresh cart view to update quantities
        await order_callback(update, context)

    elif data == "cart_checkout":
        cart.clear_cart(user_id)
        await query.edit_message_text("✅ Thank you! Your order has been placed.\nWe will contact you shortly.")

    # New: Menu with Add to Cart buttons (for adding items)
    elif data == "order_add_to_cart":
        keyboard = [
            [InlineKeyboardButton(f"{name} - R{price}", callback_data=f"menu_add_{name}")]
            for name, price in MENU_ITEMS.items()
        ]
        keyboard.append([InlineKeyboardButton("🛒 View Cart", callback_data="cart_view")])
        keyboard.append([InlineKeyboardButton("🔙 Back to Order Menu", callback_data="order_back")])
        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.edit_message_text(
            "🍽 *Menu:*\nChoose items to add to your cart:",
            parse_mode="Markdown",
            reply_markup=reply_markup
        )

    elif data.startswith("menu_add_"):
        item = data[len("menu_add_"):]
        cart.add_item(user_id, item, quantity=1)
        await query.answer(text=f"✅ Added {item} to your cart!", show_alert=False)

    else:
        # fallback to original order menu
        await order_menu(update, context, from_callback=True)

# Optional: you can add this to your callback router if you want the start callback to handle order start
async def start_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "start_back":
        from bot import start
        await start(update, context)
    elif data == "start_order":
        await order_menu(update, context, from_callback=True)
