from pyrogram.client import Client
from vars import *
import time

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Adultzonebot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=200,
            plugins={"root": "Werdevelopers"},
            sleep_threshold=15,
        )
        self.START_TIME = time.time()

    async def start(self):
        await super().start()
        me = await self.get_me()
        print(f"::==>> Dypixx Tech <<==::\n┈━═☆ {me.first_name} ☆═━┈")

    async def stop(self, *args):
        await super().stop()
        me = await self.get_me()
        print(f"{me.first_name} is stopped...")

bot = Bot()


'''
🛡️ Developed by: WeRDeveloper
🚫 Do not attempt to sell, copy, or redistribute this code.

🔗 Official Telegram Channel: https://t.me/WeRdevelopers
📩 Contact (Verified Only): https://t.me/WeRDevX
▶️ YouTube Channel: https://www.youtube.com/@WeRdevelopers

⚠️ Only @WeRDevX is officially managed. Any other accounts are fake.
'''


