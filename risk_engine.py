def risk_score(text):
    score = 0
    words = ["urgent", "otp", "account", "click", "verify"]

    for w in words:
        if w in text.lower():
            score += 20

    return min(score, 100)
