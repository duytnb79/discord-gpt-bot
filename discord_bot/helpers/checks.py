
import json
import os
from typing import Callable, TypeVar

from discord.ext import commands
from discord_bot.exceptions import *
from discord_bot.helpers import db_manager

from dotenv import load_dotenv
load_dotenv('.env.local')

config = {
    "prefix": os.getenv('BOT_PREFIX_COMMAND'),
    "token": os.getenv('BOT_TOKEN'),
    "permissions": os.getenv('BOT_PERMISSIONS'),
    "application_id": os.getenv('BOT_APPLICATION_ID'),
    "sync_commands_globally": bool(os.getenv('BOT_SYNC_COMMANDS_GLOBAL')),
    "owners": json.loads(os.getenv('BOT_OWNER'))
}

T = TypeVar("T")


def is_owner() -> Callable[[T], T]:
    """
    This is a custom check to see if the user executing the command is an owner of the bot.
    """

    async def predicate(context: commands.Context) -> bool:
        print(config["owners"])
        if context.author.id not in config["owners"]:
            raise UserNotOwner
        return True

    return commands.check(predicate)


def not_blacklisted() -> Callable[[T], T]:
    """
    This is a custom check to see if the user executing the command is blacklisted.
    """

    async def predicate(context: commands.Context) -> bool:
        if await db_manager.is_blacklisted(context.author.id):
            raise UserBlacklisted
        return True

    return commands.check(predicate)