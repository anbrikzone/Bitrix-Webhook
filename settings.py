from dotenv import load_dotenv, dotenv_values
import os
from os.path import join, dirname

# Получаем константы из .env
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

TOKEN = os.getenv('TOKEN')
BITRIX_URL = os.getenv('BITRIX_URL')

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_DATABASE = os.getenv('DB_DATABASE')