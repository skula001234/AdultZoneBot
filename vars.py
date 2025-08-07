import os
from typing import List

API_ID = int(os.getenv("API_ID", ""))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7624888045:AAFIS3GtRHXy")
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://xxxxx:mkooaa@werdeveloper.vxfam.mongodb.net/")
DATABASE_CHANNEL_ID = int(os.getenv("DATABASE_CHANNEL_ID", "-10026550xxxx"))
ADMIN_ID = int(os.getenv("ADMIN_ID", "xxxxxxxx"))
LOG_CHNL = int(os.getenv("LOG_CHNL", "-1002357280xxx"))
ADMIN_USERNAME = os.getenv("ADMIN_USERNAME", "") # Without @
IS_FSUB = bool(os.environ.get("FSUB", True))
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNEL", "-1002528152xxx").split()))
DATABASE_CHANNEL_LOG = int(os.getenv("DATABASE_CHANNEL_ID", "-1002652997xxx"))
FREE_VIDEO_DURATION = int(os.getenv("FREE_VIDEO_DURATION", "240"))

'''
🛡️ Developed by: WeRDeveloper
🚫 Do not attempt to sell, copy, or redistribute this code.

🔗 Official Telegram Channel: https://t.me/WeRdevelopers
📩 Contact (Verified Only): https://t.me/WeRDevX
▶️ YouTube Channel: https://www.youtube.com/@WeRdevelopers

⚠️ Only @WeRDevX is officially managed. Any other accounts are fake.
'''
