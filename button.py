from pyrogram.types import InlineKeyboardButton, Message

KID = "1057412250"


def add_button(message: Message):
    button = InlineKeyboardButton(text="🥀 ᴅᴇᴠᴇʟᴏᴩᴇʀ 🥀",url=f"tg://user?id={KID}")
    if message.reply_markup:
        message.reply_markup.inline_keyboard.append([button])
    else:
        message.reply_markup = InlineKeyboardMarkup([[button]])
