import json
import os

CART_FILE = "data/cart.json"

def load_cart():
    if not os.path.exists(CART_FILE):
        return {}
    with open(CART_FILE, "r") as f:
        return json.load(f)

def save_cart(cart):
    with open(CART_FILE, "w") as f:
        json.dump(cart, f, indent=2)

def get_user_cart(user_id):
    cart = load_cart()
    return cart.get(str(user_id), {})

def add_item(user_id, item, quantity=1):
    cart = load_cart()
    user_cart = cart.get(str(user_id), {})
    user_cart[item] = user_cart.get(item, 0) + quantity
    cart[str(user_id)] = user_cart
    save_cart(cart)

def remove_item(user_id, item, quantity=1):
    cart = load_cart()
    user_cart = cart.get(str(user_id), {})
    if item in user_cart:
        user_cart[item] = max(0, user_cart[item] - quantity)
        if user_cart[item] == 0:
            del user_cart[item]
        cart[str(user_id)] = user_cart
        save_cart(cart)

def clear_cart(user_id):
    cart = load_cart()
    if str(user_id) in cart:
        del cart[str(user_id)]
        save_cart(cart)
