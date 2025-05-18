import os

class script(object):
    START_TXT = """<b><blockquote expandable>Hᴇʟʟᴏ {}\n
ɪ ᴀᴍ ᴀᴜᴛᴏ ᴄᴀᴘᴛɪᴏɴ ʙᴏᴛ ᴡɪᴛʜ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ. Fᴏʀ ᴍᴏʀᴇ ɪɴғᴏ ᴏɴ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ, ᴄʟɪᴄᴋ ᴛʜᴇ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ.<b><blockquote expandable>\n
<blockquote>‣ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ: <a href='https://t.me/CodeflixSupport'>ᴄᴏᴅᴇғʟɪx</a></blockquote><b>"""

    HELP_TXT = """<b>✨ Available Commands</b><br><br>
• <b>/set_cap</b> <caption> — Set a custom caption for your channel. Use placeholders for file details and HTML tags for formatting/links.<br>
  Example: <code>/set_cap 🎥 {file_name} ({language}, {year}) - {file_size} | &lt;b&gt;❍ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ: &lt;a href='https://t.me/CodeFlix_Bots'&gt;ᴄᴏᴅᴇғʟɪx&lt;/a&gt;&lt;/b&gt;</code><br><br>
• <b>/set_font</b> <style> — Set the font style for captions. Requires a caption set with /set_cap. Available styles:<br>
  - <b>BOLD</b>: Makes text bold<br>
  - <b>ITALIC</b>: Makes text italic<br>
  - <b>UNDERLINE</b>: Underlines text<br>
  - <b>STRIKETHROUGH</b>: Strikes through text<br>
  - <b>MONOSPACE</b>: Uses fixed-width font<br>
  - <b>SPOILER</b>: Hides text until clicked<br>
  - <b>BLOCKQUOTE</b>: Adds a quote bar and indents text<br>
  - <b>NONE</b>: No formatting (default)<br>
  Example: <code>/set_font BLOCKQUOTE</code> (sets caption as a blockquote)<br>
  Example: <code>/set_font BOLD</code> (sets caption in bold)<br><br>
• <b>/del_cap</b> — Delete the custom caption and font style, reverting to the default caption.<br><br>
• <b>/start</b> — Start the bot and view the main menu.<br><br>
<b>📋 Instructions</b><br>
1. Add this bot to your channel with full admin rights (including 'Edit Messages').<br>
2. Use the commands above in your channel.<br>
3. Avoid forward tags on files for best results.<br>
4. Set a caption with /set_cap before using /set_font.<br><br>
<b>🔣 Format Placeholders</b><br>
• <code>{file_name}</code>: Original file name<br>
• <code>{file_size}</code>: File size<br>
• <code>{language}</code>: Language of file<br>
• <code>{year}</code>: Year of file<br>
• <code>{default_caption}</code>: Original caption<br><br>
<b>🔗 Adding Links</b><br>
Use HTML tags in the caption: <code>&lt;a href='URL'&gt;TEXT&lt;/a&gt;</code><br>
Example: <code>&lt;b&gt;❍ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ: &lt;a href='https://t.me/CodeFlix_Bots'&gt;ᴄᴏᴅᴇғʟɪx&lt;/a&gt;&lt;/b&gt;</code><br><br>
<b>🎯 Example Usage</b><br>
1. Set caption: <code>/set_cap 🎥 {file_name} ({language}, {year}) - {file_size} | &lt;b&gt;❍ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ: &lt;a href='https://t.me/CodeFlix_Bots'&gt;ᴄᴏᴅᴇғʟɪx&lt;/a&gt;&lt;/b&gt;</code><br>
2. Set font: <code>/set_font BLOCKQUOTE</code><br>
3. Post a video named "Movie_2023.mp4" (50MB, caption "Hindi 2023").<br>
   Result: <blockquote>🎥 Movie 2023 (Hindi, 2023) - 50.00 MB | <b>❍ ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ: <a href="https://t.me/CodeFlix_Bots">ᴄᴏᴅᴇғʟɪx</a></b></blockquote>
"""

    ABOUT_TXT = """<b>About Me</b><br><blockquote>
❍ <b>My Name:</b> <a href="https://t.me/tessia_caption_bot">Tessia</a><br>
❍ <b>Developer:</b> <a href="https://t.me/onlyyuji">Codeflix</a><br>
❍ <b>Owner:</b> <a href="https://t.me/ProYato">Yato</a><br>
❍ <b>Language:</b> <a href="https://www.python.org/">Python</a><br>
❍ <b>Database:</b> <a href="https://www.mongodb.com/">MongoDB</a><br>
❍ <b>Hosted on:</b> <a href="https://t.me/ProYato">VPS</a><br>
❍ <b>Main Channel:</b> <a href="https://t.me/CodeFlix_Bots">Codeflix</a><br>
❍ <b>Help Channel:</b> <a href="https://t.me/CodeflixSupport">Codeflix</a><br><br>
➻ Click the buttons below for help and more info about me.</blockquote>"""
<b>➻ Click the buttons below for help and more info about me.</b>"""
