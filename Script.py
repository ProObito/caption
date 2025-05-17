import os

class script(object):
    START_TXT = """Hᴇʟʟᴏ {}\n\n
ɪ ᴀᴍ ᴀᴜᴛᴏ ᴄᴀᴘᴛɪᴏɴ ʙᴏᴛ ᴡɪᴛʜ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ.Fᴏʀ ᴍᴏʀᴇ ɪɴғᴏ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ ᴄʟɪᴄᴋ ᴏɴ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ.\n\n
<b><blockquote expandable>‣ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://t.me/CodeflixSupport'>ᴄᴏᴅᴇғʟɪx</a><b><blockquote expandable>"""

    HELP_TXT = """<b><blockquote expandable>Available Commands:<blockquote expandable></b>

• <b><blockquote expandable>/set_cap</b> <caption> - Set a custom caption for your channel. Use placeholders to include file details.
  Example: <code>/set_cap 🎥 {file_name} ({language}, {year}) - {file_size}</code><b><blockquote expandable>

• <b><blockquote expandable>/set_font</b> <style> - Set the font style for your channel's captions. You must set a caption using /set_cap before setting a font style. Available styles:
  - <b>BOLD</b>: Makes text bold
  - <b>ITALIC</b>: Makes text italic
  - <b>UNDERLINE</b>: Underlines text
  - <b>STRIKETHROUGH</b>: Strikes through text
  - <b>MONOSPACE</b>: Uses fixed-width font
  - <b>SPOILER</b>: Hides text until clicked
  - <b>BLOCKQUOTE</b>: Adds a quote bar and indents text
  - <b>NONE</b>: No formatting (default)
  Example: <code>/set_font BLOCKQUOTE</code> (sets caption as a blockquote)
  Example: <code>/set_font BOLD</code> (sets caption in bold)<b><blockquote expandable>

• <b><blockquote expandable>/del_cap</b> - Delete the custom caption and font style, reverting to the default caption with no formatting.

• <b>/start</b> - Start the bot and see the main menu.<b><blockquote expandable>

<b><blockquote expandable>Instructions:<blockquote expandable></b>
1. Add this bot to your channel with full admin rights (including 'Edit Messages').
2. Use the above commands in your channel.
3. Keep files without forward tags for best results.
4. To set a font style, first set a caption with /set_cap, then use /set_font to choose a style.

<b><blockquote expandable>Format Placeholders:<blockquote expandable></b>
• <b><blockquote expandable><code>{file_name}</code> = Original File Name
• <code>{file_size}</code> = Original File Size
• <code>{language}</code> = Language of File Name
• <code>{year}</code> = Year of File
• <code>{default_caption}</code> = Original Caption of File<b><blockquote expandable>

<b><blockquote expandable>Example Usage:<blockquote expandable></b>
<b><blockquote expandable>1. Set caption: <code>/set_cap 🎥 {file_name} ({language}) - {file_size}</code>
2. Set font: <code>/set_font BOLD</code>
3. Post a video named "Movie_2023.mp4" (50MB, caption "Hindi 2023").
   Result: <b>🎥 Movie 2023 (Hindi) - 50.00 MB<blockquote expandable></b>
"""

    ABOUT_TXT = """<b><blockquote expandable>❍ ᴍʏ ɴᴀᴍᴇ : <a href="https://t.me/tessia_caption_bot">ᴛᴇssɪᴀ</a>
❍ ᴅᴇᴠᴇʟᴏᴩᴇʀ : <a href="https://t.me/onlyyuji">ᴄᴏᴅᴇғʟɪx</a>
❍ ᴏᴡɴᴇʀ : <a href="https://t.me/ProYato">ʏᴀᴛᴏ</a>
❍ ʟᴀɴɢᴜᴀɢᴇ : <a href="https://www.python.org/">ᴘʏᴛʜᴏɴ</a>
❍ ᴅᴀᴛᴀʙᴀꜱᴇ : <a href="https://www.mongodb.com/">ᴍᴏɴɢᴏ ᴅʙ</a>
❍ ʜᴏꜱᴛᴇᴅ ᴏɴ : <a href="https://t.me/ProYato">ᴠᴘs</a>
❍ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ : <a href="https://t.me/CodeFlix_Bots">ᴄᴏᴅᴇғʟɪx</a>
❍ ʜᴇʟᴩ ᴄʜᴀɴɴᴇʟ : <a href="https://t.me/CodeflixSupport">ᴄᴏᴅᴇғʟɪx</a><blockquote expandable>

<b><blockquote expandable>➻ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴜᴛᴛᴏɴs ɢɪᴠᴇɴ ʙᴇʟᴏᴡ ғᴏʀ ɢᴇᴛᴛɪɴɢ ʙᴀsɪᴄ ʜᴇʟᴩ ᴀɴᴅ ɪɴғᴏ ᴀʙᴏᴜᴛ ᴍᴇ.<blockquote expandable><b>"""
