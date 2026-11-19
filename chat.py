"""Настоящий рабочий чат с ИИ через OpenAI-совместимый API."""

import requests
from ui import white, gray, divider

def _endpoint(baseurl: str) -> str:
    base = baseurl.rstrip("/")
    if base.endswith("/chat/completions"):
        return base
    if base.endswith("/v1"):
        return f"{base}/chat/completions"
    return f"{base}/v1/chat/completions"

def run(model: dict):
    url = _endpoint(model["baseurl"])
    headers = {
        "Authorization": f"Bearer {model['api']}",
        "Content-Type": "application/json",
    }
    history = []

    print()
    print(white("   модель   ") + gray(model["name"]))
    print(white("   endpoint ") + gray(url))
    divider()
    print(gray("   /exit — выйти    /clear — очистить историю"))
    divider()
    print()

    while True:
        try:
            user = input(white("   you › ")).strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return
        if not user:
            continue
        if user in ("/exit", "/quit"):
            return
        if user == "/clear":
            history.clear()
            print(gray("   история очищена"))
            print()
            continue

        history.append({"role": "user", "content": user})
        payload = {"model": model["name"], "messages": history}

        try:
            r = requests.post(url, headers=headers, json=payload, timeout=120)
            if r.status_code != 200:
                print(gray(f"   [!] HTTP {r.status_code}: {r.text[:300]}"))
                history.pop()
                print()
                continue
            answer = r.json()["choices"][0]["message"]["content"]
        except Exception as e:
            print(gray(f"   [!] ошибка: {e}"))
            history.pop()
            print()
            continue

        history.append({"role": "assistant", "content": answer})
        print(white("   ai  › ") + answer)
        print()
