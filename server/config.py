from dotenv import load_dotenv
import os

load_dotenv()  

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'fallback_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///events.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

