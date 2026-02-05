import requests
import random
import time

URL = "http://127.0.0.1:8000/webhook"

messages = [
    "Your bank account blocked send OTP",
    "Click this link to verify https://fakebank-login.xyz",
    "Send UPI payment quickly",
    "Lottery winner share account number"
]

cid = "SIM001"

while True:
    msg = random.choice(messages)

    payload = {
        "conversation_id": cid,
        "message": msg
    }

    res = requests.post(URL, json=payload)

    print("Scammer:", msg)
    print("Agent:", res.json()["reply"])
    print("-" * 40)

    time.sleep(3)
