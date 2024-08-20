from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

class Config(object):
    # required config variables
    API_HASH = getenv("API_HASH", "8b09f7f48b3d13eb9fba2e617e349e2e"))                # get from my.telegram.org
    API_ID = int(getenv("API_ID", "29355342"))                  # get from my.telegram.org
    BOT_TOKEN = getenv("BOT_TOKEN", "6361658149:AAF5_1hq9D1LHg9XsJDyo27BszFgQDn0QiI"))              # get from @BotFather
    DATABASE_URL = getenv("DATABASE_URL", "mongodb+srv://vishalpandeynkp:Bal6Y6FZeQeoAoqV@cluster0.dzgwt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"))        # from https://cloud.mongodb.com/
    HELLBOT_SESSION = getenv("HELLBOT_SESSION", "BQG_7U4AODyRVlDQPtmSHN2-8NhXufzMLrfAzvuUnic5sxSC1faK2ndJNDtzsIXkEuvRQkzH4AfgMpXwduf_vtET5084f4FonOMbmTqGXOLYgsPkrPKPVQiBrmShIwUijokWGOHLs8J_uK_7MfApXhbFQkJjbBDxKpM5eY4z350XbTAH06Bt7th_HxgTos3oo_n1CyzGAldRzdgr8tyHvgZC99gKm1gh9x550gXdpTUsO8Wpte2xJDpvkw2WqlK5T1i8kcMfVV9HMQNnKwxUlNw0MEzGO-d91RhkZ8c6LZafNWLzJ71lD5Gp-xBBSrD57a4V6_V3DkbaLi014U3vyumdPa3m0wAAAAF2UYSPAA"))  # enter your session string here
    LOGGER_ID = int(getenv("LOGGER_ID", "-1002161817790"))            # make a channel and get its ID
    OWNER_ID = getenv("OWNER_ID", "6641988750"))                 # enter your id here

    # optional config variables
    BLACK_IMG = getenv("BLACK_IMG", "https://graph.org/file/982ec4ada80588eb9de3d.jpg")        # black image for progress
    BOT_NAME = getenv("BOT_NAME", "\x40\x4d\x75\x73\x69\x63\x5f\x48\x65\x6c\x6c\x42\x6f\x74")   # dont put fancy texts here.
    BOT_PIC = getenv("BOT_PIC", "https://graph.org/file/d6b17ce95885fbcf08c93.jpg")           # put direct link to image here
    LEADERBOARD_TIME = getenv("LEADERBOARD_TIME", "3:00")   # time in 24hr format for leaderboard broadcast
    LYRICS_API = getenv("LYRICS_API", None)             # from https://docs.genius.com/
    MAX_FAVORITES = int(getenv("MAX_FAVORITES", 30))    # max number of favorite tracks
    PLAY_LIMIT = int(getenv("PLAY_LIMIT", 0))           # time in minutes. 0 for no limit
    PRIVATE_MODE = getenv("PRIVATE_MODE", "off")        # "on" or "off" to enable/disable private mode
    SONG_LIMIT = int(getenv("SONG_LIMIT", 0))           # time in minutes. 0 for no limit
    TELEGRAM_IMG = getenv("TELEGRAM_IMG", None)         # put direct link to image here
    TG_AUDIO_SIZE_LIMIT = int(getenv("TG_AUDIO_SIZE_LIMIT", 104857600))     # size in bytes. 0 for no limit
    TG_VIDEO_SIZE_LIMIT = int(getenv("TG_VIDEO_SIZE_LIMIT", 1073741824))    # size in bytes. 0 for no limit
    TZ = getenv("TZ", "Asia/Kolkata")   # https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

    # do not edit these variables
    BANNED_USERS = filters.user()
    CACHE = {}
    CACHE_DIR = "./cache/"
    DELETE_DICT = {}
    DWL_DIR = "./downloads/"
    GOD_USERS = filters.user()
    PLAYER_CACHE = {}
    QUEUE_CACHE =  {}
    SONG_CACHE = {}
    SUDO_USERS = filters.user()


# get all config variables in a list
all_vars = [i for i in Config.__dict__.keys() if not i.startswith("__")]
