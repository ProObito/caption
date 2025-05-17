from pyrogram import Client, filters, enums 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserNotParticipant
from info import *
from .database import insert

async def not_subscribed(_, client, message):
    user_id = int(message.from_user.id)
    await insert(user_id)
    if not FORCE_SUB:
        return False
    try:             
        user = await client.get_chat_member(FORCE_SUB, message.from_user.id) 
        if user.status == enums.ChatMemberStatus.BANNED:
            return True 
        else:
            return False                
    except UserNotParticipant:
        pass
    return True


@Client.on_message(filters.private & filters.create(not_subscribed))
async def forces_sub(client, message):
    buttons = [[InlineKeyboardButton(text="ᴄᴏᴅᴇғʟɪx", url=f"https://t.me/{FORCE_SUB}") ]]
    text = "<blockquote>ʙᴀᴋᴋᴀ!!, ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴊᴏɪɴᴇᴅ ᴛᴏ ᴀʟʟ ʀᴇǫᴜɪʀᴇᴅ ᴄʜᴀɴɴᴇʟs, ᴊᴏɪɴ ᴛʜᴇ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟs ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ</blockquote>"
    try:
        silicon = await client.get_chat_member(FORCE_SUB, message.from_user.id)    
        if silicon.status == enums.ChatMemberStatus.BANNED:                                   
            return await client.send_message(message.from_user.id, text="Sᴏʀʀy Yᴏᴜ'ʀᴇ Bᴀɴɴᴇᴅ Tᴏ Uꜱᴇ Mᴇ")  
    except UserNotParticipant:                       
        return await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
    return await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
          
