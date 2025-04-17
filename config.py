# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

from os import environ 

class Config:
    API_ID = int(environ.get("API_ID", "21688431"))
    API_HASH = environ.get("API_HASH", "db274cb8e9167e731d9c8305197badeb")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7666217884:AAEWZtNvCtaV5DMT0Y5k_sneBEVxaTvPZxo") 
    BOT_SESSION = environ.get("BOT_SESSION", "vjbot") 
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://Forwardbot:<dbForwardbot@forward.3jlpu.mongodb.net/?retryWrites=true&w=majority&appName=Forward")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Forward")
    BOT_OWNER = int(environ.get("BOT_OWNER", "6861892595"))

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []

# Don't Remove Credit Tg - @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01
