from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "21432914"))
API_HASH = getenv("API_HASH", " 4d65415fcce04e8076acee5b6688c1b1")

BOT_TOKEN = getenv("BOT_TOKEN", "7874236359:AAGEMmYoMStr2EKNWtAhXjnvPz47TMaKWZI")
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://EXONTESTMONGO:EXONTESTMONGO@cluster0.bviw7ic.mongodb.net/?retryWrites=true&w=majority")

OWNER_ID = int(getenv("OWNER_ID", 5617239137))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Nxt_Bots")
