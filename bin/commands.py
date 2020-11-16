from discord.ext import commands
from sqlite3 import IntegrityError, Connection


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.conn: Connection = bot.db_conn

    @commands.command(name="add")
    async def add(self, ctx, keyword: str):
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO main.keywords (keyword, user_id) VALUES (?,?)", (keyword, ctx.author.id))
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

    @commands.Cog.listener(name="on_command_error")
    async def error_handler(self, ctx, error):
        if isinstance(error, commands.CommandNotFound) or isinstance(error, commands.UserNotFound):
            return
        else:
            await ctx.send(f"`{error}`\nPlease call my dad, I'm scared")


def setup(bot):
    bot.add_cog(Commands(bot))
