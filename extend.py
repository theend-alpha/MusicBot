from pytgcalls import PyTgCalls
from pyrogram import Client

smexy = Client(config.SESSION_NAME, config.API_ID, config.API_HASH)
pytgcalls = PyTgCalls(smexy)
