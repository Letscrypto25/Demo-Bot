# storage/cart.py

import json
import os

CART_FILE = "data/carts.json"

# Make sure data/ directory exists
os.makedirs(os.path.dirname(CART_FILE), exist_ok=True)

# === Utility Functions ===

def load_carts():
    if not os.path.exists(CART_FILE):
        return {}
    with open(CART_FILE, "r") as f:
        return json.load(f)

def save_carts(data):
    with open(CART_FILE, "w") as f:
        json.dump(data, f, indent=2)

# === Core Cart Operations ===

def get_cart(user_id: str):
    carts = load_carts()
    return carts.get(str(user_id), [])

def add_to_cart(user_id: str, item: str):
    carts = load_carts()
    uid = str(user_id)
    if uid not in carts:
        carts[uid] = []
    carts[uid].append(item)
    save_carts(carts)

def clear_cart(user_id: str):
    carts = load_carts()
    uid = str(user_id)
    if uid in carts:
        del carts[uid]
        save_carts(carts)

def remove_from_cart(user_id: str, item: str):
    carts = load_carts()
    uid = str(user_id)
    if uid in carts and item in carts[uid]:
        carts[uid].remove(item)
        save_carts(carts)
