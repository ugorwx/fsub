#Part of - #CodeXBotz #mrismanaziz

from asyncio import sleep

from pyrogram.errors import FloodWait

from database.sql import query_msg


async def users_info(bot):
    users = 0
    blocked = 0
    identity = await query_msg()
    for id in identity:
        name = bool()
        try:
            name = await bot.send_chat_action(int(id[0]), "typing")
        except FloodWait as e:
            await sleep(e.value)
        except Exception:
            pass
        if bool(name):
            users += 1
        else:
            blocked += 1
    return users, blocked
