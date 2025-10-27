#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "3140089"))
API_HASH = environ.get("API_HASH", "ef67c500cfbd85b764535cf1c8c9917f")
BOT_TOKEN = environ.get("BOT_TOKEN", "8254123476:AAHPlP24ZyfRDuIKl9buhMPnAOXlbv4e1IQ")

OWNER = int(environ.get("OWNER", "7361052650"))
CREDIT = environ.get("CREDIT", "Prunus🚬💋")
cookies_file_path = os.getenv("cookies_file_path", "youtube_cookies.txt")

TOTAL_USER = os.environ.get('TOTAL_USERS', '7361052650').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '7361052650').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))



