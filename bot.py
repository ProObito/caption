import os
from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import time

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Auto Cap",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            workers=200,
            plugins={"root": "body"},  # Ensure the "body" directory exists with plugin files
            sleep_threshold=15,
        )
        self.start_time = time.time()  # Track bot start time for uptime

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.mention = me.mention
        self.username = me.username
        self.force_channel = Config.FORCE_SUB

        # Handle force subscription channel
        if self.force_channel:
            try:
                link = await self.export_chat_invite_link(self.force_channel)
                self.invitelink = link
            except Exception as e:
                print(f"Error generating invite link: {e}")
                print("Make sure the bot is an admin in the force sub channel")
                self.force_channel = None

        # Print startup message
        print(f"<b><blockquote expandable>{me.first_name} Iꜱ Sᴛᴀʀᴛᴇᴅ.....✨️</b></blockquote>")

        # Calculate uptime
        uptime_seconds = int(time.time() - self.start_time)
        uptime_string = str(timedelta(seconds=uptime_seconds))

        # Send startup message to admin and log channel
        for chat_id in [Config.ADMIN, Config.LOG_CHANNEL]:
            if chat_id == 0:  # Skip if not set
                continue
            try:
                await self.send_photo(
                    chat_id=chat_id,
                    photo=Config.START_PIC,
                    caption=(
                        f"**{me.first_name} Iꜱ Sᴛᴀʀᴛᴇᴅ.....✨️**\n\n"
                        f"**Uptime**: `{uptime_string}`\n"
                        f"**Started by**: {me.mention}"
                    ),
                    reply_markup=InlineKeyboardMarkup(
                        [[InlineKeyboardButton("Updates", url="https://t.me/codeflix_bots")]]
                    )
                )
            except Exception as e:
                print(f"Failed to send message to chat {chat_id}: {e}")

if __name__ == "__main__":
    Bot().run()
