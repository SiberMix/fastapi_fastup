import asyncio

from telegram import Bot


class TelegramBot:
    def __init__(self, bot_token):
        self.bot_token = bot_token
        self.bot = Bot(token=self.bot_token)

    async def send_message(self, chat_id, message_text):
        await self.bot.send_message(chat_id=chat_id, text=message_text)