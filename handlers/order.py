from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes
from menus import get_order_keyboard, get_order_back_keyboard
from handlers import cart  # local cart.py handler

MENU_ITEMS = {
    "Margherita Pizza": 85,
    "Chicken Mayo": 95,
    "Garlic Bread": 30,
    "Choc Cupcake": 25,
    "Lemonade": 15,
}

# === ORDER MENU ===
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

# === MAIN ORDER CALLBACK HANDLER ===
async def order_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data
    user_id = query.from_user.id

    back_keyboard = get_order_back_keyboard()

    # === VIEW MENU (WITH ADD TO CART BUTTONS) ===
    if data == "order_view_menu":
        keyboard = [
            [InlineKeyboardButton(f"➕ {item} – R{price}", callback_data=f"menu_add_{item}")]
            for item, price in MENU_ITEMS.items()
        ]
        keyboard.append([InlineKeyboardButton("🛒 View Cart", callback_data="cart_view")])
        keyboard.append([InlineKeyboardButton("🔙 Back to Order Menu", callback_data="order_back")])
        await query.edit_message_text(
            "🍽 *Menu:*\nChoose items to add to your cart:",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # === ADD ITEM TO CART ===
    elif data.startswith("menu_add_"):
        item = data.replace("menu_add_", "")
        cart.add_item(user_id, item, 1)
        await query.answer(f"✅ {item} added to your cart!")

    # === VIEW CART ===
    elif data == "cart_view":
        user_cart = cart.get_user_cart(user_id)
        if not user_cart:
            await query.edit_message_text("🛒 Your cart is empty.", reply_markup=back_keyboard)
            return

        total = 0
        lines = []
        for item, qty in user_cart.items():
            price = MENU_ITEMS.get(item, 0)
            lines.append(f"{item} x{qty} — R{price * qty}")
            total += price * qty
        lines.append(f"\n*Total: R{total}*")

        keyboard = [
            [InlineKeyboardButton(f"➖ Remove 1 {item}", callback_data=f"cart_remove_{item}")]
            for item in user_cart
        ]
        keyboard.append([InlineKeyboardButton("✅ Checkout", callback_data="cart_checkout")])
        keyboard.append([InlineKeyboardButton("🔙 Back to Order Menu", callback_data="order_back")])

        await query.edit_message_text(
            "*🛒 Your Cart:*\n" + "\n".join(lines),
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # === REMOVE ITEM FROM CART ===
    elif data.startswith("cart_remove_"):
        item = data.replace("cart_remove_", "")
        cart.remove_item(user_id, item, 1)
        await query.answer(f"Removed 1 {item}.")
        await order_callback(update, context)  # refresh cart view

    # === CHECKOUT ===
    elif data == "cart_checkout":
        cart.clear_cart(user_id)
        await query.edit_message_text("✅ Thank you! Your order has been placed.\nWe will contact you shortly.")

    # === VIEW ORDERS ===
    elif data == "order_my_orders":
        await query.edit_message_text("📦 You currently have no active orders.", reply_markup=back_keyboard)

    # === WAIT TIME ===
    elif data == "order_wait_time":
        await query.edit_message_text("⏱ Average wait time: *15–25 minutes*", parse_mode="Markdown", reply_markup=back_keyboard)

    # === CONTACT ===
    elif data == "order_contact":
        await query.edit_message_text(
            "📞 *Contact Us:*\n- Phone: 065 982 1883\n- Telegram: @Letscrypto_bot",
            parse_mode="Markdown",
            reply_markup=back_keyboard
        )

    # === BACK TO ORDER MENU ===
    elif data == "order_back":
        await order_menu(update, context, from_callback=True)

    else:
        await query.edit_message_text("❌ Unknown action. Returning to menu...")
        await order_menu(update, context, from_callback=True)
