# Используем официальный Python-образ
FROM python:3.11

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копируем весь проект
COPY . .

# Открываем порт 8000
EXPOSE 8000

# Команда по умолчанию (запуск сервера)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
