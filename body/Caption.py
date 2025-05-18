from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait, PeerIdInvalid
from info import *
from .f_sub import not_subscribed
import asyncio
from Script import script
from .database import *
import re
import os
import sys
import html
import time
import logging
from motor.motor_asyncio import AsyncIOMotorDatabase

logger = logging.getLogger(__name__)

VALID_FONT_STYLES = ["BOLD", "ITALIC", "UNDERLINE", "STRIKETHROUGH", "MONOSPACE", "SPOILER", "BLOCKQUOTE", "SMALLCAPS", "SANS", "NONE"]

SMALLCAPS_MAP = str.maketrans({
    'a': 'ᴀ', 'b': 'ʙ', 'c': 'ᴄ', 'd': 'ᴅ', 'e': 'ᴇ', 'f': 'ғ', 'g': 'ɢ', 'h': 'ʜ', 'i': 'ɪ',
    'j': 'ᴊ', 'k': 'ᴋ', 'l': 'ʟ', 'm': 'ᴍ', 'n': 'ɴ', 'o': 'ᴏ', 'p': 'ᴘ', 'q': 'ǫ', 'r': 'ʀ',
    's': 's', 't': 'ᴛ', 'u': 'ᴜ', 'v': 'ᴠ', 'w': 'ᴡ', 'x': 'x', 'y': 'ʏ', 'z': 'ᴢ'
})

def format_caption(text: str, font_style: str) -> tuple[str, str]:
    if font_style == "SMALLCAPS":
        text = text.lower().translate(SMALLCAPS_MAP)
        return text, enums.ParseMode.HTML
    elif font_style == "SANS":
        return f"<b><i>{html.escape(text)}</i></b>", enums.ParseMode.HTML
    elif font_style == "BOLD":
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
        return text, enums.ParseMode.HTML

