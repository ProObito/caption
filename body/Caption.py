from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait
from info import *
import asyncio
from Script import script
from .database import *
import re
import os
import sys
import html
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Supported font styles
VALID_FONT_STYLES = ["BOLD", "ITALIC", "UNDERLINE", "STRIKETHROUGH", "MONOSPACE", "SPOILER", "BLOCKQUOTE", "NONE"]

def format_caption(text: str, font_style: str) -> tuple[str, str]:
    """
    Format the caption text with the specified font style.
    Returns (formatted_text, parse_mode).
    """
    if not text:
        return "", None
        
    text = html.escape(text)
    font_style = font_style.upper() if font_style else "NONE"
    
    if font_style == "BOLD":
        return f"<b>{text}</b>", enums.ParseMode.HTML
    elif font_style == "ITALIC":
        return f"<i>{text}</i>", enums.ParseMode.HTML
    elif font_style == "UNDERLINE":
        return f"<u>{text}</u>", enums.ParseMode.HTML
    elif font_style == "STRIKETHROUGH":
        return f"<s>{text}</s>", enums.ParseMode.HTML
    elif font_style == "MONOSPACE":
        return f"<code>{text}</code>", enums.ParseMode.HTML
    elif font_style == "SPOILER":
        return f"<spoiler>{text}</spoiler>", enums.ParseMode.HTML
    elif font_style == "BLOCKQUOTE":
        return f"<blockquote>{text}</blockquote>", enums.ParseMode.HTML
    else:
        return text, None

@Client.on_message(filters.command("start") & filters.private)
async def start_command(bot, message):
    try:
        user_id = int(message.from_user.id)
        await insert(user_id)
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ •", url=f"http://t.me/Tessia_Caption_Bot?startchannel=true")
                ],[
                    InlineKeyboardButton("• ᴜᴘᴅᴀᴛᴇ", url=f"https://t.me/CodeFlix_Bots"),
                    InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ •", url=f"https://t.me/CodeflixSupport")
                ],[
                    InlineKeyboardButton("• ᴀʙᴏᴜᴛ", callback_data="about"),
                    InlineKeyboardButton("ᴄᴏᴍᴍᴀɴᴅ •", callback_data="help")
                ]
            ]
        )
        await message.reply_photo(
            photo=SILICON_PIC,
            caption=script.START_TXT.format(html.escape(message.from_user.mention)),
            parse_mode=enums.ParseMode.HTML,
            reply_markup=keyboard
        )
    except Exception as e:
        logger.error(f"Error in /start: {str(e)}")
        await message.reply_text("<b>An error occurred. Please try again.</b>", parse_mode=enums.ParseMode.HTML)

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["total_users"]))
async def total_users_command(client, message):
    try:
        silicon = await message.reply_text("<blockquote>Please Wait....</blockquote>", parse_mode=enums.ParseMode.HTML)
        silicon_botz = await total_user()
        await silicon.edit(f"<blockquote>Tᴏᴛᴀʟ Usᴇʀ :- `{silicon_botz}`</blockquote>", parse_mode=enums.ParseMode.HTML)
    except Exception as e:
        logger.error(f"Error in /total_users: {str(e)}")
        await message.reply_text("<b>An error occurred while fetching user count.</b>", parse_mode=enums.ParseMode.HTML)

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["broadcast"]))
async def broadcast_command(bot, message):
    if not message.reply_to_message:
        return await message.reply_text("<b>Please reply to a message to broadcast.</b>", parse_mode=enums.ParseMode.HTML)
        
    try:
        silicon = await message.reply_text("<blockquote>Getting All ids from database..\n Please wait</blockquote>", parse_mode=enums.ParseMode.HTML)
        all_users = await getid()
        tot = await total_user()
        success = 0
        failed = 0
        deactivated = 0
        blocked = 0
        
        await silicon.edit(f"<blockquote>ʙʀᴏᴀᴅᴄᴀsᴛɪɴɢ...</blockquote>", parse_mode=enums.ParseMode.HTML)
        
        for user in all_users:
            try:
                await message.reply_to_message.copy(user['_id'])
                success += 1
            except FloodWait as e:
                await asyncio.sleep(e.value)
                await message.reply_to_message.copy(user['_id'])
                success += 1
            except Exception as e:
                if "USER_IS_BLOCKED" in str(e):
                    blocked += 1
                elif "USER_ID_INVALID" in str(e) or "USER_IS_DEACTIVATED" in str(e):
                    deactivated += 1
                else:
                    failed += 1
                await delete({"_id": user['_id']})
                
            # Update progress every 50 messages to avoid FloodWait
            if (success + failed + blocked + deactivated) % 50 == 0:
                try:
                    await silicon.edit(
                        f"<blockquote><u>ʙʀᴏᴀᴅᴄᴀsᴛ ᴘʀᴏᴄᴇssɪɴɢ</u>\n\n• ᴛᴏᴛᴀʟ ᴜsᴇʀs: {tot}\n• sᴜᴄᴄᴇssғᴜʟ: {success}\n• ʙʟᴏᴄᴋᴇᴅ ᴜsᴇʀs: {blocked}\n• ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs: {deactivated}\n• ᴜɴsᴜᴄᴄᴇssғᴜʟ: {failed}</blockquote>",
                        parse_mode=enums.ParseMode.HTML
                    )
                except FloodWait as e:
                    await asyncio.sleep(e.value)
                    
        await silicon.edit(
            f"<blockquote><u>ʙʀᴏᴀᴅᴄᴀsᴛ ᴄᴏᴍᴘʟᴇᴛᴇᴅ</u>\n\n• ᴛᴏᴛᴀʟ ᴜsᴇʀs: {tot}\n• sᴜᴄᴄᴇssғᴜʟ: {success}\n• ʙʟᴏᴄᴋᴇᴅ ᴜsᴇʀs: {blocked}\n• ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs: {deactivated}\n• ᴜɴsᴜᴄᴄᴇssғᴜʟ: {failed}</blockquote>",
            parse_mode=enums.ParseMode.HTML
        )
    except Exception as e:
        logger.error(f"Error in broadcast: {str(e)}")
        await message.reply_text("<b>An error occurred during broadcast.</b>", parse_mode=enums.ParseMode.HTML)

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command("restart"))
async def restart_bot(b, m):
    try:
        silicon = await b.send_message(
            text="<blockquote>𝙿𝚁𝙾𝙲𝙴𝚂𝚂𝙴𝚂 𝚂𝚃𝙾𝙿𝙴𝙳. 𝙱𝙾𝚃 𝙸𝚂 𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙸𝙽𝙶...</blockquote>",
            chat_id=m.chat.id,
            parse_mode=enums.ParseMode.HTML
        )       
        await asyncio.sleep(3)
        await silicon.edit("<blockquote>𝙱𝙾𝚃 𝙸𝚂 𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙴𝙳. 𝙽𝙾𝚆 𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝙼𝙴</blockquote>", parse_mode=enums.ParseMode.HTML)
        os.execl(sys.executable, sys.executable, *sys.argv)
    except Exception as e:
        logger.error(f"Error in restart: {str(e)}")
        await m.reply_text("<b>Failed to restart bot. Please try again.</b>", parse_mode=enums.ParseMode.HTML)

