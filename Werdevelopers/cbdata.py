'''
🛡️ Developed by: WeRDeveloper
🚫 Do not attempt to sell, copy, or redistribute this code.

🔗 Official Telegram Channel: https://t.me/WeRdevelopers
📩 Contact (Verified Only): https://t.me/WeRDevX
▶️ YouTube Channel: https://www.youtube.com/@WeRdevelopers

⚠️ Only @WeRDevX is officially managed. Any other accounts are fake.
'''


from pyrogram import Client
from pyrogram.types import *
from datetime import datetime
import pytz
from vars import ADMIN_USERNAME, ADMIN_ID
from Database.maindb import mdb
from pyrogram.enums import ParseMode

@Client.on_callback_query()
async def cb_handler(client, q: CallbackQuery):
    data = q.data

    if data == "close":
        await q.answer("Thanks for closing ❤️\n- @YurinaXbot", show_alert=True)
        await q.message.delete()

    elif data == "help":
        await q.edit_message_text(
            text=f"""<b>This bot is specially designed for 18+ users and allows you to access content easily through simple commands.
            
You can use /getvideo to request an 18+ video and /myplan to check your current daily limit and subscription details.

Along with the free plan, we also offer premium plans,

» Silver
» Gold
» Diamond

which provide higher limits, faster access, and better features for a smoother experience.

Please note, this bot is strictly for adult users (18+) and you are using it at your own responsibility.

<a href="https://telegra.ph/Terms--Conditions-and-Privacy-Policy-07-01">Terms and Conditions</a></b>""",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("About", callback_data="about")],
                [InlineKeyboardButton("Admin", callback_data="admincmds"),
                 InlineKeyboardButton("Home", callback_data="home")]]),
            disable_web_page_preview=True,
            parse_mode=ParseMode.HTML
        )

    elif data == "about":
        b = await client.get_me()
        await q.edit_message_text(
            text=f"""<b><blockquote>📄 Bot Info</blockquote>
             
» Bot Name - <a href='tg://user?id={b.id}'>{b.first_name}</a>
» Developer - <a href='https://t.me/{ADMIN_USERNAME}'>{ADMIN_USERNAME}</a>
» Updates - <a href='https://t.me/adulthub4all'>AdultHub4All</a>

<blockquote>⚙️ Bot Setup Details</blockquote>

» Version - V0.3
» Language - <a href='https://www.python.org/download/releases/3.0/'>Python3</a>
» Library - <a href='https://docs.pyrogram.org/'>Pyrogram</a>
» Database - <a href='https://www.mongodb.com/'>MongoDB</a>

<blockquote>⚠️ If you facing any error, Please Contact - <a href='https://t.me/{ADMIN_USERNAME}'>Support</a></blockquote>

<a href="https://telegra.ph/Terms--Conditions-and-Privacy-Policy-07-01">Terms and Conditions</a></b>""",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Home", callback_data="home"),
                 InlineKeyboardButton("Help", callback_data="help")]]),
            disable_web_page_preview=True,
            parse_mode=ParseMode.HTML
        )

    elif data == "home":
        full_name = q.from_user.first_name + \
            (" " + q.from_user.last_name if q.from_user.last_name else "")
        h = datetime.now(pytz.timezone('Asia/Kolkata')).hour
        wish = "Good Morning" if 4 <= h < 12 else "Good Afternoon" if 12 <= h < 17 else "Good Evening" if 17 <= h < 20 else "Good Night"
        await q.edit_message_text(
            text=f"""<b>👋 {full_name}, {wish}

<blockquote expandable>This bot may contain 18+ content.
Please access it at your own risk.
The material may include explicit or graphic content that is not suitable for minors.</blockquote>

<a href="https://telegra.ph/Terms--Conditions-and-Privacy-Policy-07-01">Terms and Conditions</a></b>""", reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Buy Subscription", callback_data="pro")],
                 [InlineKeyboardButton("Help", callback_data="help"), InlineKeyboardButton("About", callback_data="about")], [InlineKeyboardButton("Close", callback_data="close")]]),
            disable_web_page_preview=True,
            parse_mode=ParseMode.HTML)

    elif data == "pro":
        current_limits = await mdb.get_global_limits()
        PRIME_TXT = f"""<b><u>Free Plan:</u>

<blockquote expandable>» This free plan allows you only {current_limits['free_limit']} files per day.

» Videos must be less than 5 minutes in length.

» Free forever.</blockquote>

If you wish to upgrade, simply choose your preferred plan from the options below.

<a href="https://telegra.ph/Terms--Conditions-and-Privacy-Policy-07-01">Terms and Conditions</a></b>"""
        await q.edit_message_text(
            PRIME_TXT,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton('Silver Plan', callback_data='silver')],
                [InlineKeyboardButton('Gold Plan', callback_data='gold')],
                [InlineKeyboardButton('Diamond Plan', callback_data='diamond')],
                [InlineKeyboardButton('Back', callback_data='home'),
                InlineKeyboardButton('Close', callback_data='close')]
            ]),
            disable_web_page_preview=True,
            parse_mode=ParseMode.HTML
        )

    elif data == "silver":
        current_limits = await mdb.get_global_limits()
        await q.edit_message_text(
            text=f"""<b><u>Silver Plan</u>

» 1 Week - 25 INR
» This silver plan allows you {current_limits['prime_limit']} files per day.

<a href='https://files.catbox.moe/tu5hr1.jpg'>Click To Get QR</a>

<blockquote expandable>Note: Once you select a plan, it cannot be changed please choose carefully. Payments are non-refundable, so make sure to review everything before proceeding.</blockquote>

💬 Contact @{ADMIN_USERNAME} to upgrade your plan</b>""",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Back", callback_data="pro")]]),
            disable_web_page_preview=True,
            parse_mode=ParseMode.HTML)

    elif data == "gold":
        current_limits = await mdb.get_global_limits()
        await q.edit_message_text(
            text=f"""<b><u>Gold Plan</u>

» 15 Days - 40 INR
» This Gold plan allows you {current_limits['prime_limit']} files per day.

<a href='https://files.catbox.moe/tu5hr1.jpg'>Click To Get QR</a>

<blockquote expandable>Note: Once you select a plan, it cannot be changed please choose carefully. Payments are non-refundable, so make sure to review everything before proceeding.</blockquote>

💬 Contact @{ADMIN_USERNAME} to upgrade your plan</b>""",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Back", callback_data="pro")]]),
            disable_web_page_preview=True,
            parse_mode=ParseMode.HTML
        )

    elif data == "diamond":
        current_limits = await mdb.get_global_limits()
        await q.edit_message_text(
            text=f"""<b><u>Diamond Plan</u>

» 1 Month - 60 INR
» This Diamond plan allows you {current_limits['prime_limit']} files per day.

<a href='https://files.catbox.moe/tu5hr1.jpg'>Click To Get QR</a>

<blockquote expandable>Note: Once you select a plan, it cannot be changed please choose carefully. Payments are non-refundable, so make sure to review everything before proceeding.</blockquote>

💬 Contact @{ADMIN_USERNAME} to upgrade your plan</b>""",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Back", callback_data="pro")]]),
            disable_web_page_preview=True,
            parse_mode=ParseMode.HTML
        )

    elif data == "admincmds":
        if q.from_user.id != ADMIN_ID:
            await q.answer("You are not my admin ❌", show_alert=True)
        else:
            t = """<b><u>⭐ Admin Commands</u>
                                      
» /setlimit — Increase the daily usage limit for any user (applies to both Free and Prime users).

» /maintenance — Toggle maintenance mode ON or OFF.

» /prime — Add a user to the Prime membership.

» /remove — Remove a user from Prime membership.

» /deleteall — Delete all videos from the database.

» /delete — Delete a specific video using its Telegram message ID.

» /broadcast — Send a message broadcast to all users.

» /ban — Ban a specific user.

» /unban — Unban a specific user.

» /stats — View detailed bot statistics.</b>"""
            await q.edit_message_text(t,
                                      reply_markup=InlineKeyboardMarkup(
                                          [[InlineKeyboardButton("Back", callback_data="help")]]))


'''
🛡️ Developed by: WeRDeveloper
🚫 Do not attempt to sell, copy, or redistribute this code.

🔗 Official Telegram Channel: https://t.me/WeRdevelopers
📩 Contact (Verified Only): https://t.me/WeRDevX
▶️ YouTube Channel: https://www.youtube.com/@WeRdevelopers

⚠️ Only @WeRDevX is officially managed. Any other accounts are fake.
'''
