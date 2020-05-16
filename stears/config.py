import os
from dotenv import load_dotenv
load_dotenv()

# development and production secret key

DEV_SECRET_KEY = os.getenv('SECRET_KEY')
PROD_SECRET_KEY = os.getenv('SECRET_KEY')

# debug settings for dev and production

DEV_DEBUG = True
PROD_DEBUG = False