@Client.on_message(filters.command("start") & filters.private & ~filters.create(not_subscribed))
async def strtCap(bot, message):
    user_id = int(message.from_user.id)
    await insert(user_id)
    # Initial interactive text sequence
    m = await message.reply_text("ʜᴇʜᴇ..ɪ'ᴍ ᴀɴʏᴀ!\nᴡᴀɪᴛ ᴀ ᴍᴏᴍᴇɴᴛ. . .")
    await asyncio.sleep(0.4)
    await m.edit_text("🎊")
    await asyncio.sleep(0.5)
    await m.edit_text("⚡")
    await asyncio.sleep(0.5)
    await m.edit_text("ᴡᴀᴋᴜ ᴡᴀᴋᴜ!...")
    await asyncio.sleep(0.4)
    await m.delete()
    
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("• Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀɴɴᴇʟ •", url=f"http://t.me/Tessia_Caption_Bot?startchannel=true")
            ],[
                InlineKeyboardButton("• Uᴘᴅᴀᴛᴇs", url=f"https://t.me/CodeFlix_Bots"),
                InlineKeyboardButton("Sᴜᴘᴘᴏʀᴛ •", url=f"https://t.me/CodeflixSupport")
            ],[
                InlineKeyboardButton("• Aʙᴏᴜᴛ", callback_data="about"),
                InlineKeyboardButton("Cᴏᴍᴍᴀɴᴅs •", callback_data="help")
        ]]
    )
    try:
        # Use a placeholder or configurable animation file ID
        animation_id = START_GIF if 'CAACAgUAAxkBAAEFBAVoH4qTFGwjwrCkLJPeM0HjglJpYgACXAgAArSfGVXK3kCuYAiK2B4E' in globals() and START_GIF else None
        caption_text = script.START_TXT.format(html.escape(message.from_user.mention))
        if animation_id:
            sent_message = await bot.send_animation(
                chat_id=message.chat.id,
                animation=animation_id,
                caption=caption_text,
                parse_mode=enums.ParseMode.HTML,
                reply_markup=keyboard
            )
        else:
            # Fallback to text message if no animation ID is provided
            sent_message = await message.reply_text(
                caption_text,
                parse_mode=enums.ParseMode.HTML,
                reply_markup=keyboard
            )
            logger.warning("START_GIF not set. Using text fallback for /start command.")
        
        # Add reaction to the sent message
        await bot.set_message_reaction(
            chat_id=message.chat.id,
            message_id=sent_message.id,
            reaction=ReactionTypeEmoji(emoji=START_REACTION if 'START_REACTION' in globals() else "🎉")
        )
        # Auto-react to user's /start command
        await bot.set_message_reaction(
            chat_id=message.chat.id,
            message_id=message.id,
            reaction=ReactionTypeEmoji(emoji="👍")
        )
    except Exception as e:
        logger.error(f"Error in /start: {str(e)}, START_GIF: {animation_id if animation_id else 'Not set'}")
        await message.reply_text(
            "<b><blockquote>Oᴘs, Sᴏᴍᴇᴛʜɪɴɢ Wᴇɴᴛ Wʀᴏɴɢ! Tʀʏ Aɢᴀɪɴ Oʀ Hɪᴛ Uᴘ <a href='https://t.me/CodeflixSupport'>Sᴜᴘᴘᴏʀᴛ</a>.<blockquote></b>",
            parse_mode=enums.ParseMode.HTML
        )
        if "Expected ANIMATION, got STICKER" in str(e):
            logger.error(f"Invalid animation file ID: {animation_id}. Please update START_GIF with a valid animation file ID.")

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["total_users"]))
async def all_db_users_here(client, message):
    silicon = await message.reply_text("<blockquote>⏳ Cʜᴇᴄᴋɪɴɢ...</blockquote>", parse_mode=enums.ParseMode.HTML)
    silicon_botz = await total_user()
    await silicon.edit(f"<blockquote>👥 Tᴏᴛᴀʟ Usᴇʀs: <code>{silicon_botz}</code></blockquote>", parse_mode=enums.ParseMode.HTML)

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["broadcast"]))
async def broadcast(bot, message):
    if not message.reply_to_message:
        return await message.reply_text("<blockquote>Rᴇᴘʟʏ Tᴏ A Mᴇssᴀɢᴇ Tᴏ Bʀᴏᴀᴅᴄᴀsᴛ!</blockquote>", parse_mode=enums.ParseMode.HTML)
    silicon = await message.reply_text("<blockquote>Fᴇᴛᴄʜɪɴɢ Usᴇʀs...</blockquote>", parse_mode=enums.ParseMode.HTML)
    all_users = await getid()
    tot = await total_user()
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    await silicon.edit(f"<blockquote>📢 Bʀᴏᴀᴅᴄᴀsᴛɪɴɢ...</blockquote>", parse_mode=enums.ParseMode.HTML)
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
                f"<blockquote><u>Bʀᴏᴀᴅᴄᴀsᴛ Sᴛᴀᴛᴜs</u>\n\n👥 Tᴏᴛᴀʟ: {tot}\n✅ Sᴜᴄᴄᴇss: {success}\n🚫 Bʟᴏᴄᴋᴇᴅ: {blocked}\n🪦 Dᴇᴀᴄᴛɪᴠᴀᴛᴇᴅ: {deactivated}\n❌ Fᴀɪʟᴇᴅ: {failed}</blockquote>",
                parse_mode=enums.ParseMode.HTML
            )
        except FloodWait as e:
            await asyncio.sleep(e.value)
    await silicon.edit(
        f"<blockquote><u>🎉 Bʀᴏᴀᴅᴄᴀsᴛ Dᴏɴᴇ!</u>\n\n👥 Tᴏᴛᴀʟ: {tot}\n✅ Sᴜᴄᴄᴇss: {success}\n🚫 Bʟᴏᴄᴋᴇᴅ: {blocked}\n🪦 Dᴇᴀᴄᴛɪᴠᴀᴛᴇᴅ: {deactivated}\n❌ Fᴀɪʟᴇᴅ: {failed}</blockquote>",
        parse_mode=enums.ParseMode.HTML
    )

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command("restart"))
async def restart_bot(b, m):
    silicon = await b.send_message(
        text="<blockquote>🔄 Sʜᴜᴛᴛɪɴɢ Dᴏᴡɴ...</blockquote>",
        chat_id=m.chat.id,
        parse_mode=enums.ParseMode.HTML
    )       
    await asyncio.sleep(3)
    await silicon.edit("<blockquote>🚀 Bᴀᴄᴋ Oɴʟɪɴᴇ! Rᴇᴀᴅʏ Tᴏ Rᴏʟʟ!</blockquote>", parse_mode=enums.ParseMode.HTML)
    os.execl(sys.executable, sys.executable, *sys.argv)

