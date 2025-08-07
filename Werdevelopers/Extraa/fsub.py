'''
🛡️ Developed by: WeRDeveloper
🚫 Do not attempt to sell, copy, or redistribute this code.

🔗 Official Telegram Channel: https://t.me/WeRdevelopers
📩 Contact (Verified Only): https://t.me/WeRDevX
▶️ YouTube Channel: https://www.youtube.com/@WeRdevelopers

⚠️ Only @WeRDevX is officially managed. Any other accounts are fake.
'''


from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from vars import AUTH_CHANNELS
from pyrogram import Client
from pyrogram.types import Message
from pyrogram.errors import UserNotParticipant

async def get_fsub(bot: Client, message: Message) -> bool:
    dy = await bot.get_me()
    user_id = message.from_user.id
    not_joined_channels = []
    for channel_id in AUTH_CHANNELS:
        try:
            await bot.get_chat_member(channel_id, user_id)
        except UserNotParticipant:
            chat = await bot.get_chat(channel_id)
            invite_link = chat.invite_link or await bot.export_chat_invite_link(channel_id)
            not_joined_channels.append((chat.title, invite_link))
    if not_joined_channels:
        join_buttons = []
        for i in range(0, len(not_joined_channels), 2):
            row = []
            for j in range(2):
                if i + j < len(not_joined_channels):
                    title, link = not_joined_channels[i + j]
                    button_text = "🔔 Join Now"
                    row.append(InlineKeyboardButton(button_text, url=link))
            join_buttons.append(row)
        join_buttons.append([InlineKeyboardButton("Try Again", url=f"https://t.me/{dy.username}?start=start")])
        await message.reply(f"**👋 {message.from_user.mention}, it looks like you haven’t joined my updates channel yet.\n\nPlease join the channel to continue using the bot.\n\nSimply tap the button below.**",
                            reply_markup=InlineKeyboardMarkup(join_buttons),)
        return False
    return True

'''
🛡️ Developed by: WeRDeveloper
🚫 Do not attempt to sell, copy, or redistribute this code.

🔗 Official Telegram Channel: https://t.me/WeRdevelopers
📩 Contact (Verified Only): https://t.me/WeRDevX
▶️ YouTube Channel: https://www.youtube.com/@WeRdevelopers

⚠️ Only @WeRDevX is officially managed. Any other accounts are fake.
'''
