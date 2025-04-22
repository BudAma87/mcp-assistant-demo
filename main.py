import requests

def ask_mcp(question: str):
    if "calculate" in question.lower():
        expr = question.lower().replace("calculate", "").strip()
        res = requests.get("http://localhost:8000/tool/calculate", params={"q": expr})
        return res.json()["result"]
    elif "what is" in question.lower():
        term = question.lower().replace("what is", "").strip()
        res = requests.get("http://localhost:8000/tool/knowledge", params={"term": term})
        return res.json()["result"]
    else:
        return "Sorry, I don't understand."

if __name__ == "__main__":
    print(ask_mcp("calculate 12 / 3"))
    print(ask_mcp("what is mcp"))