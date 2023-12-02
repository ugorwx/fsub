#CodeXBotz #mrismanaziz

import os

from bot import Bot
from config import (
    ADMINS,
    API_HASH,
    API_ID,
    CHANNEL_DB,
    DATABASE_URL,
    FORCE_MESSAGE,
    FORCE_SUB_1,
    FORCE_SUB_2,
    FORCE_SUB_3,
    FORCE_SUB_4,
    LOGGER,
    RESTRICT,
    START_MESSAGE,
    BOT_TOKEN,
)
from pyrogram import filters
from pyrogram.types import Message


@Bot.on_message(filters.command("logs") & filters.user(ADMINS))
async def get_bot_logs(client: Bot, m: Message):
    bot_log_path = "logs.txt"
    if os.path.exists(bot_log_path):
        try:
            await m.reply_document(
                bot_log_path,
                quote=True,
            )
        except Exception as e:
            os.remove(bot_log_path)
            LOGGER(__name__).warning(e)
    elif not os.path.exists(bot_log_path):
        await m.reply_text("Tidak ada logs yang ditemukan!")


@Bot.on_message(filters.command("vars") & filters.user(ADMINS))
async def varsFunc(client: Bot, message: Message):
    msg = await message.reply_text("Tunggu Sebentar...")
    text = f"""
<b>MANDATORY VARS</b>
ADMINS = <code>{ADMINS}</code>
API_ID = <code>{API_ID}</code>
API_HASH = <code>{API_HASH}</code>
BOT_TOKEN = <code>{BOT_TOKEN}</code>
CHANNEL_DB = <code>{CHANNEL_DB}</code>
DATABASE_URL = <code>{DATABASE_URL}</code>
    
<b>OPTIONAL VARS</b>
RESTRICT = <code>{RESTRICT}</code>
FORCE_SUB_1 = <code>{FORCE_SUB_1}</code>
FORCE_SUB_2 = <code>{FORCE_SUB_2}</code>
FORCE_SUB_3 = <code>{FORCE_SUB_3}</code>
FORCE_SUB_4 = <code>{FORCE_SUB_4}</code>
START_MESSAGE = <code>{START_MESSAGE}</code>
FORCE_MESSAGE = <code>{FORCE_MESSAGE}</code>
"""
    await msg.edit_text(text)
