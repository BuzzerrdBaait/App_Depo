"""
Helpful links:

All settings variables:        https://docs.djangoproject.com/en/5.0/ref/settings/

Going to production checklist: https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

"""

from pathlib import Path
import os
import logging


"""
    For some reason, when I import from the same folder it gives an error.

So what I had to do is modify the modified logging function to the settings.py

the next section is going to modify the logging captions and change their colors!


!! Note to self. Django runs settings.py 2x upon start so may want to limit calling function to 1 time but it is okay now.
"""


"""

OVERWRITE log colors with ANSI escape codes

"""

class Log_Colors:

     DEBUG = '\033[96m'  #Cyan

     INFO = '\033[92m'   #Green

     WARNING = '\033[93m'  #Yellow

     ERROR = '\033[91m'   # Red

     CRITICAL = '\033[95m' # Magenta

     RESET = '\033[0m'  #Reset to default color



class ColoredFormatter(logging.Formatter):

     def format(self, record):

          log_colors = {
               'DEBUG' : Log_Colors.DEBUG,
               'INFO'  : Log_Colors.INFO,
               'WARNING': Log_Colors.WARNING,
               'ERROR': Log_Colors.ERROR,
               'CRITICAL': Log_Colors.CRITICAL
          }

          color = log_colors.get(record.levelname, Log_Colors.RESET)

          record.msg=f"{color}{record.msg}{Log_Colors.RESET}"

          return super().format(record)
     
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


logger= logging.getLogger()

for handler in logger.handlers:

     handler.setFormatter(ColoredFormatter('%(asctime)s - %(levelname)s - %(message)s'))



"""
_.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-._

USAGES
   logger.debug("debug message"),
   logger.info("info message"),
   logger.error('you used the wrong variable")
   logger.critical("critical message)

   E N D ------- OF -------  LOGGING  -------- MODDING
   
   Now onto our settings.py   
_.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-._

"""  

"GENERAL VARIABLES"

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get('DJANGO_SECRET')
ROOT_URLCONF = 'app_depot.urls'
WSGI_APPLICATION = 'app_depot.wsgi.application'

STATIC_URL='static/'

STATICFILES_DIRS=[
     os.path.join(BASE_DIR,'static'),
]

"""TIME ZONE"""
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

"""DATABASE VARIABLES"""

SCHEMA_NAME='app_depo'
DB_USER= os.environ.get('DB_USER')
DB_PASSWORD= os.environ.get('DB_PASSWORD')
DB_Credentials=[SCHEMA_NAME,DB_USER,DB_PASSWORD]

"""MEDIA  /   IMAGES    /    VIDEOS"""

MEDIA_URL='/media/'
MEDIA_ROOT= os.path.join(BASE_DIR,'media')

"""DONT FORGET TO TURN DEBUG TO FALSE IN PRODUCTION"""

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'fcapp',
    'ilovecookbooks',
    'home_page',
    'profile_management',
    'experimental_playground',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


AUTH_USER_MODEL = 'profile_management.User_Profile'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
             os.path.join(BASE_DIR,'templates','home_page'),
             os.path.join(BASE_DIR,'templates','profile_management'),
             os.path.join(BASE_DIR,'templates','experimental_playground'),
             os.path.join(BASE_DIR,'templates','ilovecookbooks'),
             os.path.join(BASE_DIR,'templates','flashcards'),
        ],

        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]



if None in DB_Credentials:
 
    logger.warning(" _.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-._\n                                      Database credentials are showing as None.\n                                     Defaulting to SQLite until you configure local variables.\n                                     Your changes will not save across sessions!! \n                                     _.-.__.-.__.-.__.-.__.-.__.-.__.-.__.-._ \n")
 
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}
else:
     
    DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': SCHEMA_NAME,
        'USER' : DB_USER,
        'PASSWORD' : DB_PASSWORD,
        'HOST' : '127.0.0.1',
        'PORT' : '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
            }
          }
     }


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
