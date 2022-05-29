import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.delete()
    await message.reply_sticker("CAACAgUAAxkBAAEENxZiNtPdibVkMsjLZrUG9NK4hotHQgAC2wEAAoM12VSdN9ujxVtnUyME")
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""**━━━━━━━━━━━━━━━━━━
Hey {message.from_user.mention()} !

        This is [{bn}](t.me/{bu}), Belongs to THE END network !

┏━━━━━━━━━━━━━━┓
┣★
┣★ ᴍᴀᴅᴇ ʙʏ: [THE END](t.me/THE_END_NETWORK)
┣★
┗━━━━━━━━━━━━━━┛

💞 If you having any queries regarding me, Try: (@THE_END_MUSIC_SUPPORT)
━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Try: add to your group !", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                  ],[
                    InlineKeyboardButton(
                        "✨ Owner ❤️", url=f"https://t.me/{me}"
                    ),
                    InlineKeyboardButton(
                        "✨ Support 💜", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                ],[
                    InlineKeyboardButton(
                        "🔎 Inline 🔎", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "✨ DEv 💫", url="t.me/iTz_DEv_xD"
                    )]
            ]
       ),
    )

