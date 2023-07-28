import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

DB_HOST = os.environ.get("DB_HOST")
DB_USERNAME = os.environ.get("DB_USERNAME")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DATABASE = os.environ.get("DATABASE")

CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
USER_AGENT = os.environ.get("USER_AGENT")

PROXIES = "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt"
