import requests
import pickle
import os

SESSIONS_DIR = "sessions"

if not os.path.exists(SESSIONS_DIR):
    os.makedirs(SESSIONS_DIR)

def send_otp(mobile):
    url = f"https://testbook.com/api/v1/user/generate-otp"
    return requests.post(url, json={"mobile": mobile}).ok

def verify_otp(mobile, otp, user_id):
    url = f"https://testbook.com/api/v1/user/verify-otp"
    session = requests.Session()
    resp = session.post(url, json={"mobile": mobile, "otp": otp})
    if resp.ok:
        with open(f"{SESSIONS_DIR}/{user_id}.pkl", "wb") as f:
            pickle.dump(session, f)
        return session
    return None

def load_session(user_id):
    path = f"{SESSIONS_DIR}/{user_id}.pkl"
    if os.path.exists(path):
        with open(path, "rb") as f:
            return pickle.load(f)
    return None
