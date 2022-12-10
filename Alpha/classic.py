from pyrogram import Client, filters, enums
from . import hl, on9_id

@Client.on_message(filters.command("classic", hl) & filters.me)
async def classic(_, m):
    
    
