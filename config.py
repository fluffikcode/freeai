"""Загрузка конфигов с сервера. Pull последней модели + валидация."""

import sys
import requests

BASE = "https://larp.saturnix.fun/freeai"
MODELS_URL = f"{BASE}/models.json"

def _get(url):
    r = requests.get(url, timeout=15)
    r.raise_for_status()
    return r.json()

def pull():
    """
    Загружает models.json, берёт ПОСЛЕДНЮЮ модель.
    Возвращает dict {name, baseurl, api} или None при ошибке.
    """
    try:
        data = _get(MODELS_URL)
    except Exception as e:
        error_msg = f"не удалось загрузить models.json: {e}"
        return None, error_msg

    models = data.get("models") or []
    if not models:
        return None, "в models.json нет моделей"

    model = models[-1]
    for key in ("name", "baseurl", "api"):
        if key not in model:
            return None, f"у модели отсутствует поле '{key}'"
    return model, None

def validate(baseurl: str, api: str) -> tuple[bool, str]:
    """
    Проверяет baseurl + api реальным запросом к /models.
    Возвращает (ok, сообщение).
    """
    if not baseurl.startswith(("http://", "https://")):
        return False, "baseurl должен начинаться с http:// или https://"

    base = baseurl.rstrip("/")
    # нормализация endpoint для проверки
    if base.endswith("/chat/completions"):
        models_url = base[: -len("/chat/completions")] + "/models"
    elif base.endswith("/v1"):
        models_url = f"{base}/models"
    else:
        models_url = f"{base}/v1/models"

    headers = {"Authorization": f"Bearer {api}"}
    try:
        r = requests.get(models_url, headers=headers, timeout=15)
    except Exception as e:
        return False, f"сеть недоступна: {e}"

    if r.status_code == 200:
        return True, "successfully"
    if r.status_code in (401, 403):
        return False, f"неверный api key (HTTP {r.status_code})"
    return False, f"HTTP {r.status_code}"
