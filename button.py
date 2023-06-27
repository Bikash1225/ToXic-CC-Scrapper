from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import Client
from pyrogram.types import Message

KID = "1057412250"

def add_button(message: Message):
    button = InlineKeyboardButton(text="🥀 ᴅᴇᴠᴇʟᴏᴩᴇʀ 🥀", url=f"tg://user?id={KID}")
    if message.edit_reply_markup:
        message.edit_reply_markup(reply_markup=message.edit_reply_markup.inline_keyboard + [[button]])
    else:
        message.edit_reply_markup(reply_markup=InlineKeyboardMarkup([[button]]))
