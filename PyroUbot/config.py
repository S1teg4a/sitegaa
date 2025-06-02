import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "200"))

DEVS = list(map(int, os.getenv("DEVS", "7752841649").split()))

API_ID = int(os.getenv("API_ID", "28947917"))

API_HASH = os.getenv("API_HASH", "b629511c747b214b0c092931b72a8d22")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7241541909:AAGVBEbUREyuCuhXBsvsoX5dWKf4nCVvAfw")

OWNER_ID = int(os.getenv("OWNER_ID", "7752841649"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-4762088128").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://Userbotdewaa:Userbotdewaa@userbotdewaa.pap1rte.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", " -1002694842430"))
