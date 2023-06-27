from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

KID = "1057412250"


def handle_message(client, message):
    button = InlineKeyboardButton(text="🥀 ᴅᴇᴠᴇʟᴏᴩᴇʀ 🥀", url=f"tg://user?id={KID}")

    if message.reply_markup:
        message.edit_reply_markup(reply_markup=message.reply_markup.inline_keyboard + [[button]])
    else:
        message.edit_reply_markup(reply_markup=InlineKeyboardMarkup([[button]]))

