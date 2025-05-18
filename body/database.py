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

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

VALID_FONT_STYLES = ["BOLD", "ITALIC", "UNDERLINE", "STRIKETHROUGH", "MONOSPACE", "SPOILER", "BLOCKQUOTE", "NONE"]

def format_caption(text: str, font_style: str) -> tuple[str, str]:
    text = html.escape(text)
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
async def strtCap(bot, message):
    user_id = int(message.from_user.id)
    await insert(user_id)
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("• ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ •", url=f"http://t.me/Tessia_Caption_Bot?startchannel=true")],
            [InlineKeyboardButton("• ᴜᴘᴅᴀᴛᴇ", url=f"https://t.me/CodeFlix_Bots"),
             InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ •", url=f"https://t.me/CodeflixSupport")],
            [InlineKeyboardButton("• ᴀʙᴏᴜᴛ", callback_data="about"),
             InlineKeyboardButton("ᴄᴀᴍᴍᴀɴᴅ •", callback_data="help"),
             InlineKeyboardButton("• ғᴏɴᴛ •", callback_data="font")]
        ]
    )
    try:
        if SILICON_PIC and SILICON_PIC.endswith(('.gif', '.mp4')):
            await message.reply_animation(
                animation=SILICON_PIC,
                caption=script.START_TXT.format(html.escape(message.from_user.mention)),
                parse_mode=enums.ParseMode.HTML,
                reply_markup=keyboard
            )
        else:
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
async def all_db_users_here(client, message):
    silicon = await message.reply_text("<b>Please Wait...</b>", parse_mode=enums.ParseMode.HTML)
    silicon_botz = await total_user()
    await silicon.edit(f"<b>Tᴏᴛᴀʟ Usᴇʀ :- <code>{silicon_botz}</code></b>", parse_mode=enums.ParseMode.HTML)

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["broadcast"]))
async def broadcast(bot, message):
    if message.reply_to_message:
        silicon = await message.reply_text("<b>Getting All IDs from database...<br>Please wait</b>", parse_mode=enums.ParseMode.HTML)
        all_users = await getid()
        tot = await total_user()
        success = 0
        failed = 0
        deactivated = 0
        blocked = 0
        await silicon.edit(f"<b>ʙʀᴏᴀᴅᴄᴀsᴛɪɴɢ...</b>", parse_mode=enums.ParseMode.HTML)
        async for user in all_users:
            try:
                await message.reply_to_message.copy(user['_id'])
                success += 1
            except FloodWait as e:
                await asyncio.sleep(e.value)
                continue
            except Exception as e:
                if "USER_IS_BLOCKED" in str(e):
                    blocked += 1
                elif "USER_ID_INVALID" in str(e) or "USER_IS_DEACTIVATED" in str(e):
                    deactivated += 1
                else:
                    failed += 1
                await delete({"_id": user['_id']})
            try:
                await silicon.edit(
                    f"<b><u>ʙʀᴏᴀᴅᴄᴀsᴛ ᴘʀᴏᴄᴇssɪɴɢ</u><br><br>• ᴛᴏᴛᴀʟ ᴜsᴇʀs: {tot}<br>• sᴜᴄᴄᴇssғᴜʟ: {success}<br>• ʙʟᴏᴄᴋᴇᴅ ᴜsᴇʀs: {blocked}<br>• ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs: {deactivated}<br>• ᴜɴsᴜᴄᴄᴇssғᴜʟ: {failed}</b>",
                    parse_mode=enums.ParseMode.HTML
                )
            except FloodWait as e:
                await asyncio.sleep(e.value)
        await silicon.edit(
            f"<b><u>ʙʀᴏᴀᴅᴄᴀsᴛ ᴄᴏᴍᴘʟᴇᴛᴇᴅ</u><br><br>• ᴛᴏᴛᴀʟ ᴜsᴇʀs: {tot}<br>• sᴜᴄᴄᴇssғᴜʟ: {success}<br>• ʙʟᴏᴄᴋᴇᴅ ᴜsᴇʀs: {blocked}<br>• ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs: {deactivated}<br>• ᴜɴsᴜᴄᴄᴇssғᴜʟ: {failed}</b>",
            parse_mode=enums.ParseMode.HTML
        )

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command("restart"))
async def restart_bot(b, m):
    silicon = await b.send_message(
        text="<b>𝙿𝚁𝙾𝙲𝙴𝚂𝚂𝙴𝚂 𝚂𝚃𝙾𝙿𝙴𝙳. 𝙱𝙾𝚃 𝙸𝚂 𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙸𝙽𝙶...</b>",
        chat_id=m.chat.id,
        parse_mode=enums.ParseMode.HTML
    )       
    await asyncio.sleep(3)
    await silicon.edit("<b>𝙱𝙾𝚃 𝙸𝚂 𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙴𝙳. 𝙽𝙾𝚆 𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝙼𝙴</b>", parse_mode=enums.ParseMode.HTML)
    os.execl(sys.executable, sys.executable, *sys.argv)

