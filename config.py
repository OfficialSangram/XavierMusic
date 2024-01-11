import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "「ʀᴇᴅ ᴡɪɴᴇ ᴍᴜsɪᴄ 」")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 10000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", None))

# Support chat id
SUPPORT_CHAT_ID = int(getenv("SUPPORT_CHAT_ID"))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", 6485380150))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/OfficialSangram/XavierMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/AvengerNews")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Red_Wine_Op")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
LOG = 2
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/8140f99138925e2741313.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/7fd3c67bca3f72ab70edd.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/748b10cdb7e21b5dae44b.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/cb512c35937ab7c5aedc5.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/134923b0408d4a08f35b8.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/134923b0408d4a08f35b8.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/24d268b14b19f9832e70a.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/581bd40bf7d495d2353f4.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/62b72a1bea8deae9a59fb.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/2de154a22f5b66e594a77.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/008030ab5784f6ce8ae43.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/008030ab5784f6ce8ae43.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
