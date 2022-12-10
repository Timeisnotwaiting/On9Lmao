from pyrogram import Client, filters
from . import BIN, PLAYERS, PLAYING, get_classic_word, on9_id

@Client.on_message(group=1)
async def watcher(_, m):
    global PLAYERS, BIN
    if not PLAYERS:
        if m.from_user.id != on9_id:
            return
        txt = m.text.split()
        if "Turn" in txt and "order:" in txt:
            ind = txt.index("order:")
            tot = len(txt)
            left = tot-(ind+1)
            for i in range(1, left+1):
                PLAYERS.append(txt[i])
       
