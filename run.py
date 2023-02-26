# from app.discord_bot.discord_api import client, discord_token

# if __name__== '__main__':
#     client.run(discord_token)


import os
from dotenv import load_dotenv

load_dotenv('.env.local')

print(os.getenv('BOT_TOKEN'))