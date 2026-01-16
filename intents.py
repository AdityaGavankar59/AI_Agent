import re

def detect_intent(text: str):
    t = text.strip().lower()

    if t in ("exit", "quit", "bye"):
        return "exit", {}
    if t in ("help", "menu", "commands"):
        return "help", {}

    # weather: "weather Mumbai" or "what's the weather in Mumbai."
    if "weather" in t or "temperature" in t:
        # crude city extraction: last word
        parts = text.split()
        city = parts[-1] if len(parts) > 1 else None
        return "weather", {"city": city}

    # calc: "calc 2+3*4" or "calculate 10/2"
    if t.startswith("calc ") or t.startswith("calculate "):
        expr = text.split(" ", 1)[1]
        return "calc", {"expr": expr}
    # or generic math detection
    if re.search(r"\d", t) and any(op in t for op in "+-*/"):
        return "calc", {"expr": text}

    # wiki: "wiki neural networks" or "what are neural networks."
    if t.startswith("wiki "):
        topic = text.split(" ", 1)[1]
        return "wiki", {"topic": topic}
    if t.startswith("what is ") or t.startswith("who is "):
        topic = text.split(" ", 2)[2] if len(text.split()) > 2 else None
        return "wiki", {"topic": topic}

    # to-do
    if t.startswith("add todo ") or t.startswith("add task "):
        task = text.split(" ", 2)[2] if len(text.split()) > 2 else None
        return "add_todo", {"task": task}
    if "list todos" in t or "show todos" in t or "show tasks" in t:
        return "list_todo", {}

    # joke/quote
    if "joke" in t or "quote" in t:
        return "joke", {}

    return "unknown", {}
