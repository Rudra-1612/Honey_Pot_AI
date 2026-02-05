import random

PERSONAS = [
    "I am old and confused.",
    "I am a student and new to banking.",
    "Please explain slowly."
]

def get_persona():
    return random.choice(PERSONAS)
