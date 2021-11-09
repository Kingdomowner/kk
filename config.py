import os
from os import getenv
from dotenv import load_dotenv
from helpers.uptools import fetch_heroku_git_url

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQAexEbU2HvQAru_UaXBprUB7lA8qHBoFakXzz5pCAihc010QNlQk8UwZgJaTHnzn8SP3rsvJ41i0X7E5yJHkR2YnVNpdw7usLj2-M7eZcTI8wLIk_x05cHsQgpP7SelA28Sp5z2KL8e1FGYwcwUOknVqL6TTBDYKeWGKC2Q8u4NQdJQMEC1x4T6eQaOFYOPHJ4YKugzlkPIJi31eOTs25MiYMc1e6NuN9fK6Wht2qx6KcVOutUcvUi5ZgqOQqRZPXCGRPQihujnBLCZVyhLCXNh-WsSgv8Nj7vK1X2lVCOW2njzrGmmlR04oYbCNgXH2zELiV3csbjnNcXsRp13r02hVmdKvwA")
BOT_TOKEN = getenv("BOT_TOKEN","1978000206:AAH8RZdfyTz4iefS978gUIaespDFLWsNJ8Q")
BOT_NAME = getenv("BOT_NAME", "Kingdom family group help bot")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/8628c642a266a22effd8c.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/4c39fbb88932761913fff.png")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/73e10ed6e2bd32b478de6.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/b95c13eef1ebd14dbb458.png")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
API_ID = int(getenv("API_ID","7635212"))
API_HASH = getenv("API_HASH","d2ff99e45bef6b7f94628277f888a644")
BOT_USERNAME = getenv("BOT_USERNAME", "kingdom_of_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "kingdom_of_bot_assistant")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "kingdom_family")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "kingdom_family_chanel")
# isi dengan username kamu tanpa simbol @
OWNER_NAME = getenv("OWNER_NAME", "kingdom_owner")
# fill with your nickname
ALIVE_NAME = getenv("ALIVE_NAME", "Levina")
# fill with your id as the owner of the bot
OWNER_ID = int(os.environ.get("OWNER_ID","1985638127"))
DATABASE_URL = os.environ.get("DATABASE_URL","mongodb://mongo:PrgDvhMqPXtPP83a6X4c@containers-us-west-10.railway.app:5881")  # fill with your mongodb url
# make a private channel and get the channel id
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
# just fill with True or False (optional)
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS","1985638127").split()))
# UPDATER CONFIG
U_BRANCH = "main"
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
UPSTREAM_REPO = os.environ.get(
    "UPSTREAM_REPO", "https://github.com/levina-lab/VeezMusic"
)
HEROKU_URL = fetch_heroku_git_url(HEROKU_API_KEY, HEROKU_APP_NAME)
