import re

def normalise(text: str) -> str:
    t = text.replace("\r", "")
    t = re.sub(r"\t", " ", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()
