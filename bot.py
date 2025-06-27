import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
)
from dotenv import load_dotenv

# Load .env file
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# START COMMAND
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()
    message = (
        "👋 Welcome to FLOW-NET Bot!\n"
        "Please choose a bot type to test:\n\n"
        "🔹 /order - Order system bot\n"
        "🔹 /deliveries - Delivery updates bot\n"
        "🔹 /stock - Stock-taking bot\n"
        "🔹 /helpbot - General help/FAQ bot"
    )
    await update.message.reply_text(message)

# CHOOSE A MODE
async def order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["mode"] = "order"
    await update.message.reply_text("🛒 You selected Order Bot.\nType something like: `Place 2x Pepperoni`")

async def deliveries(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["mode"] = "deliveries"
    await update.message.reply_text("🚚 You selected Delivery Bot.\nAsk something like: `Where is my delivery?`")

async def stock(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["mode"] = "stock"
    await update.message.reply_text("📦 You selected Stock Bot.\nTry: `Update: 5x flour, 2x cheese`")

async def helpbot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["mode"] = "help"
    await update.message.reply_text("🤖 You selected Help Bot.\nAsk something like: `How do I place an order?`")

# HANDLE TEXT BASED ON CURRENT MODE
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mode = context.user_data.get("mode")
    msg = update.message.text

    if not mode:
        await update.message.reply_text("Please choose a mode first: /start")
        return

    if mode == "order":
        await update.message.reply_text(f"🧾 Got it! Sending order: \"{msg}\"")
    elif mode == "deliveries":
        await update.message.reply_text("📍 Tracking your delivery... ETA: 15 mins.")
    elif mode == "stock":
        await update.message.reply_text("📊 Stock updated. Thanks!")
    elif mode == "help":
        await update.message.reply_text("💬 Here's a quick help answer to your message.")
    else:
        await update.message.reply_text("❓ Unknown mode. Please /start again.")

# MAIN BOT ENTRY
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("order", order))
    app.add_handler(CommandHandler("deliveries", deliveries))
    app.add_handler(CommandHandler("stock", stock))
    app.add_handler(CommandHandler("helpbot", helpbot))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Bot is running...")
    app.run_polling()
