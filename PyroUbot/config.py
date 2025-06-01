import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "200"))

DEVS = list(map(int, os.getenv("DEVS", "5716598718").split()))

API_ID = int(os.getenv("API_ID", "22550997"))

API_HASH = os.getenv("API_HASH", "90aa08d2d7217fbfd511cdff22530fb5")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7915569165:AAF975EB35V9bFkiTP71XN7Q_pGzOk_wkS8")

OWNER_ID = int(os.getenv("OWNER_ID", "6728786795"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-4768074011").split()))

RMBG_API = os.getenv("RMBG_API", "sLja5XNkWjVfJu8g3ZSmrorX")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://sitegaa:sitegaa@cluster0.ip0xswg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", " -4768074011"))
