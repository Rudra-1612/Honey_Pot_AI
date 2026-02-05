import re

def extract_intel(text):
    upi = re.findall(r'\w+@\w+', text)
    links = re.findall(r'https?://\S+', text)
    phones = re.findall(r'\d{10}', text)
    accounts = re.findall(r'\d{10,18}', text)

    return {
        "upi_ids": upi,
        "links": links,
        "phones": phones,
        "accounts": accounts
    }
