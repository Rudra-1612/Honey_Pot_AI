def classify_scam(text):
    text = text.lower()

    if "job" in text:
        return "job_fraud"
    if "lottery" in text:
        return "lottery"
    if "upi" in text:
        return "upi_scam"
    return "bank_phishing"
