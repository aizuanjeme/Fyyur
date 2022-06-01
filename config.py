import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.urandom(32)
# SECRET_KEY = os.getenv('SECRET_KEY')

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

WTF_CSRF_SECRET_KEY = os.getenv('stephanie')

WTF_CSRF_ENABLED = False

# Connect to the database


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:!pass4sure@localhost:5432/fyyur'
# When deploying to Heroku
SQLALCHEMY_TRACK_MODIFICATIONS = False

# SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') 
# if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
#     SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
