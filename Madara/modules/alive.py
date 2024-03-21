import random
from sys import version_info

from pyrogram import __version__ as pver
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram import __version__ as lver
from telethon import __version__ as tver

from Madara import BOT_NAME, pgram
from Uchiha.helper import PHOTO

ASAU = [
    [
        InlineKeyboardButton(
            text="𝗨𝗣𝗗𝗔𝗧𝗘𝗦", url=f"https://t.me/Muichiro_Updates"
        ),
        InlineKeyboardButton(
            text="𝗦𝗨𝗣𝗣𝗢𝗥𝗧", url=f"https://t.me/Muichiro_support"
        ),
    ],
]


@pgram.on_message(filters.command("alive"))
async def awake(_, message: Message):
    await message.reply_photo(
        random.choice(PHOTO),
        caption=f"""**ʜᴇʏ, ɪ ᴀᴍ {BOT_NAME}**
    ➖➖➖➖➖➖➖➖➖➖➖➖
          ➖➖➖➖➖➖➖
**𝗠𝗬 𝗢𝗪𝗡𝗘𝗥 :** [𝖢𝖮𝖭𝖢](https://t.me/Conc_chemical)
**𝗗𝗘𝗩𝗘𝗟𝗢𝗣𝗘𝗥 :** [𝖢𝖧𝖤𝖬𝖨𝖢𝖠𝖫](https://t.me/Conc_chemical)
» **𝗟𝗜𝗕𝗥𝗔𝗥𝗬 𝗩𝗘𝗥𝗦𝗜𝗢𝗡 :** `{lver}`
» **𝗧𝗘𝗟𝗘𝗧𝗛𝗢𝗡 𝗩𝗘𝗥𝗦𝗜𝗢𝗡 :** `{tver}`
» **𝗣𝗬𝗥𝗢𝗚𝗥𝗔𝗠 𝗩𝗘𝗥𝗦𝗜𝗢𝗡 :** `{pver}`
» **𝗣𝗬𝗧𝗛𝗢𝗡 𝗩𝗘𝗥𝗦𝗜𝗢𝗡 :** `{version_info[0]}.{version_info[1]}.{version_info[2]}`
""",
        reply_markup=InlineKeyboardMarkup(ASAU),
    )


__mod_name__ = "𝗔𝗟𝗜𝗩𝗘"
