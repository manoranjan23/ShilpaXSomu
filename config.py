import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "28588693"))
API_HASH = getenv("API_HASH", "fac94f1f1aa4aa395280a670ddf9c0f2")
BOT_PRIVACY = getenv("BOT_PRIVACY", "https://telegra.ph/Privacy-Policy-for-AnieXEricaMusic-10-06")
BOT_TOKEN = getenv("BOT_TOKEN", "8124266415:AAEBEFp6GMZ-FSBaqNFFKvHzCc4tCZKN3Xs")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Ishuxd:ishusomuxd@ishuxd.78ljc.mongodb.net/?retryWrites=true&w=majority&appName=Ishuxd")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 600))

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID",-1002100433415))

OWNER_ID = int(getenv("OWNER_ID", 7070591202))

OWNER = int(getenv("OWNER", 7070591202))

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

HEROKU_API_KEY = getenv("HEROKU_API_KEY","HK543fklqxgt66hvxf")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/manoranjan23/ShilpaXSomu",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/somueditingzone")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/somueditingzone")
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "2a230af10e0a40638dc77c1febb47170")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "7f92897a59464ddbbf00f06cd6bda7fc")
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 5242880000))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 5242880000))

STRING1 = getenv("STRING_SESSION", "BQGuuesAcXAFZzpr0TzAgJOXg39sslAINNpUb06vfqZhUUvUqikn8_1q4in52UbHMM_lIW3foXNu6NuGLpipZLsfm1CGfpsy--0JV7DoJOy8C-dKGgzKkg2aA4VSDwSx-dYLv0EaaFM5etjr7yQNLLTg71-07gg5AtaPaSl1Y04thVEdNTSboP4iANZBu0nm4RoCXMkkf8t9DkJldpCPTwtD39EXtcR7a8PqIF10NyRALZlygfMGRXrWa63Q1eW-rDgmGabeu6KDsmlSHnrXH8bJShNRElxFFjl0j0r9IlfDaQPO8jRyn52-fVGzAm9azz5e2bYLewpiad02Q3m8IvxJkvuq4wAAAAHUG3e7AA")
STRING2 = getenv("STRING_SESSION2", "")
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv("START_IMG_URL", "https://envs.sh/YZY.mp4")
PING_IMG_URL = getenv("PING_IMG_URL", "https://envs.sh/JZ4.jpg")
PLAYLIST_IMG_URL = "https://envs.sh/7wj.jpg"
STATS_IMG_URL = getenv("STATS_IMG_URL", "https://envs.sh/A32.jpg")
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://envs.sh/A32.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://envs.sh/A3u.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
