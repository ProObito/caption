from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserNotParticipant, PeerIdInvalid
from info import FORCE_SUB_1, FORCE_SUB_2
from .database import insert
import logging

logger = logging.getLogger(__name__)

async def not_subscribed(_, client: Client, message):
    user_id = int(message.from_user.id)
    await insert(user_id)  # Save user ID to database
    if not (FORCE_SUB_1 and FORCE_SUB_2):
        return False  # Proceed if no force sub channels
    not_joined = []
    try:
        # Check first channel
        try:
            user = await client.get_chat_member(FORCE_SUB_1, user_id)
            if user.status == enums.ChatMemberStatus.BANNED:
                return True  # Banned users can't proceed
        except UserNotParticipant:
            not_joined.append(FORCE_SUB_1)
        except PeerIdInvalid:
            logger.error(f"Invalid channel ID: {FORCE_SUB_1}")
            not_joined.append(FORCE_SUB_1)  # Treat as not joined
        # Check second channel
        try:
            user = await client.get_chat_member(FORCE_SUB_2, user_id)
            if user.status == enums.ChatMemberStatus.BANNED:
                return True
        except UserNotParticipant:
            not_joined.append(FORCE_SUB_2)
        except PeerIdInvalid:
            logger.error(f"Invalid channel ID: {FORCE_SUB_2}")
            not_joined.append(FORCE_SUB_2)
        return bool(not_joined)  # True if not joined any channel
    except Exception as e:
        logger.error(f"Error checking subscription: {str(e)}")
        return True  # Block on other errors

@Client.on_message(filters.private & filters.create(not_subscribed))
async def forces_sub(client: Client, message):
    user_id = message.from_user.id
    buttons = []
    not_joined = []
    banned = False
    # Check first channel
    try:
        user = await client.get_chat_member(FORCE_SUB_1, user_id)
        if user.status == enums.ChatMemberStatus.BANNED:
            banned = True
    except UserNotParticipant:
        not_joined.append(FORCE_SUB_1)
    except PeerIdInvalid:
        logger.error(f"Invalid channel ID: {FORCE_SUB_1}")
        not_joined.append(FORCE_SUB_1)
    # Check second channel
    try:
        user = await client.get_chat_member(FORCE_SUB_2, user_id)
        if user.status == enums.ChatMemberStatus.BANNED:
            banned = True
    except UserNotParticipant:
        not_joined.append(FORCE_SUB_2)
    except PeerIdInvalid:
        logger.error(f"Invalid channel ID: {FORCE_SUB_2}")
        not_joined.append(FORCE_SUB_2)
    # Handle banned case
    if banned:
        return await client.send_message(
            user_id,
            text="<b>Sᴏʀʀy, Yᴏᴜ'ʀᴇ Bᴀɴɴᴇᴅ Tᴏ Uꜱᴇ Mᴇ</b>",
            parse_mode=enums.ParseMode.HTML
        )
    # Build buttons for not joined channels
    for channel in not_joined:
        channel_handle = channel.lstrip("")  # Convert ID to handle format
        buttons.append([
            InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/CodeFlix_Bots")
        ])
    if not buttons:  # Fallback if something goes wrong
        buttons = [
            [InlineKeyboardButton(text="ᴄᴏᴅᴇғʟɪx", url="https://t.me/CodeFlix_Bots")],
            [InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url="https://t.me/CodeflixSupport")]
        ]
    text = "<blockquote>ʙᴀᴋᴋᴀ!!, ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴊᴏɪɴᴇᴅ ᴛᴏ  ᴀʟʟ ʀᴇǫᴜɪʀᴇᴅ ᴄʜᴀɴɴᴇʟs, ᴊᴏɪɴ ᴛʜᴇ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟs ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ</blockquote>"
    return await message.reply_text(
        text=text,
        reply_markup=InlineKeyboardMarkup(buttons),
        parse_mode=enums.ParseMode.HTML
    )
