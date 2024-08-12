import json
import os
from os import getenv

from dotenv import load_dotenv

load_dotenv()


def get_user_list(config, key):
    with open("{}/Madara/{}".format(os.getcwd(), config), "r") as json_file:
        return json.load(json_file)[key]


class Config(object):
    LOGGER = True
    # ᴀᴅᴅ ʏᴏᴜʀ ᴠᴇʀs  (ᴍᴀɪɴ ᴠᴇʀs)
    API_ID = int(getenv("API_ID", "13279715"))
    API_HASH = getenv("API_HASH", "56e198053932ecf216af72a2ddffcd78")
    EVENT_LOGS = int(getenv("EVENT_LOGS", "-1002139608040"))
    DATABASE_URL = getenv(
        "DATABASE_URL",
        "postgres://qszfsijv:y6sYqkEb8Z9lFGBmriG7AYjbSbgAJBVk@peanut.db.elephantsql.com/qszfsijv",
    )  # elephantsql.com
    REDIS_URL = "redis://default:FyNzPZ045GV2JXidIlYVYWExT5d2PDfz@redis-19786.c279.us-central1-1.gce.cloud.redislabs.com:19786"  # redis.os
    MONGO_DB_URL = getenv(
        "MONGO_DB_URL",
        "mongodb+srv://Obito:Obito@obito.uolt8k3.mongodb.net/?retryWrites=true&w=majority",
    )
    TOKEN = getenv("TOKEN", "7118713344:AAEqtTMQQTAFcAj35hk_iYLkfU-lQJDIbuY")
    OWNER_USERNAME = getenv("OWNER_USERNAME", "King_Akaza_Shadow")
    OWNER_ID = int(getenv("OWNER_ID", "7122227582"))
    SUPPORT_CHAT = getenv("SUPPORT_CHAT", "Friends_Zone_l")

    # ɴᴏᴛ ɪᴍᴘᴏʀᴛᴀɴᴛ ᴢᴏɴᴇ, ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴇᴅɪᴛ
    MONGO_DB = "Madara"  # ⚠️ ᴅᴏɴ'ᴛ ᴇᴅɪᴛ
    ARQ_API_URL = "arq.hamker.dev"  # ⚠️ ᴅᴏɴ'ᴛ ᴇᴅɪᴛ
    ARQ_API_KEY = "GFUXSS-XJINVJ-CMIQKI-NHHBNS-ARQ"
    DONATION_LINK = "t.me/obito_shadow"
    HELP_IMG = "https://graph.org/file/9b8b09ce1d5d48f8004f3.jpg"
    START_VIDEO = "https://graph.org/file/2904688233933fd7e64fc.mp4"
    UPDATES_CHANNEL = "Ix_Updates"
    INFOPIC = False
    GENIUS_API_TOKEN = (
        "gIgMyTXuwJoY9VCPNwKdb_RUOA_9mCMmRlbrrdODmNvcpslww_2RIbbWOB8YdBW9"
    )
    SPAMWATCH_API = "tBIAzON4MiJmj_WwVbcI3HSXv03xoOZLgQqcZXgQD~6mvM_Gl0fresvC~FoROHKP"
    REM_BG_API_KEY = None
    OPENWEATHERMAP_ID = None
    WALL_API = None
    TIME_API_KEY = None
    NO_LOAD = ["rss"]
    TEMP_DOWNLOAD_DIRECTORY = "./"  # ⚠️ ᴅᴏɴ'ᴛ ᴇᴅɪᴛ
    LOAD = []  # ⚠️ ᴅᴏɴ'ᴛ ᴇᴅɪᴛ
    DEL_CMDS = True
    BAN_STICKER = None
    WORKERS = 8
    STRICT_GBAN = True
    WEBHOOK = False
    URL = None
    PORT = []
    ALLOW_EXCL = []
    ALLOW_CHATS = True
    CERT_PATH = []
    SPAMWATCH_SUPPORT_CHAT = "Friends_Zone_l"
    BOT_API_URL = "https://api.telegram.org/bot"  # ⚠️ ᴅᴏɴ'ᴛ ᴇᴅɪᴛ
    DRAGONS = [6529892817]  # User id of sudo users
    DEV_USERS = [6529892817]  # User id of dev users
    REQUESTER = [6529892817]  # ⚠️ ᴅᴏɴ'ᴛ ᴇᴅɪᴛ
    DEMONS = [6529892817]  # User id of support users
    INSPECTOR = [6529892817]  # ⚠️ ᴅᴏɴ'ᴛ ᴇᴅɪᴛ
    TIGERS = [6529892817]  # User id of tiger users
    WOLVES = [6529892817]  # User id of whitelist users

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True


# ENJOY
