# ЭТО НЕ ДИПСИК САМА ДЕЛАЛА

# CT Helper 🎤

Телеграм-бот с двумя командами: приветствие и случайная цитата.

## 📋 Команды

| Команда  | Описание                        |
|----------|---------------------------------|
| `/start` | Приветствие и список команд     |
| `/swaga` | Случайная цитата из списка      |

## 🛠️ Требования

- Python 3.10+
- Telegram Bot Token ([получить у @BotFather](https://t.me/BotFather))

## 🚀 Установка и запуск

### Локально

```bash
# 1. Клонировать репозиторий
git clone https://github.com/zlatahet-cell/ruslan_goyda.git
cd ruslan_goyda

# 2. Создать виртуальное окружение
python -m venv .venv
source .venv/bin/activate        # Linux/macOS
# .venv\Scripts\activate         # Windows

# 3. Установить зависимости
pip install aiogram python-dotenv

# 4. Создать .env
echo "TOKEN=твой_токен_от_BotFather" > .env

# 5. Запустить
python bot.py
```

### Через Docker

```bash
docker compose up -d --build
docker compose logs -f
```

## 📁 Структура проекта

```
.
├── bot.py                # основной файл бота
├── requirements.txt      # зависимости
├── Dockerfile            # образ
├── docker-compose.yml    # запуск
├── .env                  # токен (не коммитить!)
├── .dockerignore
└── README.md
```

## 📄 `requirements.txt`

```
aiogram==3.15.0
python-dotenv==1.0.1
```

## 📄 `.env`

```env
TOKEN=123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
```

> ⚠️ **Не коммить `.env`!** Добавь его в `.gitignore`.

## 📄 `.gitignore`

```
.env
.venv/
__pycache__/
*.pyc
```

## 📄 `Dockerfile`

```dockerfile
FROM python:3.12-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "bot.py"]
```

## 📄 `docker-compose.yml`

```yaml
services:
  bot:
    build: .
    container_name: ct_helper_bot
    restart: unless-stopped
    env_file: .env
```

## 🧪 Как проверить

1. Открой бота в Telegram
2. Отправь `/start` — должен ответить приветствием
3. Отправь `/swaga` — получишь случайную цитату
4. Отправь `/swaga` ещё раз — цитата (скорее всего) другая

## 🐛 Известные проблемы

- **`NameError: name 'os' is not defined`** → добавь `import os`
- **`NameError: name 'name' is not defined`** → используй `if __name__ == "__main__":`
- **Бот молчит** → проверь токен в `.env` и что переменная называется `TOKEN`
- **`Unauthorized`** → токен неверный или отозван, создай новый у @BotFather

## 📝 Лицензия

Учебный проект.