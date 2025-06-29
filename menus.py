from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# === Entry Screen ===
def get_entry_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🧍 I’m a Customer", callback_data="start_customer")],
        [InlineKeyboardButton("👨‍🍳 Admin Panel", callback_data="start_admin")]
    ])


# === Customer Main Menu ===
def get_customer_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🍽 View Menu", callback_data="menu_view")],
        [InlineKeyboardButton("🛒 View Cart", callback_data="cart_view")],
        [InlineKeyboardButton("📍 Track Order", callback_data="delivery_track")],
        [InlineKeyboardButton("📞 Contact", callback_data="customer_contact")],
        [InlineKeyboardButton("🔙 Back to Role Select", callback_data="back_to_entry")]
    ])


# === Admin Main Menu ===
def get_admin_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🧾 View Orders", callback_data="admin_orders")],
        [InlineKeyboardButton("📦 Stock Management", callback_data="admin_stock")],
        [InlineKeyboardButton("🚚 Delivery Setup", callback_data="admin_delivery")],
        [InlineKeyboardButton("⚙️ Settings", callback_data="admin_settings")],
        [InlineKeyboardButton("🔙 Back to Role Select", callback_data="back_to_entry")]
    ])


# === Order Menu ===
def get_order_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🍕 View Menu", callback_data="order_view_menu")],
        [InlineKeyboardButton("📦 My Orders", callback_data="order_my_orders")],
        [InlineKeyboardButton("⏱ Wait Time", callback_data="order_wait_time")],
        [InlineKeyboardButton("📞 Contact", callback_data="order_contact")],
        [InlineKeyboardButton("🔙 Back to Customer Menu", callback_data="start_customer")]
    ])


def get_order_back_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 Back to Order Menu", callback_data="order_back")]
    ])


# === Delivery ===
def get_delivery_keyboard():  # Used by customers
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📍 Track My Order", callback_data="delivery_track_status")],
        [InlineKeyboardButton("📜 Delivery History", callback_data="delivery_history")],
        [InlineKeyboardButton("📞 Contact", callback_data="delivery_contact")],
        [InlineKeyboardButton("🔙 Back to Customer Menu", callback_data="start_customer")]
    ])


def get_admin_delivery_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🚚 Incoming Deliveries", callback_data="admin_delivery_incoming")],
        [InlineKeyboardButton("🗓 Schedule Pickup", callback_data="admin_delivery_schedule")],
        [InlineKeyboardButton("📦 Manage Drivers", callback_data="admin_delivery_drivers")],
        [InlineKeyboardButton("🔙 Back to Admin Panel", callback_data="start_admin")]
    ])


# === Stock ===
def get_stock_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("📦 View Stock", callback_data="stock_view")],
        [InlineKeyboardButton("➕ Add Stock", callback_data="stock_add")],
        [InlineKeyboardButton("➖ Remove Stock", callback_data="stock_remove")],
        [InlineKeyboardButton("🧾 Stock Report", callback_data="stock_report")],
        [InlineKeyboardButton("🔙 Back to Admin Panel", callback_data="start_admin")]
    ])


def get_stock_back_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 Back to Stock Menu", callback_data="stock_back")]
    ])


# === Help ===
def get_help_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("❓ How to Use", callback_data="help_how_to_use")],
        [InlineKeyboardButton("🛠 Features", callback_data="help_features")],
        [InlineKeyboardButton("📞 Support", callback_data="help_support")],
        [InlineKeyboardButton("🔙 Back to Customer Menu", callback_data="start_customer")]
    ])


def get_help_back_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 Back to Help Menu", callback_data="help_back")]
    ])


# === Settings (Admin) ===
def get_settings_back_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 Back to Admin Panel", callback_data="start_admin")]
    ])
