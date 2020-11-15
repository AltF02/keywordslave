from bin.config import conf
from bin.database import DataBase
from bin.bot import start_discord_bot


if __name__ == '__main__':
    DataBase.connect()
    start_discord_bot(conf.get('discord', 'token'))