@Client.on_message(filters.command("set_cap") & filters.channel)
async def setCap(bot, message):
    if len(message.command) < 2:
        return await message.reply(
            "<blockquote>📝 Usᴀɢᴇ: <b>/set_cap Yᴏᴜʀ Cᴀᴘᴛɪᴏɴ</b>\nUsᴇ <code>{file_name}</code> Fᴏʀ Fɪʟᴇ Nᴀᴍᴇ.\nUsᴇ <code>{file_size}</code> Fᴏʀ Sɪᴢᴇ.\nUsᴇ <code>{link}</code> Fᴏʀ Lɪɴᴋ.\n\nEx: <code>/set_cap <a href='{link}'>{file_name}</a> - {file_size}</code></blockquote>",
            parse_mode=enums.ParseMode.HTML
        )
    chnl_id = message.chat.id
    caption = message.text.split(" ", 1)[1] if len(message.text.split(" ", 1)) > 1 else None
    chkData = await chnl_ids.find_one({"chnl_id": chnl_id})
    if chkData:
        await updateCap(chnl_id, caption)
        return await message.reply(
            f"<blockquote>✅ Nᴇᴡ Cᴀᴘᴛɪᴏɴ Sᴇᴛ: {html.escape(caption)}</blockquote>",
            parse_mode=enums.ParseMode.HTML
        )
    else:
        await addCap(chnl_id, caption)
        return await message.reply(
            f"<blockquote>🎉 Cᴀᴘᴛɪᴏɴ Sᴇᴛ: {html.escape(caption)}</blockquote>",
            parse_mode=enums.ParseMode.HTML
        )

@Client.on_message(filters.command("set_font") & filters.channel)
async def setFont(bot, message):
    if len(message.command) < 2:
        return await message.reply(
            f"<blockquote>🖌️ Usᴀɢᴇ: <b>/set_font STYLE</b>\n\nSᴛʏʟᴇs: {', '.join(VALID_FONT_STYLES)}\n\nEx: /set_font SMALLCAPS</blockquote>",
            parse_mode=enums.ParseMode.HTML
        )
    chnl_id = message.chat.id
    font_style = message.command[1].upper()
    if font_style not in VALID_FONT_STYLES:
        return await message.reply(
            f"<blockquote>❌ Iɴᴠᴀʟɪᴅ Sᴛʏʟᴇ! Pɪᴄᴋ Fʀᴏᴍ: {', '.join(VALID_FONT_STYLES)}</blockquote>",
            parse_mode=enums.ParseMode.HTML
        )
    chkData = await chnl_ids.find_one({"chnl_id": chnl_id})
    if not chkData:
        return await message.reply(
            "<blockquote>📝 Sᴇᴛ A Cᴀᴘᴛɪᴏɴ Wɪᴛʜ /set_cap Fɪʀsᴛ!</blockquote>",
            parse_mode=enums.ParseMode.HTML
        )
    await updateFontStyle(chnl_id, font_style)
    await message.reply(
        f"<blockquote>🖌️ Fᴏɴᴛ Sᴇᴛ Tᴏ: {font_style}</blockquote>",
        parse_mode=enums.ParseMode.HTML
    )

@Client.on_message(filters.command("set_link") & filters.channel)
async def setLink(bot, message):
    if len(message.command) < 3:
        return await message.reply(
            "<blockquote>🔗 Usᴀɢᴇ: <b>/set_link TEXT URL</b>\n\nEx: <code>/set_link Watch_Now https://t.me/CodeFlix_Bots</code></blockquote>",
            parse_mode=enums.ParseMode.HTML
        )
    chnl_id = message.chat.id
    link_text = message.command[1]
    link_url = message.command[2]
    chkData = await chnl_ids.find_one({"chnl_id": chnl_id})
    if not chkData:
        return await message.reply(
            "<blockquote>📝 Sᴇᴛ A Cᴀᴘᴛɪᴏɴ Wɪᴛʜ /set_cap Fɪʀsᴛ!</blockquote>",
            parse_mode=enums.ParseMode.HTML
        )
    await chnl_ids.update_one({"chnl_id": chnl_id}, {"$set": {"link_text": link_text, "link_url": link_url}}, upsert=True)
    await message.reply(
        f"<blockquote>🔗 Lɪɴᴋ Sᴇᴛ: <a href='{html.escape(link_url)}'>{html.escape(link_text)}</a></blockquote>",
        parse_mode=enums.ParseMode.HTML
    )