@Client.on_message(filters.command("set_cap") & filters.channel)
async def setCap(bot, message):
    if len(message.command) < 2:
        return await message.reply(
            "<b>Usage: <code>/set_cap Your caption</code><br><br>Use <code>{file_name}</code> to show file name.<br>Use <code>{file_size}</code> to show file size.<br><br>✓ Now you are clear 💫</b>",
            parse_mode=enums.ParseMode.HTML
        )
    chnl_id = message.chat.id
    caption = message.text.split(" ", 1)[1] if len(message.text.split(" ", 1)) > 1 else None
    chkData = await chnl_ids.find_one({"chnl_id": chnl_id})
    if chkData:
        await updateCap(chnl_id, caption)
        return await message.reply(
            f"<b>Your New Caption: <code>{html.escape(caption)}</code></b>",
            parse_mode=enums.ParseMode.HTML
        )
    else:
        await addCap(chnl_id, caption)
        return await message.reply(
            f"<b>Your New Caption Is: <code>{html.escape(caption)}</code></b>",
            parse_mode=enums.ParseMode.HTML
        )

@Client.on_message(filters.command("set_font") & filters.channel)
async def setFont(bot, message):
    if len(message.command) < 2:
        return await message.reply(
            f"<b>Usage: <code>/set_font STYLE</code><br><br>Available styles: {', '.join(VALID_FONT_STYLES)}<br><br>Example: /set_font BLOCKQUOTE</b>",
            parse_mode=enums.ParseMode.HTML
        )
    chnl_id = message.chat.id
    font_style = message.command[1].upper()
    if font_style not in VALID_FONT_STYLES:
        return await message.reply(
            f"<b>Invalid font style! Choose from: {', '.join(VALID_FONT_STYLES)}</b>",
            parse_mode=enums.ParseMode.HTML
        )
    chkData = await chnl_ids.find_one({"chnl_id": chnl_id})
    if not chkData:
        return await message.reply(
            "<b>No caption set for this channel. Use /set_cap first.</b>",
            parse_mode=enums.ParseMode.HTML
        )
    await updateFontStyle(chnl_id, font_style)
    await message.reply(
        f"<b>Font style set to: <code>{font_style}</code></b>",
        parse_mode=enums.ParseMode.HTML
    )

@Client.on_message(filters.command("font") & filters.private)
async def font_cmd(bot, message):
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("BOLD", callback_data="font_BOLD"),
             InlineKeyboardButton("ITALIC", callback_data="font_ITALIC")],
            [InlineKeyboardButton("UNDERLINE", callback_data="font_UNDERLINE"),
             InlineKeyboardButton("STRIKETHROUGH", callback_data="font_STRIKETHROUGH")],
            [InlineKeyboardButton("MONOSPACE", callback_data="font_MONOSPACE"),
             InlineKeyboardButton("SPOILER", callback_data="font_SPOILER")],
            [InlineKeyboardButton("BLOCKQUOTE", callback_data="font_BLOCKQUOTE"),
             InlineKeyboardButton("NONE", callback_data="font_NONE")],
            [InlineKeyboardButton("• ʙᴀᴄᴋ •", callback_data="start")]
        ]
    )
    await message.reply_text(
        "<b>Select a font style:</b>",
        reply_markup=keyboard,
        parse_mode=enums.ParseMode.HTML
    )

@Client.on_message(filters.command("del_cap") & filters.channel)
async def delCap(_, msg):
    chnl_id = msg.chat.id
    try:
        await chnl_ids.delete_one({"chnl_id": chnl_id})
        return await msg.reply(
            "<b><i>✓ Successfully Deleted Your Caption. Now I am Using My Default Caption</i></b>",
            parse_mode=enums.ParseMode.HTML
        )
    except Exception as e:
        e_val = await msg.reply(
            f"<b>Error: <code>{html.escape(str(e))}</code></b>",
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
async def reCap(bot, message):
    chnl_id = message.chat.id
    default_caption = message.caption or ""
    if message.media:
        for file_type in ("video", "audio", "document", "voice"):
            obj = getattr(message, file_type, None)
            if obj and hasattr(obj, "file_name"):
                file_name = obj.file_name
                file_size = obj.file_size
                language = extract_language(default_caption)
                year = extract_year(default_caption)
                file_name = re.sub(r"@\w+\s*", "", file_name).replace("_", " ").replace(".", " ")
                cap_dets = await chnl_ids.find_one({"chnl_id": chnl_id})
                try:
                    if cap_dets:
                        cap = cap_dets["caption"]
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
                    continue

def get_size(size):
    units = ["Bytes", "Kʙ", "Mʙ", "Gʙ", "Tʙ", "Pʙ", "Eʙ"]
    size = float(size)
    i = 0
    while size >= 1024.0 and i < len(units) - 1:
        i += 1
        size /= 1024.0
    return "%.2f %s" % (size, units[i])

@Client.on_callback_query(filters.regex(r'^start'))
async def start(bot, query):
    try:
        await query.message.edit_text(
            text=script.START_TXT.format(html.escape(query.from_user.mention)),
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("• ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ •", url=f"http://t.me/Tessia_Caption_Bot?startchannel=true")],
                    [InlineKeyboardButton("• ᴜᴘᴅᴀᴛᴇ", url=f"https://t.me/CodeFlix_Bots"),
                     InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ •", url=f"https://t.me/CodeflixSupport")],
                    [InlineKeyboardButton("• ᴀʙᴏᴜᴛ", callback_data="about"),
                     InlineKeyboardButton("ᴄᴀᴍᴍᴀɴᴅ •", callback_data="help"),
                     InlineKeyboardButton("• ғᴏɴᴛ •", callback_data="font")]
                ]
            ),
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("Start menu displayed")
    except Exception as e:
        logger.error(f"Error in start callback: {str(e)}")
        await query.message.reply_text("<b>An error occurred. Please try again.</b>", parse_mode=enums.ParseMode.HTML)

