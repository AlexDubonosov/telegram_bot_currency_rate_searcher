import os
from dotenv import load_dotenv, find_dotenv


if not find_dotenv():
    exit('Переменные окружения не загружены, т.к. отсутствует файл .env')
else:
    load_dotenv()


BOT_TOKEN = os.getenv('BOT_TOKEN')
API_KEY = os.getenv('API_KEY')


MENU_COMMANDS = (
    ("/start", "Запустить бота"),
    ('/currency', 'Выбрать валюту'),
    ('/history', 'Последние 10 запросов'),
    ("/help", "Вывести справку")
)
