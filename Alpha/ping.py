from pyrogram import Client, filters
from . import hl, startTime
import time

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for i in range(len(time_list)):
        time_list[i] = str(time_list[i]) + time_suffix_list[i]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time

@Client.on_message(filters.command("ping", hl) & filters.me)
async def pinging(_, m):
    st = time.time()
    upt = get_readable_time(int(time.time()-startTime))
    end = time.time()
    return await m.edit(f"Uptime : {upt}\n\nPing : {(end-st)*1000}ms")