@Client.on_message(filters.command("del_cap") & filters.channel)
async def delCap(_, msg):
    chnl_id = msg.chat.id
    try:
        await chnl_ids.delete_one({"chnl_id": chnl_id})
        return await msg.reply(
            "<blockquote><b><i>✅ Cᴀᴘᴛɪᴏɴ Dᴇʟᴇᴛᴇᴅ! Nᴏᴡ Usɪɴɢ Dᴇғᴀᴜʟᴛ.</i></b></blockquote>",
            parse_mode=enums.ParseMode.HTML
        )
    except Exception as e:
        e_val = await msg.reply(
            f"<blockquote>❌ Eʀʀᴏʀ: {html.escape(str(e))}</blockquote>",
            parse_mode=enums.ParseMode.HTML
        )
        await asyncio.sleep(5)
        await e_val.delete()

@Client.on_message(filters.command("stats") & filters.user(ADMIN))
async def stats(bot, message):
    silicon = await message.reply_text("<blockquote>⏳ Fᴇᴛᴄʜɪɴɢ Sᴛᴀᴛs...</blockquote>", parse_mode=enums.ParseMode.HTML)
    total_users = await total_user()
    total_channels = await chnl_ids.count_documents({})
    await silicon.edit(
        f"<blockquote>📊 Bᴏᴛ Sᴛᴀᴛs\n\n👥 Tᴏᴛᴀʟ Usᴇʀs: <code>{total_users}</code>\n📢 Tᴏᴛᴀʟ Cʜᴀɴɴᴇʟs: <code>{total_channels}</code></blockquote>",
        parse_mode=enums.ParseMode.HTML
    )

@Client.on_message(filters.command("ping"))
async def ping(bot, message):
    start_time = time.time()
    silicon = await message.reply_text("<blockquote>🏓 Pɪɴɢɪɴɢ...</blockquote>", parse_mode=enums.ParseMode.HTML)
    end_time = time.time()
    ping_time = round((end_time - start_time) * 1000, 2)
    await silicon.edit(f"<blockquote>🏓 Pᴏɴɢ! <code>{ping_time}ms</code></blockquote>", parse_mode=enums.ParseMode.HTML)

