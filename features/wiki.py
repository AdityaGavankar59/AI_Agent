import requests

API_URL = "https://en.wikipedia.org/api/rest_v1/page/summary/"

def wiki_summary(topic: str) -> str:
    if not topic:
        return "Please provide a topic for Wikipedia search."

    title = topic.strip().replace(" ", "_")
    url = API_URL + title

    try:
        resp = requests.get(url, timeout=5)
        if resp.status_code == 404:
            return f"No Wikipedia page found for '{topic}'."
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        return f"Error fetching Wikipedia summary: {e}"

    extract = data.get("extract")
    if not extract:
        return f"Wikipedia did not return a summary for '{topic}'."

    # Keep it short
    if len(extract) > 600:
        extract = extract[:600].rsplit(" ", 1)[0] + "..."
    return extract
