from dotenv import load_dotenv
import os

load_dotenv()  # Loads environment variables from .env file

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'fallback_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///events.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Add any other configuration variables here

