from os import environ, getenv
import re
import os

id_pattern = re.compile(r"^.\d+$")


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


ADMIN = int(getenv("ADMIN", "5585016974"))
SILICON_PIC = os.environ.get("SILICON_PIC", "https://telegra.ph/file/21a8e96b45cd6ac4d3da6.jpg")
API_ID = int(getenv("API_ID", "20718334"))
API_HASH = str(getenv("API_HASH", "4e81464b29d79c58d0ad8a0c55ece4a5"))
BOT_TOKEN = str(getenv("BOT_TOKEN", "7976984538:AAGLp9tX4gD3oepR40KtD6ANwYH-Hy6GPOY"))
FORCE_SUB_1 = "-1001234567890"  # First channel ID (update with valid ID)
FORCE_SUB_2 = "-1002078429106"  # Second channel ID (update with valid ID)
FORCE_SUB = os.environ.get("FORCE_SUB", "") 
MONGO_DB = str(getenv("MONGO_DB", "mongodb+srv://spxsolo:umaid2008@cluster0.7fbux.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"))
START_GIF = "CAACAgUAAxkBAAEFBAVoH4qTFGwjwrCkLJPeM0HjglJpYgACXAgAArSfGVXK3kCuYAiK2B4E"  # Replace with your GIF/video file_id or URL
START_REACTION = "🔥"  # Reaction emoji for /start message
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002078429106"))  # Log channel ID
DEF_CAP = str(
    getenv(
        "DEF_CAP",
        "<b>File Name:- `{file_name}`\n\n{file_size}</b>",
    )
)
