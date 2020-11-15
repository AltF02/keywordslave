import asyncpraw
from discord_webhook import DiscordWebhook, DiscordEmbed

from bin.database import DataBase
from bin.config import conf

reddit = asyncpraw.Reddit(client_id=conf.get('reddit', 'client_id'),
                          client_secret=conf.get('reddit', 'client_secret'),
                          refresh_token=conf.get('reddit', 'refresh_token'),
                          user_agent=conf.get('reddit', 'user_agent'))


# def send_webhook(submission):
#     webhook = DiscordWebhook(url=conf.get('discord', 'webhook_url'))
#     embed = DiscordEmbed(color=0xEE7E38)
#     embed.set_title(submission.title)
#     embed.set_url(submission.permalink)
#     embed.set_author(name=submission.author.name, icon_url=submission.author.icon_img)
#     embed.set_timestamp()
#     if not submission.is_self:
#         embed.set_image(url=submission.url)
#
#     webhook.add_embed(embed)
#     webhook.execute()

# def start_reddit_stream():
#     for submission in reddit.subreddit("dankmemes+memes+okbuddyretard").stream.submissions():
#         keywords = DataBase.get_keywords()
#         print(submission)
#         if submission.title in keywords:
#             send_webhook(submission)
