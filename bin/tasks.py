import discord
from discord.ext import commands, tasks

from bin.config import conf
from bin.database import DataBase
from bin.reddit import reddit


class Tasks(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.conn = bot.db_conn
        self.channel_id = conf.get('discord', 'channel_id')
        self.keyword_task.start()

    @tasks.loop()
    async def keyword_task(self):
        await self.bot.wait_until_ready()

        subreddit = await reddit.subreddit("matthewsplaypalace")  # dankmemes+memes+okbuddyretard
        async for submission in subreddit.stream.submissions():
            keywords = DataBase.get_keywords()
            if any(submission.title in i for i in keywords):
                await self.send_notification(submission)

    async def send_notification(self, submission):
        channel = await self.bot.fetch_channel(self.channel_id)
        embed = discord.Embed(color=0xEE7E38)
        embed.title = submission.title
        embed.set_author(name=submission.author.name, icon_url=submission.author.icon_url)
        if not submission.is_self:
            embed.set_image(url=submission.url)


def setup(bot):
    bot.add_cog(Tasks(bot))
