# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re
from os import environ,getenv
from Script import script 

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '3335796'))
API_HASH = environ.get('API_HASH', '138b992a0e672e8346d8439c3f42ea78')
BOT_TOKEN = environ.get('BOT_TOKEN', "5088657122:AAELk-O6R8rYxzqXNvWWRhtl2O0-FNLwHS0")

PICS = (environ.get('PICS', 'https://telegra.ph/file/19eeb26fa2ce58765917a.jpg')).split() #SAMPLE PIC
NOR_IMG = environ.get("NOR_IMG", "https://telegra.ph/file/19eeb26fa2ce58765917a.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://t.me/dlchinHub")
SPELL_IMG = environ.get("SPELL_IMG", "https://telegra.ph/file/19eeb26fa2ce58765917a.jpg")

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '763990585').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001792962793').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
PREMIUM_USER = [int(user) if id_pattern.search(user) else user for user in environ.get('PREMIUM_USER', '').split()]
AUTH_CHANNEL = environ.get('AUTH_CHANNEL', "-1001792962793")

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://sushankm16:4i1WAfPYKWyqPIDD@cluster0.sngp9pz.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "vkbotsthalpathy")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

PORT = environ.get("PORT", "8080")

LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001792962793'))



                           # Don't Remove Credit @VJ_Botz
                           # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
                           # Ask Doubt on telegram @KingVJ01


# Online Stream and Download
NO_PORT = bool(environ.get('NO_PORT', False))
APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = environ.get('APP_NAME')
else:
    ON_HEROKU = False
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
URL = "https://demo-gsmz.onrender.com".format(FQDN) if ON_HEROKU or NO_PORT else \
    "https://demo-gsmz.onrender.com/".format(FQDN, PORT)
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
WORKERS = int(environ.get('WORKERS', '4'))
SESSION_NAME = str(environ.get('SESSION_NAME', 'LazyBot'))
MULTI_CLIENT = False
name = str(environ.get('name', 'TechVJBot'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME'))

else:
    ON_HEROKU = False
HAS_SSL=bool(getenv('HAS_SSL',False))
if HAS_SSL:
    URL = "https://demo-gsmz.onrender.com/".format(FQDN)
else:
    URL = "https://demo-gsmz.onrender.com/".format(FQDN)



LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
