'''
🛡️ Developed by: WeRDeveloper
🚫 Do not attempt to sell, copy, or redistribute this code.

🔗 Official Telegram Channel: https://t.me/WeRdevelopers
📩 Contact (Verified Only): https://t.me/WeRDevX
▶️ YouTube Channel: https://www.youtube.com/@WeRdevelopers

⚠️ Only @WeRDevX is officially managed. Any other accounts are fake.
'''


from pyrogram import Client, filters
from pyrogram.types import *
from vars import *
from Database.maindb import mdb
from Database.userdb import udb
from datetime import datetime
import pytz, random, asyncio
from Werdevelopers.Extraa.fsub import get_fsub
from pyrogram.enums import ParseMode

async def get_updated_limits():
        global FREE_LIMIT, PRIME_LIMIT
        limits = await mdb.get_global_limits()
        FREE_LIMIT = limits["free_limit"]
        PRIME_LIMIT = limits["prime_limit"]
        return limits

@Client.on_message(filters.command("start") & filters.private)
async def start_command(client, message):
    if await udb.is_user_banned(message.from_user.id):
        await message.reply("**🚫 You are banned from using this bot**",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Support 🧑‍💻", url=f"https://t.me/{ADMIN_USERNAME}")]]))
        return
    if IS_FSUB and not await get_fsub(client, message):return
    if await udb.get_user(message.from_user.id) is None:
        await udb.addUser(message.from_user.id, message.from_user.first_name)
        await client.send_message(LOG_CHNL,text=f"**🆕 #NEW_USER\n👤 User: {message.from_user.mention()}\n🆔 ID: `{message.from_user.id}`**")
    full_name = message.from_user.first_name + (" " + message.from_user.last_name if message.from_user.last_name else "")
    h = datetime.now(pytz.timezone('Asia/Kolkata')).hour
    wish = "Good Morning" if 4 <= h < 12 else "Good Afternoon" if 12 <= h < 17 else "Good Evening" if 17 <= h < 20 else "Good Night"
    msg = f"""<b>👋 {full_name}, {wish}

<blockquote expandable>This bot may contain 18+ content.
Please access it at your own risk.
The material may include explicit or graphic content that is not suitable for minors.</blockquote>

<a href="https://telegra.ph/Terms--Conditions-and-Privacy-Policy-07-01">Terms and Conditions</a></b>"""
    await message.reply_text(msg,
                             reply_markup = InlineKeyboardMarkup(
                                 [[InlineKeyboardButton("Buy Subscription", callback_data="pro")],
                                  [InlineKeyboardButton("Help", callback_data="help"),InlineKeyboardButton("About", callback_data="about")],[InlineKeyboardButton("Close", callback_data="close")]]),
                                  disable_web_page_preview=True,
                                  parse_mode=ParseMode.HTML,
                                  message_effect_id=5104841245755180586)

@Client.on_message(filters.command("getvideos") & filters.private)
async def send_random_video(client: Client, message: Message):
    if await udb.is_user_banned(message.from_user.id):
        await message.reply("**🚫 You are banned from using this bot**",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Support 🧑‍💻", url=f"https://t.me/{ADMIN_USERNAME}")]]))
        return
    limits = await get_updated_limits()
    if limits.get('maintenance', False):
        await message.reply_text("**🛠️ Bot Under Maintenance — Back Soon!**")
        return
    if IS_FSUB and not await get_fsub(client, message):return
    user_id = message.from_user.id
    user = await mdb.get_user(user_id)
    plan = user.get("plan", "free")
    if plan == "prime":
        videos = await mdb.get_all_videos()
    else:
        videos = await mdb.get_free_videos()
    if not videos:
        await message.reply_text("No videos available at the moment.")
        return
    random_video = random.choice(videos)
    daily_count = user.get("daily_count", 0)
    daily_limit = user.get("daily_limit", FREE_LIMIT)

    if daily_count > daily_limit:
        await message.reply_text(f"**🚫 You've reached your daily limit of {daily_limit} videos.\n\n>Limit will reset every day at 5 AM (IST).**")
    else:
        try:
            caption_text = "<b>🔞 Powered by: [AdultHUB4All](https://t.me/adulthub4all)\n\n<blockquote>⚠️ This file will auto delete in 5 minutes!</blockquote>\n\n💾 Please *save it in your Saved Messages* or *forward it elsewhere* to keep it safe! 🔐</b>"
            video_id = random_video["video_id"]
            dy = await client.copy_message(
                chat_id=message.chat.id,
                from_chat_id=DATABASE_CHANNEL_ID,
                message_id=video_id,
                caption=caption_text)
            await mdb.increment_daily_count(user_id)
            await asyncio.sleep(300)
            await dy.delete()
        except Exception as e:
            print(f"Error sending video: {e}")
            await message.reply_text("Failed to send video..")

@Client.on_message(filters.command("plans") & filters.private)
async def show_plans(client: Client, message: Message):
    current_limits = await mdb.get_global_limits()
    PRIME_TXT = f"""<b><u>Free Plan:</u>

» This free plan allows you only {current_limits['free_limit']} files per day.
» Videos must be less than 5 minutes in length.
» Free forever.

If you wish to upgrade, simply choose your preferred plan from the options below.

<a href="https://telegra.ph/Terms--Conditions-and-Privacy-Policy-07-01">Terms and Conditions</a></b>"""
    await message.reply_text(
        PRIME_TXT,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton('Silver Plan', callback_data='silver')],
            [InlineKeyboardButton('Gold Plan', callback_data='gold')],
            [InlineKeyboardButton('Diamond Plan', callback_data='diamond')],
            [InlineKeyboardButton('Back', callback_data='home'),
            InlineKeyboardButton('Close', callback_data='close')]
        ]),
        disable_web_page_preview=True,
         parse_mode=ParseMode.HTML)
    

'''
🛡️ Developed by: WeRDeveloper
🚫 Do not attempt to sell, copy, or redistribute this code.

🔗 Official Telegram Channel: https://t.me/WeRdevelopers
📩 Contact (Verified Only): https://t.me/WeRDevX
▶️ YouTube Channel: https://www.youtube.com/@WeRdevelopers

⚠️ Only @WeRDevX is officially managed. Any other accounts are fake.
'''
