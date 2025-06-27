import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = 7494273135:AAG_eyFajwjeXWd7EWf1A0nlMp1RmWFMoG8 # Replace this

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["/order_menu", "/deliveries"],
        ["/stock_take", "/help_bot"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "👋 Welcome to the FLOW-NET Demo Bot!\n\n"
        "Explore template flows below:\n"
        "📦 /order_menu – Customer order flow\n"
        "🚚 /deliveries – Delivery assignment\n"
        "📦 /stock_take – Stock tracker\n"
        "💬 /help_bot – General helpdesk bot\n",
        reply_markup=reply_markup
    )

# Order menu simulation
async def order_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🍕 Order Menu\n\n"
        "1. Margherita – R65\n"
        "2. BBQ Chicken – R85\n"
        "3. Vegan Delight – R75\n\n"
        "To place an order, reply with the item number (e.g. '1')"
    )

# Delivery tracking simulation
async def deliveries(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚚 Delivery Tracking\n\n"
        "• Order #1234 – Out for delivery 🚴\n"
        "• Order #1235 – Delivered ✅\n"
        "• Order #1236 – Preparing 🧑‍🍳"
    )

# Stock take simulation
async def stock_take(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📦 Stock Take\n\n"
        "• Cheese: ✅ In stock\n"
        "• Tomato Sauce: ⚠️ Low\n"
        "• Boxes: ❌ Out of stock"
    )

# Help bot
async def help_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💬 Help Bot\n\n"
        "Hi! How can I help?\n"
        "• Type 'hours' for working hours\n"
        "• Type 'location' for address\n"
        "• Or ask your question below."
    )

# Generic fallback
async def fallback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if "hours" in text:
        await update.message.reply_text("🕓 We’re open Mon–Sat, 8AM to 6PM.")
    elif "location" in text:
        await update.message.reply_text("📍 123 Baker Street, Cape Town")
    else:
        await update.message.reply_text("🤖 I’ll pass that to support. In the real bot, this would notify staff.")

# --- MAIN BOT SETUP ---
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("order_menu", order_menu))
    app.add_handler(CommandHandler("deliveries", deliveries))
    app.add_handler(CommandHandler("stock_take", stock_take))
    app.add_handler(CommandHandler("help_bot", help_bot))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, fallback))

    print("🤖 Bot is running...")
    app.run_polling()