@Client.on_message(filters.command("set_cap") & filters.channel)
async def set_caption_command(bot, message):
    try:
        if len(message.command) < 2:
            return await message.reply(
                "<blockquote>Usᴀɢᴇ: <b>/set_cap 𝑌𝑜𝑢𝑟 𝑐𝑎𝑝𝑡𝑖𝑜𝑛</b> 𝑈𝑠𝑒 <code>{file_name}</code> 𝑇𝑜 𝑠ℎ𝑜𝑤 𝑦𝑜𝑢𝑟 𝐹𝑖𝑙𝑒 𝑁𝑎𝑚𝑒.\n\n𝑈𝑠𝑒 <code>{file_size}</code> 𝑇𝑜 𝑠ℎ𝑜𝑤 𝑦𝑜𝑢𝑟 𝐹𝑖𝑙𝑒 𝑆𝑖𝑧𝑒\n\n✓ 𝑀𝑎𝑦 𝐵𝑒 𝑁𝑜𝑤 𝑌𝑜𝑢 𝑎𝑟𝑒 𝑐𝑙𝑒𝑎𝑟💫</blockquote>",
                parse_mode=enums.ParseMode.HTML
            )
            
        chnl_id = message.chat.id
        caption = message.text.split(" ", 1)[1] if len(message.text.split(" ", 1)) > 1 else None
        
        if not caption:
            return await message.reply(
                "<blockquote>Please provide a valid caption.</blockquote>",
                parse_mode=enums.ParseMode.HTML
            )
            
        chkData = await chnl_ids.find_one({"chnl_id": chnl_id})
        if chkData:
            await updateCap(chnl_id, caption)
            return await message.reply(
                f"<blockquote>Your New Caption: {html.escape(caption)}</blockquote>",
                parse_mode=enums.ParseMode.HTML
            )
        else:
            await addCap(chnl_id, caption)
            return await message.reply(
                f"<blockquote>Yᴏᴜʀ Nᴇᴡ Cᴀᴘᴛɪᴏɴ Is: {html.escape(caption)}</blockquote>",
                parse_mode=enums.ParseMode.HTML
            )
    except Exception as e:
        logger.error(f"Error in set_cap: {str(e)}")
        await message.reply_text("<b>An error occurred while setting caption.</b>", parse_mode=enums.ParseMode.HTML)

