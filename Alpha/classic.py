from pyrogram import Client, filters, enums
from . import *
import time
import random

PLAYING = False

BIN = []

@Client.on_message(filters.command("classic", hl) & filters.me)
async def classic(_, m):
    global PLAYING, BIN
    if PLAYING:
        return await m.edit("***ALREADY IN GAME***")
    PLAYING = True
    return await m.edit("***STARTED***")

@Client.on_message(filters.command(["end", "stop", "terminate"], hl) & filters.me)
async def endf(_, m):
    global PLAYING, BIN
    if not PLAYING:
        return await m.edit("***NO GAME TO TERMINATE***")
    PLAYING = False
    BIN.clear()
    return await m.edit("***TERMINATED***")

name = None
@Client.on_message(group=1)
async def watcher(_, m):
    global BIN, name
    if not PLAYING:
        return
    if not name:
        name = (await _.get_me()).first_name.split()[0]
    if m.from_user.id != on9_id:
        return
    txt = m.text.split()
    if "is" in txt and "accepted." in txt:
        BIN.append(txt[0].lower())
        return
    if txt[0].lower() == "turn:":
        formed_name = txt[1]
    else:
        return
    if formed_name == name:
        await _.send_chat_action(m.chat.id, enums.ChatAction.TYPING)
        ind = txt.index("with")
        letter = txt[ind+1].lower()
        ind = txt.index("least")
        length = int(txt[ind+1])
        if length <= 5:
            time.sleep(random.choice([3, 4, 5]))
        elif length > 5 and length <= 10:
            time.sleep(random.choice([6, 7, 8]))
        else:
            time.sleep(random.choice([9, 10, 11]))
        g = get_classic_word(letter, length, BIN)
        await _.send_chat_action(m.chat.id, enums.ChatAction.CANCEL)
        await _.send_message(m.chat.id, g)