@Client.on_message(filters.command("id"))
async def get_id(bot, message):
    chat_id = message.chat.id
    user_id = message.from_user.id if message.from_user else "Aɴᴏɴʏᴍᴏᴜs"
    reply = f"<blockquote>🆔 Cʜᴀᴛ ID: <code>{chat_id}</code>\n👤 Usᴇʀ ID: <code>{user_id}</code></blockquote>"
    if message.reply_to_message:
        reply += f"\n👤 Rᴇᴘʟɪᴇᴅ Usᴇʀ ID: <code>{message.reply_to_message.from_user.id}</code>"
    await message.reply_text(reply, parse_mode=enums.ParseMode.HTML)

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
                file_name = (
                    re.sub(r"@\w+\s*", "", file_name)
                    .replace("_", " ")
                    .replace(".", " ")
                )
                cap_dets = await chnl_ids.find_one({"chnl_id": chnl_id})
                try:
                    if cap_dets:
                        cap = cap_dets["caption"]
                        font_style = cap_dets.get("font_style", "NONE")
                        link = cap_dets.get("link_url", obj.web_page_url or "https://t.me/CodeFlix_Bots")
                        link_text = cap_dets.get("link_text", file_name)
                        replaced_caption = cap.format(
                            file_name=html.escape(file_name),
                            file_size=get_size(file_size),
                            default_caption=html.escape(default_caption),
                            language=language,
                            year=year,
                            link=link
                        )
                        if "{link}" in cap and link_text:
                            replaced_caption = replaced_caption.replace(f"<a href='{link}'>{html.escape(file_name)}</a>", f"<a href='{link}'>{html.escape(link_text)}</a>")
                        formatted_caption, parse_mode = format_caption(replaced_caption, font_style)
                        await message.edit_caption(caption=formatted_caption, parse_mode=parse_mode)
                    else:
                        replaced_caption = DEF_CAP.format(
                            file_name=html.escape(file_name),
                            file_size=get_size(file_size),
                            default_caption=html.escape(default_caption),
                            language=language,
                            year=year
                        )
                        formatted_caption, parse_mode = format_caption(replaced_caption, "NONE")
                        await message.edit_caption(caption=formatted_caption, parse_mode=parse_mode)
                except FloodWait as e:
                    await asyncio.sleep(e.value)
                except Exception as e:
                    logger.error(f"Error formatting caption: {str(e)}")
                    await message.reply_text(f"<b>❌ Eʀʀᴏʀ: {html.escape(str(e))}</b>", parse_mode=enums.ParseMode.HTML)
    return

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
                    [
                        InlineKeyboardButton("🌟 Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀɴɴᴇʟ", url=f"http://t.me/Tessia_Caption_Bot?startchannel=true")
                    ],[
                        InlineKeyboardButton("📢 Uᴘᴅᴀᴛᴇs", url=f"https://t.me/CodeFlix_Bots"),
                        InlineKeyboardButton("💬 Sᴜᴘᴘᴏʀᴛ", url=f"https://t.me/CodeflixSupport")
                    ],[
                        InlineKeyboardButton("ℹ️ Aʙᴏᴜᴛ", callback_data="about"),
                        InlineKeyboardButton("📚 Cᴏᴍᴍᴀɴᴅs", callback_data="help")
                    ]
                ]
            ),
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("Sᴛᴀʀᴛ Mᴇɴᴜ Lᴏᴀᴅᴇᴅ! 🚀")
    except Exception as e:
        logger.error(f"Error in start callback: {str(e)}")
        await query.message.reply_text("<b>😵 Eʀʀᴏʀ! Tʀʏ Aɢᴀɪɴ.</b>", parse_mode=enums.ParseMode.HTML)
        await query.answer("Eʀʀᴏʀ Oᴄᴄᴜʀʀᴇᴅ")

@Client.on_callback_query(filters.regex(r'^help'))
async def help(bot, query):
    try:
        await query.message.edit_text(
            text=script.HELP_TXT,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('ℹ️ Aʙᴏᴜᴛ', callback_data='about')
                    ],[
                        InlineKeyboardButton('🔙 Bᴀᴄᴋ', callback_data='start')
                    ]
                ]
            ),
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("Hᴇʟᴘ Mᴇɴᴜ Lᴏᴀᴅᴇᴅ! 📚")
    except Exception as e:
        logger.error(f"Error in help callback: {str(e)}")
        await query.message.reply_text("<b>😵 Fᴀɪʟᴇᴅ Tᴏ Sʜᴏᴡ Hᴇʟᴘ! Tʀʏ Aɢᴀɪɴ.</b>", parse_mode=enums.ParseMode.HTML)
        await query.answer("Eʀʀᴏʀ Oᴄᴄᴜʀʀᴇᴅ")

@Client.on_callback_query(filters.regex(r'^about'))
async def about(bot, query):
    try:
        await query.message.edit_text(
            text=script.ABOUT_TXT,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('📚 Hᴏᴡ Tᴏ Usᴇ', callback_data='help')
                    ],[
                        InlineKeyboardButton('🔙 Bᴀᴄᴋ', callback_data='start')
                    ]
                ]
            ),
            parse_mode=enums.ParseMode.HTML
        )
        await query.answer("Aʙᴏᴜᴛ Mᴇɴᴜ Lᴏᴀᴅᴇᴅ! 🌌")
    except Exception as e:
        logger.error(f"Error in about callback: {str(e)}")
        await query.message.reply_text("<b>😵 Fᴀɪʟᴇᴅ Tᴏ Sʜᴏᴡ Aʙᴏᴜᴛ! Tʀʏ Aɢᴀɪɴ.</b>", parse_mode=enums.ParseMode.HTML)
        await query.answer("Eʀʀᴏʀ Oᴄᴄᴜʀʀᴇᴅ")
