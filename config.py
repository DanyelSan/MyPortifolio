import os
from dotenv import load_dotenv

load_dotenv()

email = os.getenv("EMAIL_USER")
password = os.getenv("EMAIL_PASSWORD")
secret_key = os.getenv("SECRET_KEY")