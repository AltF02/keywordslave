import discord
from discord.ext import commands
from sqlite3 import IntegrityError, Connection
from disputils import BotEmbedPaginator


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.conn: Connection = bot.db_conn

    @commands.command(name="add")
    async def add(self, ctx, keyword: str):
        if len(keyword) <= 2:
            return await ctx.send("Please don't try to break me >:(")

        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO main.keywords (keyword, user_id) VALUES (LOWER(?),?)", (keyword, ctx.author.id))
            cursor.close()
            self.conn.commit()
        except IntegrityError:
            await ctx.send(f"Keyword `{keyword}` is already in the database")
        else:
            await ctx.send(f"Added `{keyword}`")

    @commands.command(name="remove")
    async def remove(self, ctx, keyword: str):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM keywords WHERE lower(keyword) = lower(?)", (keyword,))
        if cursor.rowcount > 0:
            await ctx.send(f"Removed `{keyword}`")
        else:
            await ctx.send(f"No such keyword exists")
        cursor.close()
        self.conn.commit()

    @commands.command(name="list")
    async def list(self, ctx, user: discord.Member = None):
        user = user or ctx.author
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM keywords WHERE user_id = (?)", (user.id,))
        rows = cursor.fetchall()

        if not rows:
            return await ctx.send(f"{user} has no keywords that I'm aware of :(")

        embeds = []
        keywords = []

        for i, row in enumerate(rows):
            keywords.append(f'• {row[0]}')
            if i % 10 == 0 and not i == 0:
                embeds.append(discord.Embed(color=0xEE7E38, description='\n'.join(keywords), title="Keywords"))
                keywords = []

        embeds.append(discord.Embed(color=0xEE7E38, description='\n'.join(keywords), title="Keywords"))

        await BotEmbedPaginator(ctx, embeds).run()

    @commands.Cog.listener(name="on_command_error")
    async def error_handler(self, ctx, error):
        if isinstance(error, commands.CommandNotFound) or isinstance(error, commands.UserNotFound):
            return
        else:
            await ctx.send(f"`{error}`\nPlease call my dad, I'm scared")
            raise error


def setup(bot):
    bot.add_cog(Commands(bot))
