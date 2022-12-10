from pyrogram import Client, idle
from config import *

yashu = Client(":Alpha-Op:", api_id=API_ID, api_hash=API_HASH, string_session=STRING_SESSION, plugins=dict(root="Alpha"))

yashu.start()
print("bot started !")
idle()
