MEMORY = {}

def get_history(cid):
    return MEMORY.get(cid, [])

def save_history(cid, msg, role):
    MEMORY.setdefault(cid, []).append({"role": role, "msg": msg})
