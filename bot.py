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
        self.force_channels = {}  # Dictionary to store channel IDs and their invite links

        # Handle force subscription channels
        for channel_var, channel_name in [
            ("FORCE_SUB_1", info.FORCE_SUB_1),
            ("FORCE_SUB_2", info.FORCE_SUB_2)
        ]:
            if channel_name:
                try:
                    link = await self.export_chat_invite_link(channel_name)
                    self.force_channels[channel_name] = link
                    print(f"Invite link for {channel_name}: {link}")
                except Exception as e:
                    print(f"Error generating invite link for {channel_name}: {e}")
                    print(f"Make sure the bot is an admin in {channel_name}")
                    self.force_channels[channel_name] = None

        # Print startup message
        print(f"<b><blockquote expandable>{me.first_name} Iꜱ Sᴛᴀʀᴛᴇᴅ.....✨️</b></blockquote>")

        # Calculate uptime
        uptime_seconds = int(time.time() - self.start_time)
        uptime_string = str(timedelta(seconds=uptime_seconds))

        # Send startup message to admin and log channel
        for chat_id in [info.ADMIN, info.LOG_CHANNEL]:
            if chat_id == 0:  # Skip if not set
                continue
            try:
                await self.send_photo(
                    chat_id=chat_id,
                    photo=info.SILICON_PIC,
                    caption=("<b><blockquote expandable>{me.first_name} Iꜱ Sᴛᴀʀᴛᴇᴅ.....✨️\nUptime: `{uptime_string}`\nStarted by: {me.mention}<b><blockquote expandable>"),
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton("Updates", url="https://t.me/codeflix_bots")]]
                    )
                )
            except Exception as e:
                print(f"Failed to send message to chat {chat_id}: {e}")

if __name__ == "__main__":
    Bot().run()