@Client.on_message(filters.command("set_font") & filters.channel)
async def set_font_command(bot, message):
    try:
        if len(message.command) < 2:
            return await message.reply(
                f"<blockquote>Usᴀɢᴇ: <b>/set_font STYLE</b>\n\nAvailable styles: {', '.join(VALID_FONT_STYLES)}\n\nExample: /set_font BLOCKQUOTE</blockquote>",
                parse_mode=enums.ParseMode.HTML
            )
            
        chnl_id = message.chat.id
        font_style = message.command[1].upper()
        
        if font_style not in VALID_FONT_STYLES:
            return await message.reply(
                f"<blockquote>Invalid font style! Choose from: {', '.join(VALID_FONT_STYLES)}</blockquote>",
                parse_mode=enums.ParseMode.HTML
            )
            
        chkData = await chnl_ids.find_one({"chnl_id": chnl_id})
        if not chkData:
            return await message.reply(
                "<blockquote>No caption set for this channel. Use /set_cap first.</blockquote>",
                parse_mode=enums.ParseMode.HTML
            )
            
        await updateFontStyle(chnl_id, font_style)
        await message.reply(
            f"<blockquote>Font style set to: {font_style}</blockquote>",
            parse_mode=enums.ParseMode.HTML
        )
    except Exception as e:
        logger.error(f"Error in set_font: {str(e)}")
        await message.reply_text("<b>An error occurred while setting font style.</b>", parse_mode=enums.ParseMode.HTML)

@Client.on_message(filters.command("del_cap") & filters.channel)
async def delete_caption_command(_, msg):
    try:
        chnl_id = msg.chat.id
        result = await chnl_ids.delete_one({"chnl_id": chnl_id})
        
        if result.deleted_count > 0:
            await msg.reply(
                "<blockquote><b><i>✓ Sᴜᴄᴄᴇssғᴜʟʟʏ... Dᴇʟᴇᴛᴇᴅ Yᴏᴜʀ Cᴀᴘᴛɪᴏɴ Nᴏᴡ I ᴀᴍ Usɪɴɢ Mʏ Dᴇғᴀᴜʟᴛ Cᴀᴘᴛɪᴏɴ</i></b></blockquote>",
                parse_mode=enums.ParseMode.HTML
            )
        else:
            await msg.reply(
                "<blockquote>No caption found to delete for this channel.</blockquote>",
                parse_mode=enums.ParseMode.HTML
            )
    except Exception as e:
        logger.error(f"Error in del_cap: {str(e)}")
        e_val = await msg.reply(
            f"<blockquote>Error: {html.escape(str(e))}</blockquote>",
            parse_mode=enums.ParseMode.HTML
        )
        await asyncio.sleep(5)
        await e_val.delete()

def extract_language(default_caption):
    if not default_caption:
        return "Hindi-English"
    language_pattern = r'\b(Hindi|English|Tamil|Telugu|Malayalam|Kannada|Hin)\b'
    languages = set(re.findall(language_pattern, default_caption, re.IGNORECASE))
    return ", ".join(sorted(languages, key=str.lower)) if languages else "Hindi-English"

def extract_year(default_caption):
    if not default_caption:
        return None
    match = re.search(r'\b(19\d{2}|20\d{2})\b', default_caption)
    return match.group(1) if match else None

