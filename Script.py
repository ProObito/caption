import os

class script(object):
    START_TXT = """<b>🎉 Yo, {}! Wᴇʟᴄᴏᴍᴇ Tᴏ Tʜᴇ Uʟᴛɪᴍᴀᴛᴇ Aɴɪᴍᴇ Cʀᴇᴡ! 🚀</b>
I'ᴍ Tᴇssɪᴀ, Yᴏᴜʀ Aᴜᴛᴏ-Cᴀᴘᴛɪᴏɴ Sᴇɴᴘᴀɪ! Cᴜsᴛᴏᴍɪᴢᴇ Cᴀᴘᴛɪᴏɴs, Aᴅᴅ Lɪɴᴋs, Aɴᴅ Sᴘɪᴄᴇ Uᴘ Yᴏᴜʀ Cʜᴀɴɴᴇʟs Wɪᴛʜ Fᴀɴᴄʏ Fᴏɴᴛs! 😎
<blockquote>🌟 Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ: <a href='https://t.me/CodeflixSupport'>CᴏᴅᴇFʟɪx Cʀᴇᴡ</a></blockquote>
👇 Cʜᴇᴄᴋ Oᴜᴛ Tʜᴇ Bᴜᴛᴛᴏɴs Fᴏʀ Mᴏʀᴇ!"""

    HELP_TXT = """<b>🔥 Aᴡᴇsᴏᴍᴇ Cᴏᴍᴍᴀɴᴅs Fᴏʀ Yᴏᴜ, Sᴇɴᴘᴀɪ! 🚀</b>

• <b>/set_cap</b> <caption> — Cʀᴀғᴛ A Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ Wɪᴛʜ Pʟᴀᴄᴇʜᴏʟᴅᴇʀs Oʀ Lɪɴᴋs.
  Ex: <code>/set_cap 🎥 <a href='{link}'>{file_name}</a> ({language}, {year}) - {file_size}</code>

• <b>/set_font</b> <style> — Sᴛʏʟᴇ Yᴏᴜʀ Cᴀᴘᴛɪᴏɴs (Uᴇs /set_cap Fɪʀsᴛ). Sᴛʏʟᴇs:
  - <b>BOLD</b> 💪: <b>Bold Text</b>
  - <b>ITALIC</b> 𝘪𝘵𝘢𝘭𝘪𝘤: <i>Slanted Vibes</i>
  - <b>UNDERLINE</b> ⬇️: <u>Underlined Swag</u>
  - <b>STRIKETHROUGH</b> ~strike~: <s>Crossed Out</s>
  - <b>MONOSPACE</b> 🖥️: <code>Coder Aesthetic</code>
  - <b>SPOILER</b> 🙈: <spoiler>Hidden Gem</spoiler>
  - <b>BLOCKQUOTE</b> 📜: <blockquote>Quoted Epicness</blockquote>
  - <b>SMALLCAPS</b> 🅂🄼🄰🄻🄻: ꜱᴍᴀʟʟ ᴄᴀᴘꜱ ᴄᴏᴏʟ
  - <b>SANS</b> 🅂🄰🄽🅂: 𝗦𝗔𝗡𝗦 𝗦𝗘𝗥𝗜𝗙 𝗕𝗢𝗟𝗗
  - <b>NONE</b> 📄: Plain Jane
  Ex: <code>/set_font BOLD</code> → <b>Epic Caption</b>

• <b>/set_link</b> <text> <url> — Mᴀᴋᴇ Sᴘᴇᴄɪғɪᴄ Tᴇxᴛ Iɴ Cᴀᴘᴛɪᴏɴ Cʟɪᴄᴋᴀʙʟᴇ.
  Ex: <code>/set_link Watch_Now https://t.me/CodeFlix_Bots</code> → <a href='https://t.me/CodeFlix_Bots'>Watch_Now</a>

• <b>/del_cap</b> — Rᴇsᴇᴛ Cᴀᴘᴛɪᴏɴ Aɴᴅ Fᴏɴᴛ Tᴏ Dᴇғᴀᴜʟᴛ.

• <b>/stats</b> — Cʜᴇᴄᴋ Tᴏᴛᴀʟ Usᴇʀs Aɴᴅ Cʜᴀɴɴᴇʟs (Aᴅᴍɪɴ Oɴʟʏ).

• <b>/ping</b> — Tᴇsᴛ Bᴏᴛ’s Sᴘᴇᴇᴅ. Pɪɴɢ! 🏓

• <b>/id</b> — Gᴇᴛ Cʜᴀᴛ Oʀ Usᴇʀ ID.

• <b>/start</b> — Kɪᴄᴋsᴛᴀʀᴛ Tʜᴇ Bᴏᴛ Wɪᴛʜ A Fᴀɴᴄʏ Mᴇɴᴜ.

<b>Aᴅᴅ Cʟɪᴄᴋᴀʙʟᴇ Lɪɴᴋs</b>
Uᴇs <code><a href='{link}'>text</a></code> Iɴ /set_cap Oʀ /set_link Fᴏʀ Lɪɴᴋs Wɪᴛʜ Fᴏɴᴛs.
  Ex: <code>/set_cap <a href='{link}'>{file_name}</a> - {file_size}</code>
      <code>/set_font SANS</code>
      Vɪᴅᴇᴏ Wɪᴛʜ Lɪɴᴋ "https://t.me/CodeFlix_Bots" → <b><a href='https://t.me/CodeFlix_Bots'>Movie 2023</a> - 50.00 MB</b>

<b>Hᴏᴡ Tᴏ Rᴏᴄᴋ Iᴛ</b>
1. Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Cʜᴀɴɴᴇʟ Wɪᴛʜ Fᴜʟʟ Aᴅᴍɪɴ Rɪɢʜᴛs ('Eᴅɪᴛ Mᴇssᴀɢᴇs').
2. Usᴇ Cᴏᴍᴍᴀɴᴅs Iɴ Cʜᴀɴɴᴇʟ.
3. Aᴠᴏɪᴅ Fᴏʀᴡᴀʀᴅ Tᴀɢs Oɴ Fɪʟᴇs.
4. Sᴇᴛ Cᴀᴘᴛɪᴏɴ Wɪᴛʜ /set_cap Bᴇғᴏʀᴇ /set_font.

<b>Pʟᴀᴄᴇʜᴏʟᴅᴇʀs</b>
• <code>{file_name}</code>: Fɪʟᴇ Nᴀᴍᴇ
• <code>{file_size}</code>: Fɪʟᴇ Sɪᴢᴇ
• <code>{language}</code>: Fɪʟᴇ Lᴀɴɢᴜᴀɢᴇ
• <code>{year}</code>: Fɪʟᴇ Yᴇᴀʀ
• <code>{default_caption}</code>: Oʀɪɢɪɴᴀʟ Cᴀᴘᴛɪᴏɴ
• <code>{link}</code>: Cʟɪᴄᴋᴀʙʟᴇ URL

<b>Eᴘɪᴄ Exᴀᴍᴘʟᴇ</b>
1. <code>/set_cap 🎥 <a href='{link}'>{file_name}</a> ({language}) - {file_size}</code>
2. <code>/set_font SMALLCAPS</code>
3. Pᴏsᴛ Vɪᴅᴇᴏ "Movie_2023.mp4" (50MB, "Hindi 2023", Lɪɴᴋ "https://t.me/CodeFlix_Bots").
   Rᴇsᴜʟᴛ: <b>🎥 <a href='https://t.me/CodeFlix_Bots'>ᴍᴏᴠɪᴇ 2023</a> (ʜɪɴᴅɪ) - 50.00 ᴍʙ</b>
"""

    ABOUT_TXT = """<b>Aʙᴏᴜᴛ Yᴏᴜʀ Sᴇɴᴘᴀɪ</b>
<blockquote>
❍ Nᴀᴍᴇ: <a href="https://t.me/tessia_caption_bot">Tᴇssɪᴀ</a>
❍ Dᴇᴠᴇʟᴏᴘᴇʀ: <a href="https://t.me/onlyyuji">CᴏᴅᴇFʟɪx</a>
❍ Oᴡɴᴇʀ: <a href="https://t.me/ProYato">Yᴀᴛᴏ</a>
❍ Lᴀɴɢᴜᴀɢᴇ: <a href="https://www.python.org/">Pʏᴛʜᴏɴ</a>
❍ Dᴀᴛᴀʙᴀsᴇ: <a href="https://www.mongodb.com/">MᴏɴɢᴏDB</a>
❍ Hᴏsᴛᴇᴅ Oɴ: <a href="https://t.me/ProYato">VPS</a>
❍ Mᴀɪɴ Cʜᴀɴɴᴇʟ: <a href="https://t.me/CodeFlix_Bots">CᴏᴅᴇFʟɪx</a>
❍ Hᴇʟᴘ Cʜᴀɴɴᴇʟ: <a href="https://t.me/CodeflixSupport">CᴏᴅᴇFʟɪx Sᴜᴘᴘᴏʀᴛ</a>
</blockquote>
<b>➻ Hɪᴛ Tʜᴇ Bᴜᴛᴛᴏɴs Fᴏʀ Mᴏʀᴇ Iɴғᴏ! 🚀</b>"""
