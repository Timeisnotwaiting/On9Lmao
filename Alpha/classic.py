from pyrogram import Client, filters, enums
from . import *

PLAYING = False

@Client.on_message(filters.command("classic", hl) & filters.me)
async def classic(_, m):
    global PLAYING, BIN
    if PLAYING:
        return await m.edit("***ALREADY IN GAME***")
    PLAYING = True
    return await m.edit("***STARTED***")

@Client.on_message(filters.command(["end", "stop", "terminate"], hl) & filters.me)
async def endf(_, m):
    global PLAYING
    if not PLAYING:
        return await m.edit("***NO GAME TO TERMINATE***")
    PLAYING = False
    return await m.edit("***TERMINATED***")

name = None
@Client.on_message(group=1)
async def watcher(_, m):
    global BIN, name
    if not PLAYING:
        return
    if not name:
        name = (await _.get_me()).first_name + " "
    if m.from_user.id != on9_id:
        return
    txt = m.text.split()
    if "is" in txt and "accepted." in txt:
        BIN.append(txt[0].lower())
        return
    ind = txt.index("Next:")
    new_l = txt[1:ind]
    formed_name = ""
    for h in new_l:
        formed_name += h
        formed_name += " "
    if formed_name == name:
        await _.send_chat_action(m.chat.id, enums.ChatAction.TYPING)
        ind = txt.index("with")
        letter = txt[ind+1]
        ind = txt.index("least")
        length = int(txt[ind+1])
        g = get_classic_word(letter, length)
        await _.send_chat_action(m.chat.id, enums.ChatAction.CANCEL)
        await _.send_message(m.chat.id, g)
