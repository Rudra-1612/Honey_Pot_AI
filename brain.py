import time
from agent.persona import get_persona

def generate_reply(history, msg):
    time.sleep(1.5)  # human delay

    persona = get_persona()

    return f"{persona} Can you send details again?"
