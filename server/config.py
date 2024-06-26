from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from a .env file 

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '0d218c33670f873391e5c5fdc8d309ad92ea061bacd1bfb8'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://dinah_5:123456@localhost:5432/events_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

