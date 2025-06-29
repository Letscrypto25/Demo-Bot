from telegram import InlineKeyboardButton, InlineKeyboardMarkup

def get_start_keyboard():
    keyboard = [
        [InlineKeyboardButton("🧾 Order Menu", callback_data="start_order")],
        [InlineKeyboardButton("🚚 Delivery Bot", callback_data="start_delivery")],
        [InlineKeyboardButton("📦 Stock Management", callback_data="start_stock")],
        [InlineKeyboardButton("❓ General Help", callback_data="start_help")]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_order_keyboard():
    keyboard = [
        [InlineKeyboardButton("🍕 View Menu", callback_data="order_view_menu")],
        [InlineKeyboardButton("📝 Place Order", callback_data="order_place")],
        [InlineKeyboardButton("📦 My Orders", callback_data="order_my_orders")],
        [InlineKeyboardButton("⏱ Wait Time", callback_data="order_wait_time")],
        [InlineKeyboardButton("📞 Contact", callback_data="order_contact")],
        [InlineKeyboardButton("🔙 Back to Main Menu", callback_data="start_back")]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_order_back_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 Back to Order Menu", callback_data="order_back")]
    ])

def get_delivery_keyboard():
    keyboard = [
        [InlineKeyboardButton("🚚 View Deliveries", callback_data="delivery_view")],
        [InlineKeyboardButton("📍 Track My Order", callback_data="delivery_track")],
        [InlineKeyboardButton("📜 Delivery History", callback_data="delivery_history")],
        [InlineKeyboardButton("🗓 Schedule Delivery", callback_data="delivery_schedule")],
        [InlineKeyboardButton("📞 Contact", callback_data="delivery_contact")],
        [InlineKeyboardButton("🔙 Back to Main Menu", callback_data="start_back")]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_delivery_back_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 Back to Delivery Menu", callback_data="delivery_back")]
    ])

def get_stock_keyboard():
    keyboard = [
        [InlineKeyboardButton("📦 View Stock", callback_data="stock_view")],
        [InlineKeyboardButton("➕ Add Stock", callback_data="stock_add")],
        [InlineKeyboardButton("➖ Remove Stock", callback_data="stock_remove")],
        [InlineKeyboardButton("🧾 Stock Report", callback_data="stock_report")],
        [InlineKeyboardButton("🔙 Back to Main Menu", callback_data="start_back")]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_stock_back_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 Back to Stock Menu", callback_data="stock_back")]
    ])
    
def get_help_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("❓ How to Use", callback_data="help_how_to_use")],
        [InlineKeyboardButton("🛠 Features", callback_data="help_features")],
        [InlineKeyboardButton("📞 Support", callback_data="help_support")],
        [InlineKeyboardButton("🔙 Back to Main Menu", callback_data="start_back")]
    ])

def get_help_back_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 Back to Help Menu", callback_data="help_back")]
    ])
#split 

def get_entry_keyboard():
    keyboard = [
        [InlineKeyboardButton("🧍 I’m a Customer", callback_data="start_customer")],
        [InlineKeyboardButton("👨‍🍳 Admin Panel", callback_data="start_admin")]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_customer_keyboard():
    keyboard = [
        [InlineKeyboardButton("🍽 View Menu", callback_data="menu_view")],
        [InlineKeyboardButton("🛒 View Cart", callback_data="cart_view")],
        [InlineKeyboardButton("📍 Track Order", callback_data="delivery_track")],
        [InlineKeyboardButton("📞 Contact", callback_data="customer_contact")],
        [InlineKeyboardButton("🔙 Back", callback_data="start_back")]
    ]
    return InlineKeyboardMarkup(keyboard)

def get_admin_keyboard():
    keyboard = [
        [InlineKeyboardButton("🧾 View Orders", callback_data="admin_orders")],
        [InlineKeyboardButton("📦 Stock Management", callback_data="admin_stock")],
        [InlineKeyboardButton("🚚 Deliveries", callback_data="admin_delivery")],
        [InlineKeyboardButton("⚙️ Settings", callback_data="admin_settings")],
        [InlineKeyboardButton("🔙 Back", callback_data="start_back")]
    ]
    return InlineKeyboardMarkup(keyboard)
