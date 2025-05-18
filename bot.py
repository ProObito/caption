import os
from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from datetime import timedelta
import time
from info import *
class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Auto Cap",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=200,
            plugins={"root": "body"},
            sleep_threshold=15,
        )
        self.start_time = time.time()  # Track bot start time for uptime

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.mention = me.mention
        self.username = me.username
         # Print startup message
        print(f"<b><blockquote expandable>{me.first_name} Iꜱ Sᴛᴀʀᴛᴇᴅ.....✨️</b></blockquote>")

        # Calculate uptime
        uptime_seconds = int(time.time() - self.start_time)
        uptime_string = str(timedelta(seconds=uptime_seconds))

        # Send startup message to admin and log channel
        for chat_id in [ADMIN, LOG_CHANNEL]:
            if chat_id == 0:  # Skip if not set
                continue
            try:
                await self.send_photo(
                    chat_id=chat_id,
                    photo=SILICON_PIC,
                    caption=("<b><blockquote expandable>{me.first_name} Iꜱ Sᴛᴀʀᴛᴇᴅ.....✨️\nUptime: `{uptime_string}`\nStarted by: {me.mention}<b><blockquote expandable>"),
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton("Updates", url="https://t.me/codeflix_bots")]]
                    )
                )
            except Exception as e:
                print(f"Failed to send message to chat {chat_id}: {e}")

if __name__ == "__main__":
    Bot().run()
