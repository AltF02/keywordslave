from discord.ext import commands

from bin.database import DataBase


class Bot(commands.Bot):
    def __init__(self, database_conn):
        super().__init__(command_prefix=".keyword ", description='Reddit keyword bot',
                         case_insensitive=True)
        self.db_conn = database_conn
        self.load_extension('bin.commands')
        self.load_extension('bin.tasks')

    @staticmethod
    async def on_ready():
        print("Discord bot logged in...")


def start_discord_bot(token: str):
    bot = Bot(database_conn=DataBase.conn)
    bot.run(token)
