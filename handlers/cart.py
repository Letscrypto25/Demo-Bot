import json
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

CART_FILE = os.path.join("data", "carts.json")

# === Load and Save Cart ===
def load_cart():
    with open(CART_FILE, "r") as f:
        return json.load(f)

def save_cart(cart):
    with open(CART_FILE, "w") as f:
        json.dump(cart, f, indent=2)

# === Add item to cart ===
async def add_to_cart(update: Update, context: ContextTypes.DEFAULT_TYPE, item: str):
    user_id = str(update.effective_user.id)
    cart = load_cart()
    cart.setdefault(user_id, []).append(item)
    save_cart(cart)
    await update.callback_query.answer(f"✅ Added {item} to cart", show_alert=False)

# === View Cart ===
async def view_cart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    cart = load_cart()
    items = cart.get(user_id, [])

    if not items:
        await update.callback_query.edit_message_text("🛒 Your cart is empty.")
        return

    text = "🛒 *Your Cart:*\n" + "\n".join(f"- {i}" for i in items)
    keyboard = [
        [InlineKeyboardButton("🗑 Clear Cart", callback_data="cart_clear")],
        [InlineKeyboardButton("🔙 Back", callback_data="order_back")]
    ]
    await update.callback_query.edit_message_text(
        text=text,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# === Clear Cart ===
async def clear_cart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    cart = load_cart()
    cart[user_id] = []
    save_cart(cart)
    await update.callback_query.edit_message_text("🧹 Cart cleared.")
