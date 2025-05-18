import os

class script(object):
    START_TXT = """<b><blockquote expandable>Hᴇʟʟᴏ {}\n
ɪ ᴀᴍ ᴀᴜᴛᴏ ᴄᴀᴘᴛɪᴏɴ ʙᴏᴛ ᴡɪᴛʜ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ. Fᴏʀ ᴍᴏʀᴇ ɪɴғᴏ ᴏɴ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ, ᴄʟɪᴄᴋ ᴛʜᴇ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ.<b><blockquote expandable>\n
<blockquote>‣ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ: <a href='https://t.me/CodeflixSupport'>ᴄᴏᴅᴇғʟɪx</a></blockquote><b>"""

    HELP_TXT = """<b>✨ Available Commands</b>

• <b>/set_cap</b> <caption> — <i>Set a custom caption for your channel. Use placeholders for file details and links.<b>
  <b>Example: <code>/set_cap 🎥 {file_name} ({language}, {year}) - {file_size} | ❍ ʜᴇʟᴘ ᴄʜᴀɴɴᴇʟ: {link_text}</code><b>

• <b>/set_link</b> <text> <url> — <i>Set clickable text and URL for the <code>{link_text}</code> placeholder in captions.<b>
  <b>Example: <code>/set_link Codeflix https://t.me/CodeflixSupport</code><b>

• <b><blockquote>/set_font</b> <style> — Set the font style for captions. Requires a caption set with /set_cap. Available styles:
  - <b>BOLD</b>: Makes text bold
  - <b>ITALIC</b>: Makes text italic
  - <b>UNDERLINE</b>: Underlines text
  - <b>STRIKETHROUGH</b>: Strikes through text
  - <b>MONOSPACE</b>: Uses fixed-width font
  - <b>SPOILER</b>: Hides text until clicked
  - <b>BLOCKQUOTE</b>: Adds a quote bar and indents text
  - <b>NONE</b>: No formatting (default)
  Example: <code>/set_font BLOCKQUOTE</code> (sets caption as a blockquote)
  Example: <code>/set_font BOLD</code> (sets caption in bold)<blockquote expandable>

• <b>/del_cap</b> — Delete the custom caption, font style, and link, reverting to the default caption.

• <b>/start</b> — Start the bot and view the main menu.

<b><blockquote>📋 Instructions</b>
1. Add this bot to your channel with full admin rights (including 'Edit Messages').
2. Use the commands above in your channel.
3. Avoid forward tags on files for best results.
4. Set a caption with /set_cap before using /set_font or /set_link.

<b><blockquote>🔣 Format Placeholders</b>
• <code>{file_name}</code>: Original file name
• <code>{file_size}</code>: File size
• <code>{language}</code>: Language of file
• <code>{year}</code>: Year of file
• <code>{default_caption}</code>: Original caption
• <code>{link_text}</code>: Clickable text linking to a URL (set with /set_link)

<b><blockquote>🎯 Example Usage</b>
1. Set caption: <code>/set_cap 🎥 {file_name} ({language}) - {file_size} | ❍ ʜᴇʟᴘ ᴄʜᴀɴɴᴇʟ: {link_text}</code>
2. Set link: <code>/set_link Codeflix https://t.me/CodeflixSupport</code>
3. Set font: <code>/set_font BLOCKQUOTE</code>
4. Post a video named "Movie_2023.mp4" (50MB, caption "Hindi 2023").
   Result: <blockquote>🎥 Movie 2023 (Hindi) - 50.00 MB | ❍ ʜᴇʟᴘ ᴄʜᴀɴɴᴇʟ: <a href="https://t.me/CodeflixSupport">Codeflix</a></blockquote>
"""

    ABOUT_TXT = """<b>About Me</b>
<blockquote>
<b>❍ ᴍʏ ɴᴀᴍᴇ: <a href="https://t.me/tessia_caption_bot">ᴛᴇssɪᴀ</a><b>
<b>❍ ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href="https://t.me/onlyyuji">ᴄᴏᴅᴇғʟɪx</a><b>
<b>❍ ᴏᴡɴᴇʀ: <a href="https://t.me/ProYato">ʏᴀᴛᴏ</a><b>
<b>❍ ʟᴀɴɢᴜᴀɢᴇ: <a href="https://www.python.org/">ᴘʏᴛʜᴏɴ</a><b>
<b>❍ ᴅᴀᴛᴀʙᴀsᴇ: <a href="https://www.mongodb.com/">ᴍᴏɴɢᴏ ᴅʙ</a><b>
<b>❍ ʜᴏsᴛᴇᴅ ᴏɴ: <a href="https://t.me/ProYato">ᴠᴘs</a><b>
<b>❍ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ: <a href="https://t.me/CodeFlix_Bots">ᴄᴏᴅᴇғʟɪx</a><b>
<b>❍ ʜᴇʟᴘ ᴄʜᴀɴɴᴇʟ: <a href="https://t.me/CodeflixSupport">ᴄᴏᴅᴇғʟɪx</a><b>
<blockquote>
<b>➻ Click the buttons below for help and more info about me.</b>"""
