from pyrogram import Client, filters, enums
from . import *
import time
import random
from .watchers import classic_watcher

PLAYING = False

LAST = None

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
@Client.on_message(group=classic_watcher)
async def watcher(_, m):
    global BIN, name, LAST
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
    if "has" in txt and "been" in txt and "used." in txt:
        user_n = m.reply_to_message.from_user.first_name.split()[0]
        if name == user_n:
            letter = LAST[0]
            length = len(LAST)
            g = get_classic_word(letter, length, BIN)
            return await _.send_message(m.chat.id, g)
    if "not" in txt and "in" in txt and "my" in txt and "list" in txt:
        user_n = m.reply_to_message.from_user.first_name.split()[0]
        if name == user_n:
            letter = LAST[0]
            length = len(LAST)
            g = get_classic_word(letter, length, BIN)
            return await _.send_message(m.chat.id, g)
    if txt[0].lower() == "turn:":
        formed_name = txt[1]
    else:
        return
    if formed_name == name:
        st_imp = time.time()
        time.sleep(1)
        await _.send_chat_action(m.chat.id, enums.ChatAction.TYPING)
        ind = txt.index("with")
        letter = txt[ind+1].lower()
        ind = txt.index("least")
        length = int(txt[ind+1])
        g = get_classic_word(letter, length, BIN)
        LAST = g
        end_imp = time.time()
        diff = int(end_imp - st_imp)
        await _.send_chat_action(m.chat.id, enums.ChatAction.TYPING)
        await _.send_message(m.chat.id, g)
        await _.send_message(m.chat.id, f"{str(diff)[0:4]}")
        await _.send_chat_action(m.chat.id, enums.ChatAction.CANCEL)
