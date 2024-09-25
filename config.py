# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "29236719"))
API_HASH = getenv("API_HASH", "1ccf1bd0a86af974e3210a55f662c062")
BOT_TOKEN = getenv("BOT_TOKEN", "7654455845:AAErH5gfWVeu5-zoHO5Q8rvGYHgI_Ijc6nM")
OWNER_ID = list(map(int, getenv("OWNER_ID", "893383574").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://keshavptdr98:D8lbdQUW4euV07l4@cluster0.dok926y.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP = getenv("LOG_GROUP", "-1002074744533")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002477425890"))
