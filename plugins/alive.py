from pyrogram import filters
from pyrogram import __version__ as pyro_vr
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from modules.config import *
from pyrogram import Client
from modules.config import ALIVE_PIC
 

 
@Client.on_message(filters.command(["alive", "awake"], [".", "!"]) & filters.me)
async def alive(client: Client, e: Message):
    try:
        Alive_msg = f"ðððð¥ ðð¬ðð«ðð¨ð­ ðð¬ ðð§ ðð¢ð«ð ð¥ \n\n"
        Alive_msg += f"â ââââââ â ââââââ â \n"
        Alive_msg += f"âº Vá´ÊsÉªá´É´ : `2.0 Pro` \n"
        Alive_msg += f"âº á´ÊÊá´ á´ á´ÊsÉªá´É´ : `{pyro_vr}` \n"
        Alive_msg += f"âº Uá´á´á´á´á´s : [Já´ÉªÉ´](https://t.me/adityaserver)` \n"
        Alive_msg += f"âº Sá´á´á´á´Êá´ : [Já´ÉªÉ´](https://t.me/adityadiscus) \n"
        Alive_msg += f"â ââââââ â ââââââ â \n\n"
        await e.reply_photo(
        photo=ALIVE_PIC,
        caption=Alive_msg,
        reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton(
                        "â¢ ðð¡ðð§ð§ðð¥ â¢", url="https://t.me/adityaserver")
                ], [
                    InlineKeyboardButton(
                        "â¢ ððð©ð¨ â¢", url="https://github.com/adityabots/kaaluserbot")
                ]],
        ),
    ) 
    except Exception as lol:         
        Alive_msg = f"ðððð¥ ðð¬ðð«ðð¨ð­ ðð¬ ðð§ ðð¢ð«ð ð¥ \n\n"
        Alive_msg += f"â ââââââ â ââââââ â \n"
        Alive_msg += f"âº á´ á´ÊsÉªá´É´ : `2.0 Pro` \n"
        Alive_msg += f"âº PÊÊá´ á´ á´ÊsÉªá´É´ : `1.4.15` \n"
        Alive_msg += f"âº Sá´á´á´á´Êá´ : [Já´ÉªÉ´](https://t.me/adityadiscus) \n"
        Alive_msg += f"â ââââââ â ââââââ â \n\n"
        await e.reply_photo(
        photo=ALIVE_PIC,
        caption=Alive_msg,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("â¢ ðð¡ðð§ð§ðð¥ â¢", url="https://t.me/adityaserver"),
                ],
                [
                    InlineKeyboardButton("â¢ ððð©ð¨ â¢", url="https://github.com/adityabots/kaaluserbot"),
                ],
            ],
        ),
    ) 
