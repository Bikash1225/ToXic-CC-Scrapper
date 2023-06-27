from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def add_button(message):
    button = InlineKeyboardButton(text="🥀 ᴅᴇᴠᴇʟᴏᴩᴇʀ 🥀", url="https://example.com")
    keyboard = InlineKeyboardMarkup([[button]])

    if message.reply_markup:
        message.edit_reply_markup(reply_markup=message.reply_markup.inline_keyboard + keyboard.inline_keyboard)
    else:
        message.edit_reply_markup(reply_markup=keyboard)
