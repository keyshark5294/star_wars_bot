import os
from dotenv import load_dotenv, find_dotenv


if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
# DB_HOST = os.getenv("DB_HOST")
# DB_USER = os.getenv("USER_NAME")
# DB_PASSWORD = os.getenv("PASSWORD")
# DB_NAME = os.getenv("DB_NAME")