@Client.on_callback_query(filters.regex(r'^help'))
async def help(bot, query):
    try:
        await query.message.edit_text(
            text=script.HELP_TXT,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton('• ᴀʙᴏᴜᴛ •', callback_data='about'),
                     InlineKeyboardButton('• ғᴏɴᴛ •', callback_data='font')],
                    [InlineKeyboardButton('• ʙᴀᴄᴋ •', callback_data='start')]
                ]
            ),
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("Help menu displayed")
    except Exception as e:
        logger.error(f"Error in help callback: {str(e)}")
        await query.message.reply_text("<b>Failed to display help. Please try again.</b>", parse_mode=enums.ParseMode.HTML)
        await query.answer("Error occurred")

@Client.on_callback_query(filters.regex(r'^about'))
async def about(bot, query):
    try:
        await query.message.edit_text(
            text=script.ABOUT_TXT,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton('• ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ •', callback_data='help'),
                     InlineKeyboardButton('• ғᴏɴᴛ •', callback_data='font')],
                    [InlineKeyboardButton('• ʙᴀᴄᴋ •', callback_data='start')]
                ]
            ),
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("About menu displayed")
    except Exception as e:
        logger.error(f"Error in about callback: {str(e)}")
        await query.message.reply_text("<b>Failed to display about. Please try again.</b>", parse_mode=enums.ParseMode.HTML)
        await query.answer("Error occurred")

@Client.on_callback_query(filters.regex(r'^font'))
async def font_callback(bot, query):
    try:
        await query.message.edit_text(
            text=f"<b>Select a font style:</b><br><br>Available styles: {', '.join(VALID_FONT_STYLES)}",
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("BOLD", callback_data="font_BOLD"),
                     InlineKeyboardButton("ITALIC", callback_data="font_ITALIC")],
                    [InlineKeyboardButton("UNDERLINE", callback_data="font_UNDERLINE"),
                     InlineKeyboardButton("STRIKETHROUGH", callback_data="font_STRIKETHROUGH")],
                    [InlineKeyboardButton("MONOSPACE", callback_data="font_MONOSPACE"),
                     InlineKeyboardButton("SPOILER", callback_data="font_SPOILER")],
                    [InlineKeyboardButton("BLOCKQUOTE", callback_data="font_BLOCKQUOTE"),
                     InlineKeyboardButton("NONE", callback_data="font_NONE")],
                    [InlineKeyboardButton("• ʙᴀᴄᴋ •", callback_data="start")]
                ]
            ),
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("Font menu displayed")
    except Exception as e:
        logger.error(f"Error in font callback: {str(e)}")
        await query.message.reply_text("<b>Failed to display font menu. Please try again.</b>", parse_mode=enums.ParseMode.HTML)
        await query.answer("Error occurred")

@Client.on_callback_query(filters.regex(r'^font_([A-Z]+)$'))
async def set_font_callback(bot, query):
    font_style = query.matches[0].group(1)
    if font_style not in VALID_FONT_STYLES:
        await query.message.reply_text(
            f"<b>Invalid font style! Choose from: {', '.join(VALID_FONT_STYLES)}</b>",
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("Invalid font style")
        return
    chnl_id = query.message.chat.id
    chkData = await chnl_ids.find_one({"chnl_id": chnl_id})
    if not chkData:
        await query.message.reply_text(
            "<b>No caption set for this channel. Use /set_cap first.</b>",
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("No caption set")
        return
    await updateFontStyle(chnl_id, font_style)
    await query.message.edit_text(
        f"<b>Font style set to: <code>{font_style}</code></b>",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("• ʙᴀᴄᴋ •", callback_data="start")]]),
        parse_mode=enums.ParseMode.HTML
    )
    await query.answer(f"Font style set to {font_style}")
