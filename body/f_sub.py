from pyrogram import Client, filters, enums 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserNotParticipant, PeerIdInvalid
from info import *
from .database import insert

async def not_subscribed(_, client, message):
    user_id = int(message.from_user.id)
    await insert(user_id)
    if not (FORCE_SUB_1 or FORCE_SUB_2):
        return False
    try:
        user1 = await client.get_chat_member(FORCE_SUB_1, user_id)
        user2 = await client.get_chat_member(FORCE_SUB_2, user_id) if FORCE_SUB_2 else None
        if user1.status == enums.ChatMemberStatus.BANNED or (user2 and user2.status == enums.ChatMemberStatus.BANNED):
            return True
        return False
    except UserNotParticipant:
        return True
    except PeerIdInvalid:
        await message.reply_text(
            "<b>Invalid channel ID or bot not in channel. Contact the admin.</b>",
            parse_mode=enums.ParseMode.HTML
        )
        return True
    except Exception as e:
        await message.reply_text(
            f"<b>Error: {html.escape(str(e))}</b>",
            parse_mode=enums.ParseMode.HTML
        )
        return True

@Client.on_message(filters.private & filters.create(not_subscribed))
async def forces_sub(client, message):
    buttons = [
        [InlineKeyboardButton("• ᴄᴏᴅᴇғʟɪx ʙᴏᴛs •", url=f"https://t.me/CodeFlix_Bots")]
    ]
    if FORCE_SUB_2:
        buttons.append([InlineKeyboardButton("• ᴏᴛʜᴇʀ ᴄʜᴀɴɴᴇʟ •", url=f"https://t.me/{FORCE_SUB_2.lstrip('-100')}")])
    text = "<b>Oiii ʙᴀᴋᴋᴀ!!, ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴊᴏɪɴᴇᴅ ᴛᴏ ᴀʟʟ ʀᴇǫᴜɪʀᴇᴅ ᴄʜᴀɴɴᴇʟs, ᴊᴏɪɴ ᴛʜᴇ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟs ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ</b>"
    try:
        user1 = await client.get_chat_member(FORCE_SUB_1, message.from_user.id)
        if user1.status == enums.ChatMemberStatus.BANNED:
            return await client.send_message(
                message.from_user.id,
                text="<b>Sᴏʀʀy Yᴏᴜ'ʀᴇ Bᴀɴɴᴇᴅ Tᴏ Uꜱᴇ Mᴇ</b>",
                parse_mode=enums.ParseMode.HTML
            )
        if FORCE_SUB_2:
            user2 = await client.get_chat_member(FORCE_SUB_2, message.from_user.id)
            if user2.status == enums.ChatMemberStatus.BANNED:
                return await client.send_message(
                    message.from_user.id,
                    text="<b>Sᴏʀʀy Yᴏᴜ'ʀᴇ Bᴀɴɴᴇᴅ Tᴏ Uꜱᴇ Mᴇ</b>",
                    parse_mode=enums.ParseMode.HTML
                )
    except UserNotParticipant:
        return await message.reply_text(
            text=text,
            reply_markup=InlineKeyboardMarkup(buttons),
            parse_mode=enums.ParseMode.HTML
        )
    except PeerIdInvalid:
        return await message.reply_text(
            "<b>Invalid channel ID or bot not in channel. Contact the admin.</b>",
            parse_mode=enums.ParseMode.HTML
        )
    except Exception as e:
        return await message.reply_text(
            f"<b>Error: {html.escape(str(e))}</b>",
            parse_mode=enums.ParseMode.HTML
        )
