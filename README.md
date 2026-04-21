# streamService-backend

## Установка

### Требования
- Python 3.12

### Клонирование и настройка

```bash
# Клонировать репозиторий
git clone <repository-url>
cd streamService-backend

# Создать виртуальное окружение с Python 3.12
python3.12 -m venv venv

# Активировать виртуальное окружение
source venv/bin/activate  # для macOS/Linux
# или
venv\Scripts\activate  # для Windows

# Установить зависимости
pip install -r requirements.txt
```

## Запуск

```bash
# Убедитесь что виртуальное окружение активировано
uvicorn main:app --reload
```

Сервер запустится на `http://127.0.0.1:8000`

Тестовый эндпоинт: `http://127.0.0.1:8000/test`
