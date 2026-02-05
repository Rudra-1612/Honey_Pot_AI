import datetime

def log(text):
    with open("app.log", "a") as f:
        f.write(f"{datetime.datetime.now()} - {text}\n")
