# freeai

Терминальный клиент к freeai-моделям.

## Установка

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Запуск

```bash
python main.py
```

Меню:
- `1` — pull: загружает `models.json` с сервера, берёт **последнюю** модель
  и печатает `name`, `baseurl`, `api`.
- `2` — openstructure: открывает интерактивный чат с ИИ, используя
  последнюю модель. В чате доступны `/exit` и `/clear`.

## Формат `models.json`

Файл должен лежать по адресу
`https://larp.saturnix.fun/freeai/models.json` и иметь вид:

```json
{
  "models": [
    {
      "name": "gpt-4o-mini",
      "baseurl": "https://api.example.com/v1",
      "api": "sk-..."
    },
    {
      "name": "llama-3.1-70b",
      "baseurl": "https://api.example.com/v1",
      "api": "sk-..."
    }
  ]
}
```

Последний элемент массива считается актуальным — его и берёт `pull`,
его же использует `openstructure`.

## Как это работает

- `pull` → `GET /freeai/models.json` → `models[-1]` → печать.
- `openstructure` → тот же pull → `POST {baseurl}/v1/chat/completions`
  с историей сообщений → стрим-ответ не используется (обычный запрос),
  но историей можно управлять через `/clear`.

## Совместимость API

Любой OpenAI-совместимый endpoint: `baseurl` может быть как
`https://host/v1`, так и `https://host/v1/chat/completions` — клиент
сам нормализует путь.
