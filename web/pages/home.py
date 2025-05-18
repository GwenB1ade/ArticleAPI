import streamlit as st


def home():
    st.title("🏠 Home")
    st.write(
        "This is a UI created using Streamlit. You can use this UI to test the API functionality."
    )

    st.markdown(
        """# 📚 ArticleAPI

🚀 Небольшой, но мощный API для работы со статьями, поддерживающий REST, GraphQL и gRPC

## 📝 Project Description

Этот проект демонстрирует мои навыки в создании современных API с использованием различных технологий и подходов.

### 🛠️ Используемые технологии:
- 🐘 PostgreSQL
- 🍃 MongoDB
- 🔍 ElasticSearch
- ⚡ FastAPI
- � GraphQL
- 🚀 gRPC

### 🌟 Основные особенности:
- **RESTful архитектура** с чёткой структурой (GET, POST, PUT, DELETE)
- ⚡ Асинхронная обработка запросов
- 🧠 Полная типизация кода
- 🛡️ Валидация данных через Pydantic
- 🎯 Поддержка GraphQL
- ⚡ Высокопроизводительный gRPC

## Запуск приложения

### 1️⃣ Клонируем репозиторий:

```bash
git clone https://github.com/GwenB1ade/ArticleAPI
```

### 2️⃣ Запускаем скрипт установки
Для Linux/macOS:
```bash
chmod +x install.sh
./install.sh
```

Для Windows:
```bash
install.bat
```


### 3️⃣ Запускаем приложение

```bash
chmod +x run.sh
./run.sh
```

Для Windows:
```bash
run.bat
```

## 🛠️ Установка и запуск ArticleAPI вручную

## 📥 Клонирование репозитория

Для начала работы склонируйте проект с GitHub:

```bash
git clone https://github.com/GwenB1ade/ArticleAPI
cd ArticleAPI
```

## 🐳 Запуск Docker-контейнеров
Запустите все необходимые сервисы через Docker:
```bash
docker-compose up -d
```

## 🐍 Настройка Python-окружения
### 1️⃣ Создайте виртуальное окружение:
```bash
python -m venv .venv
```

### 2️⃣ Активируйте окружение:

```bash
# Для Linux/MacOS:
source .venv/bin/activate

# Для Windows:
.venv\Scripts\activate
```
### 3️⃣ Установите зависимости:

```bash
uv run pip install -e .
cd src
```

## 🚀 Запуск приложения
Для REST/GraphQL API:

```bash
uv run main.py run
```
Для gRPC сервера:

```bash
uv run main.py grpc
```

Для запуска Streamlit приложения, небходимо выполнить следующие команды из корня проекта:

```bash
cd web
uv run streamlit run main.py --server.runOnSave True
```

## 🔍 API Endpoints

### REST API:
- 📚 Swagger UI: `/docs`
- 📖 ReDoc: `/redoc`

### GraphQL:
- 🧩 GraphQL Playground: `/graphql`

### gRPC:
Порт: `50051`  
Рекомендуемые инструменты тестирования:
1. 🛠️ Postman (с поддержкой gRPC)
2. 🖥️ grpcui

## 🔮 Future Improvements

Планируемые улучшения:
- 🔒 Улучшение системы авторизации
- ⏳ Полная асинхронная работа с БД
- 🚀 Оптимизация запросов
- 🔍 Улучшение поиска в ElasticSearch

---

💡 Проект в активной разработке - ваши идеи и вклад приветствуются!"""
    )


home()
