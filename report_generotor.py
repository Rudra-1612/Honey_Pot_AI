import json

STATS_FILE = "data/stats.json"

def load():
    with open(STATS_FILE) as f:
        return json.load(f)

def save(data):
    with open(STATS_FILE, "w") as f:
        json.dump(data, f)

def generate_report(cid, reply, scam_type, score, intel):
    stats = load()

    stats["total_scams"] += 1
    stats["active_chats"] += 1
    stats["risk_scores"].append(score)
    stats["logs"].append(f"{cid} -> {scam_type} ({score})")

    save(stats)

    return {
        "conversation_id": cid,
        "is_scam": True,
        "reply": reply,
        "scam_type": scam_type,
        "risk_score": score,
        "extracted_intel": intel
    }

STATS = load()
