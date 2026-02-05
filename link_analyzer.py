def link_risk(url):
    bad = ["login", "verify", "update"]
    return "HIGH" if any(b in url for b in bad) else "LOW"
