# Regen & Mod by @shamilhabeebnelli
# Pyrogram - Telegram MTProto API Client Library for Python
# Copyright (C) 2017-2020 Dan <https://github.com/delivrance>
#
# This file is part of Pyrogram.
#
# Pyrogram is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pyrogram is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.


from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
import signal
from utils import USERNAME, FFMPEG_PROCESSES
from config import Config
import os
import sys
U=USERNAME
CHAT=Config.CHAT


HOME_TEXT = "<b>Helo, [{}](tg://user?id={}),\n\n Iam A Bot Project by Technical Wing.\n I Can Manage Group VC.\n\n Hit /help to know about available commands.\n\n 🏷️ Maintained By: @Amani_m_h_d</b> "
HELP = """
🎧 <b>I Can Play Music On VoiceChats 🤪</b>

🎶 **Admin Commands**:

• `/r` __Start Radio__
• `/sr` __Stops Radio Stream__

© Powered By 
[ __@Amani_m_h_d | Technical Wing__ ]
"""



@Client.on_message(filters.command('start'))
async def start(client, message):
    buttons = [
        [
        InlineKeyboardButton("❔ How To Use Me ❔", callback_data="help"),
                ],[
                InlineKeyboardButton('Updates Channel 📌', url='https://t.me/my_test_botz'),
                InlineKeyboardButton('Subscribe YouTube', url='https://m.youtube.com/channel/UCRfF8JZK4MSQXsXVhhzYI3w')
                ],[
                InlineKeyboardButton('👨‍💻 Developer', url='https://t.me/shamilnelli'),
                InlineKeyboardButton('Follow on Instagram', url='https://instagram.com/imad_union/')
                ],[
                InlineKeyboardButton('📜 Source Code 📜', url='https://t.me/nokkiirunnoippokittum'),
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text(text=HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)
    await message.delete()


@Client.on_message(filters.command("help"))
async def show_help(client, message):
    buttons = [
        [
                InlineKeyboardButton('Updates Channel 📌', url='https://t.me/my_test_botz'),
                InlineKeyboardButton('Subscribe YouTube', url='https://m.youtube.com/channel/UCRfF8JZK4MSQXsXVhhzYI3w')
                ],[
                InlineKeyboardButton('👨‍💻 Developer', url='https://t.me/shamilnelli'),
                InlineKeyboardButton('Follow on Instagram', url='https://instagram.com/imad_union/')
                ],[
                InlineKeyboardButton('📜 Source Code 📜', url='https://t.me/nokkiirunnoippokittum'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text(text=HELP, reply_markup=reply_markup)
    await message.delete()
