import asyncpraw

from bin.config import conf
from bin.database import DataBase
from bin.bot import start_discord_bot

reddit = asyncpraw.Reddit(client_id=conf.get('reddit', 'client_id'),
                          client_secret=conf.get('reddit', 'client_secret'),
                          refresh_token=conf.get('reddit', 'refresh_token'),
                          user_agent=conf.get('reddit', 'user_agent'))


if __name__ == '__main__':
    DataBase.connect()
    start_discord_bot(conf.get('discord', 'token'))
