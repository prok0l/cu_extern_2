# Экстерн-проект #2 

Запуск 

- создание .env файла
    ```
    API_KEY=
    HOST=localhost
    PORT=8080
    API_URL=http://dataservice.accuweather.com/
    ```
  
- создание виртуального окружения
    ```bash
    python -m venv venv
    ```

- активация виртуального окружения
    ```bash
    source venv/bin/activate
    ```
  
- установка зависимостей
    ```bash
    pip install -r ./requirements.txt
    ```
  
- запуск
    ```bash
    python ./app.py
    ```