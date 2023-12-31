from defs import getUrl, getcards, phone
from pyrogram import Client, filters
from button import add_button
import asyncio
import os, sys
import re
import requests
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from datetime import datetime
import pytz
import config
from button import add_button



app = Client("bot",config.API_ID,config.API_HASH,bot_token=config.BOT_TOKEN)
app2 = Client("UB client",api_id=config.API_ID,api_hash=config.API_HASH,session_string=str(config.SESSION))
SEND_ID = -1001943074057

ccs = []
chats = [
    '@HQ_cc_Live',
]

with open('cards.txt', 'r') as r:
    temp_cards = r.read().splitlines()

for x in temp_cards:
    car = getcards(x)
    if car:
        ccs.append(car[0])
    else:
        continue

@app.on_message()
def handle_message(client, message):
    add_button(message)
        


@app.on_message(filters.chat(chats) & filters.text)
async def my_event_handler(client: Client, message: Message):
    ist_timezone = pytz.timezone('Asia/Kolkata')
    current_time = datetime.now(tz=ist_timezone).strftime("%a %b %d %H:%M:%S %Y")

    if message.reply_markup:
        text = message.reply_markup.stringify()
        urls = getUrl(text)
        if not urls:
            return
        text = requests.get(urls[0]).text
    else:
        text = message.text
    ...

    if message.reply_markup:
        text = message.reply_markup.stringify()
        urls = getUrl(text)
        if not urls:
            return
        text = requests.get(urls[0]).text
    else:
        text = message.text
    cards = getcards(text)
    if not cards:
        return
    cc, mes, ano, cvv = cards
    if cc in ccs:
        return
    ccs.append(cc)
    extra = cc[0:0 + 12]
    bin = requests.get(f'https://bins.antipublic.cc/bins/{cc[:6]}')
    if not bin:
        return
    bin_json = bin.json()
    fullinfo = f"{cc}|{mes}|{ano}|{cvv}"
    # print(f'{cc}|{mes}|{ano}|{cvv}')
    print(f'{cc}|{mes}|{ano}|{cvv} - ALPHA XOP [a+]')
    with open('cards.txt', 'a') as w:
        w.write(fullinfo + '\n')
#    await app.send_photo(
    await app.send_message(
        chat_id=SEND_ID,
#        photo='heart4youu.jpg',
#        caption=f"""
        text=f"""
══════════════════════
                тσχιᴄ ѕᴄяαρρєя    
══════════════════════

**• ᴄᴀʀᴅ ⥁**
  ⤷ `{cc}|{mes}|{ano}|{cvv}` 
**━━━━━━━━━━━━━━━━━━━**
**• ʙɪɴ ➻** `{cc[:6]}` | {bin_json['country_flag']}

**• ɪɴғᴏ ➻**  `{bin_json['type']}` 
**• ᴛʏᴘᴇ ➻** `{bin_json['brand']}`
**• ʙᴀɴᴋ ➻** `{bin_json['bank']}`
**• ᴄᴏᴜɴᴛʀʏ ➻** `{bin_json['country_name']}` | {bin_json['country_flag']} 

**• ᴇxᴛʀᴀ ➻**
  ⤷ `{extra}xxxx|{mes}|{ano}|{cvv}` 
**━━━━━━━━━━━━━━━━━━━**
**Time:** `{current_time}` (IST)
""",
)
add_button(Message)



@app.on_message(filters.outgoing & filters.regex(r'.lives'))
async def my_event_handler(client: Client, message: Message):
    await message.reply_document(document='cards.txt')
    await asyncio.sleep(15)


app.run()
