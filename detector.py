def detect_scam(text: str) -> bool:
    keywords = ["otp", "bank", "account", "verify", "link", "urgent"]
    return any(k in text.lower() for k in keywords)
