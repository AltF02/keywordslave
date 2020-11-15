from discord.ext import commands

from bin.database import DataBase


class Bot(commands.Bot):
    def __init__(self, database_conn):
        super().__init__(command_prefix=".keyword ", description='Reddit keyword bot',
                         case_insensitive=True)
        self.db_conn = database_conn
        self.add_commands()
        self.load_extension('bin.tasks')

    @staticmethod
    async def on_ready():
        print("Discord bot logged in...")

    # async def on_message(self, message: discord.Message):
    #     await message.channel.send(message.content)

    def add_commands(self):
        @self.command(name="add", pass_context=True)
        async def add(ctx, keyword: str):
            cursor = DataBase.conn.cursor()
            cursor.execute("INSERT INTO main.keywords (keyword) VALUES (?)", (keyword,))
            DataBase.conn.commit()
            await ctx.send(f"Added {keyword}")

        @self.command(name="remove", pass_context=True)
        async def remove(ctx, keyword: str):
            cursor = DataBase.conn.cursor()
            cursor.execute("")

def start_discord_bot(token: str):
    bot = Bot(database_conn=DataBase.conn)
    bot.run(token)
