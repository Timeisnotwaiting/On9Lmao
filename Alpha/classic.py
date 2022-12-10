from pyrogram import Client, filters, enums
from . import hl, on9_id, PLAYING, ews

BIN = {}
@Client.on_message(filters.command("classic", hl) & filters.me)
async def classic(_, m):
    global PLAYING
    if PLAYING:
        return await m.edit("***ALREADY IN GAME***")
    
    
