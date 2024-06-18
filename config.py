# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "26305156")

API_HASH = os.environ.get("API_HASH", "9937930c368c669ca905e9a95aa712f0")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7466479376:AAFUy78h73xK6y5vibmNBKD5AftNAUfQZ60") 

FORCE_SUB = os.environ.get("FORCE_SUB", "moviebot_channel") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "movieworld")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://kallu:kallu@movieworld.5aaiagq.mongodb.net/?retryWrites=true&w=majority&appName=movieworld")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/69b2cdff38834e2eee83b.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5606411877').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
