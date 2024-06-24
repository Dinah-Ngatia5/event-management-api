from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from a .env file 

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'fallback_secret_key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://dinah_5:123456@localhost:5432/events_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

