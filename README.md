# Задача
Решение задачи от Лепишко Вадима

Перед началом необходимо выполнить:
1. Установить зависимости (pip install -r requirements.txt)
2. Установить переменные окружения:
- SECRET_KEY - ключ
- DATABASE_URL - путь к БД
- FLASK_APP - путь к файлу manage.py
- FLASK_DEBUG - дебаг режим
- CONFIG - путь к классу Config

Пример:
- SECRET_KEY = q(cfai#09+%qm!^vs6gm^rh=_2@%8npsu-*%^glr)bhx84s$g*
- DATABASE_URL = postgresql://postgres:root@localhost/products
- FLASK_APP = manage.py
- FLASK_DEBUG= 1
- CONFIG = config.Config

3. Создать базу данных и провести миграции
4. Заполнить БД с помощью команд:
- flask fill products путь_к_products.csv
- flask fill reviews путь_к_reviews.csv
5. Запуститить сервер командой flask run
