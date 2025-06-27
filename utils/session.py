# utils/session.py

user_sessions = {}

def set_user_mode(user_id, mode):
    user_sessions[user_id] = mode

def get_user_mode(user_id):
    return user_sessions.get(user_id, None)

def clear_user_mode(user_id):
    if user_id in user_sessions:
        del user_sessions[user_id]
