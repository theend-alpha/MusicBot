from pytgcalls import PyTgCalls
from pyrogram import Client
from typing import List
from typing import Union
from pyrogram import filters
import config
from config import API_ID, API_HASH, BOT_TOKEN 

COMMAND_PREFIXES = '/'

SUPPORT_GROUP = "BTS_CHAT_ZONE"

UPDATES_CHANNEL = "BTS_CHAT_ZONE_S"

GROUP = "BTS_CHAT_ZONE"

CHANNEL = "BTS_CHAT_ZONE_S"

other_filters = filters.group & ~ filters.edited & \
    ~ filters.via_bot & ~ filters.forwarded
other_filters2 = filters.private & ~ filters.edited \
    & ~ filters.via_bot & ~ filters.forwarded

def command(commands: Union[str, List[str]]):
    return filters.command(commands, COMMAND_PREFIXES)

smexy = Client(config.SESSION_NAME, config.API_ID, config.API_HASH)
pytgcalls = PyTgCalls(smexy)

app = Client(
    "MusicBot",
    API_ID,
    API_HASH,
    BOT_TOKEN,
