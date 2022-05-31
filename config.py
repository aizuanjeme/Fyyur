import os
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
# SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:!pass4sure@localhost:5432/fyyur'
SQLALCHEMY_DATABASE_URI = 'postgresql://cedulktzyrtvbp:d90034e6b7ebdadf141847868625f745cd9557d6e2f6d3ce8c912874bfb9ecfc@ec2-34-227-120-79.compute-1.amazonaws.com:5432/d8tncga3uf15s2'
# SQLALCHEMY_DATABASE_URI = 'postgres://cedulktzyrtvbp:d90034e6b7ebdadf141847868625f745cd9557d6e2f6d3ce8c912874bfb9ecfc@ec2-34-227-120-79.compute-1.amazonaws.com:5432/d8tncga3uf15s2'
SQLALCHEMY_TRACK_MODIFICATIONS = False
