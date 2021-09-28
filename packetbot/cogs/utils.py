from discord.ext import commands

class Util(commands.Cog):
    def __init__(self, bot, config):
        self.bot = bot
        self.bot.add_listener(self.on_message, "on_message")

    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        # if '@clear all' in message.content and message.author.permissions_in(message.channel).manage_messages:
        if message.content == '@clear all' and message.author.permissions_in(message.channel).manage_messages:
            deleted = await message.channel.purge(limit=100, check=is_not_pinned)
            await message.channel.send('Todas as mensagens foram apagadas.'.format(deleted))

        await self.bot.process_commands(message)