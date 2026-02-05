from fastapi import APIRouter
from core.detector import detect_scam
from core.classifier import classify_scam
from core.risk_engine import risk_score
from agent.brain import generate_reply
from agent.memory import save_history, get_history
from intelligence.extractor import extract_intel
from intelligence.report_generator import generate_report

router = APIRouter()

@router.post("/webhook")
def webhook(data: dict):
    cid = data["conversation_id"]
    msg = data["message"]

    history = get_history(cid)
    save_history(cid, msg, "scammer")

    is_scam = detect_scam(msg)

    if not is_scam:
        return {"is_scam": False, "reply": "Okay"}

    scam_type = classify_scam(msg)
    reply = generate_reply(history, msg)
    intel = extract_intel(msg)
    score = risk_score(msg)

    save_history(cid, reply, "agent")

    return generate_report(cid, reply, scam_type, score, intel)


@router.get("/stats")
def stats():
    from intelligence.report_generator import STATS
    return STATS
