"""Точка входа. Меню 1/2 с возвратом. Выход — по 'exit'."""

import sys
from ui import print_logo, white, gray, divider, success, error
import config
import chat

def _read(prompt: str) -> str | None:
    """Читает строку. None = Ctrl+D/Ctrl+C."""
    try:
        return input(prompt)
    except (EOFError, KeyboardInterrupt):
        print()
        return None

def do_pull():
    model, err = config.pull()
    divider()
    if err:
        error(err)
    else:
        print(white("   модель   ") + gray(model["name"]))
        print(white("   baseurl  ") + gray(model["baseurl"]))
        print(white("   api      ") + gray(model["api"]))
        success("pulled")
    divider()
    print()

def do_openstructure():
    divider()
    print(gray("   введи baseurl и api (или 'exit' для отмены)"))
    divider()
    print()

    while True:
        baseurl = _read(white("   baseurl › "))
        if baseurl is None:
            return
        baseurl = baseurl.strip()
        if baseurl.lower() == "exit":
            return
        if not baseurl:
            error("baseurl не может быть пустым")
            print()
            continue

        api = _read(white("   api     › "))
        if api is None:
            return
        api = api.strip()
        if api.lower() == "exit":
            return
        if not api:
            error("api не может быть пустым")
            print()
            continue

        print()
        print(gray("   проверка…"))
        ok, msg = config.validate(baseurl, api)
        if ok:
            success(msg)
            print()
            # имя модели узнаем из /models? — для простоты спрашиваем
            name = _read(white("   model   › "))
            if name is None:
                return
            name = name.strip()
            if not name or name.lower() == "exit":
                error("нужно имя модели")
                print()
                continue
            chat.run({"name": name, "baseurl": baseurl, "api": api})
            return
        else:
            error(msg)
            print()

def main():
    while True:
        print_logo()
        print(white("   1") + gray(" · pull           загрузить последнюю модель"))
        print(white("   2") + gray(" · openstructure  подключиться и открыть чат"))
        print()
        print(gray("   введи 1, 2 или exit"))
        print()

        choice = _read(white("   › "))
        if choice is None:
            print(gray("   bye"))
            sys.exit(0)
        choice = choice.strip().lower()

        if choice == "exit":
            print(gray("   bye"))
            sys.exit(0)

        print()
        if choice == "1":
            do_pull()
        elif choice == "2":
            do_openstructure()
        else:
            error("неизвестный пункт")
            print()

if __name__ == "__main__":
    main()