@Client.on_message(filters.channel)
async def handle_channel_message(bot, message):
    try:
        chnl_id = message.chat.id
        default_caption = message.caption or ""
        
        if not message.media:
            return
            
        file_name = ""
        file_size = 0
        
        # Get file name and size based on media type
        for file_type in ("video", "audio", "document", "voice"):
            obj = getattr(message, file_type, None)
            if obj and hasattr(obj, "file_name"):
                file_name = obj.file_name
                file_size = obj.file_size
                break
                
        if not file_name:
            return
            
        language = extract_language(default_caption)
        year = extract_year(default_caption)
        
        # Clean up file name
        file_name = re.sub(r"@\w+\s*", "", file_name).replace("_", " ").replace(".", " ")
        
        cap_dets = await chnl_ids.find_one({"chnl_id": chnl_id})
        
        try:
            if cap_dets:
                cap = cap_dets.get("caption", DEF_CAP)
                font_style = cap_dets.get("font_style", "NONE")
                
                replaced_caption = cap.format(
                    file_name=file_name,
                    file_size=get_size(file_size),
                    default_caption=default_caption,
                    language=language,
                    year=year
                )
                
                formatted_caption, parse_mode = format_caption(replaced_caption, font_style)
                await message.edit_caption(caption=formatted_caption, parse_mode=parse_mode)
            else:
                replaced_caption = DEF_CAP.format(
                    file_name=file_name,
                    file_size=get_size(file_size),
                    default_caption=default_caption,
                    language=language,
                    year=year
                )
                
                formatted_caption, parse_mode = format_caption(replaced_caption, "NONE")
                await message.edit_caption(caption=formatted_caption, parse_mode=parse_mode)
        except FloodWait as e:
            await asyncio.sleep(e.value)
        except Exception as e:
            logger.error(f"Error editing caption: {str(e)}")
    except Exception as e:
        logger.error(f"Error in channel message handler: {str(e)}")

def get_size(size):
    """Convert file size to human readable format"""
    if not size:
        return "0 Bytes"
        
    try:
        size = float(size)
    except (TypeError, ValueError):
        return "0 Bytes"
        
    units = ["Bytes", "KB", "MB", "GB", "TB", "PB", "EB"]
    i = 0
    while size >= 1024.0 and i < len(units) - 1:
        i += 1
        size /= 1024.0
    return "%.2f %s" % (size, units[i])

@Client.on_callback_query(filters.regex(r'^start$'))
async def start_callback(bot, query):
    try:
        await query.message.edit_text(
            text=script.START_TXT.format(html.escape(query.from_user.mention)),
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("• ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ •", url=f"http://t.me/Tessia_Caption_Bot?startchannel=true")
                    ],[
                        InlineKeyboardButton("• ᴜᴘᴅᴀᴛᴇ", url=f"https://t.me/CodeFlix_Bots"),
                        InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ •", url=f"https://t.me/CodeflixSupport")
                    ],[
                        InlineKeyboardButton("• ᴀʙᴏᴜᴛ", callback_data="about"),
                        InlineKeyboardButton("ᴄᴏᴍᴍᴀɴᴅ •", callback_data="help")
                    ]
                ]
            ),
            parse_mode=enums.ParseMode.HTML
        )
    except Exception as e:
        logger.error(f"Error in start callback: {str(e)}")
        await query.answer("Failed to update message", show_alert=True)

@Client.on_callback_query(filters.regex(r'^help$'))
async def help_callback(bot, query):
    try:
        await query.message.edit_text(
            text=script.HELP_TXT,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('• ᴀʙᴏᴜᴛ •', callback_data='about')
                    ],[
                        InlineKeyboardButton('• ʙᴀᴄᴋ •', callback_data='start')
                    ]
                ]
            ),
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer()
    except Exception as e:
        logger.error(f"Error in help callback: {str(e)}")
        await query.answer("Failed to show help", show_alert=True)

@Client.on_callback_query(filters.regex(r'^about$'))
async def about_callback(bot, query):
    try:
        await query.message.edit_text(
            text=script.ABOUT_TXT,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('• ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ •', callback_data='help')
                    ],[
                        InlineKeyboardButton('• ʙᴀᴄᴋ •', callback_data='start')
                    ]
                ]
            ),
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer()
    except Exception as e:
        logger.error(f"Error in about callback: {str(e)}")
        await query.answer("Failed to show about", show_alert=True)

@Client.on_callback_query(filters.regex(r'^font$'))
async def font_callback(bot, query):
    try:
        await query.message.edit_text(
            text=script.FONT_TXT,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('• ᴀʙᴏᴜᴛ •', callback_data='about')
                    ],[
                        InlineKeyboardButton('• ʙᴀᴄᴋ •', callback_data='start')
                    ]
                ]
            ),
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer()
    except Exception as e:
        logger.error(f"Error in font callback: {str(e)}")
        await query.answer("Failed to show font info", show_alert=True)
