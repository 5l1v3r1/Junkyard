### ---- IMPORTS ---- ###
import asyncio
from discord.ext import commands
from datetime import datetime

from src.utils import *
from src.config import *
from src.core import *

client = commands.Bot(command_prefix=Configuration().prefix, self_bot=True)
client.remove_command('help')

@client.event
async def on_ready() -> None:
    '''
    await on_ready() -> None

    Runs when the bot has come online

    :returns None: Nothing
    '''

    Utils().clear()
    Utils().pprint('Saint selfbot online.')
    Utils().pprint(f'See the commands with "{Configuration().prefix}help"\n\n')

    Core.connected_at = datetime.now()

@client.command()
async def ping(ctx) -> None:    
    '''
    await ping() -> None

    about: Discord command to test if the bot is working
    syntax: <prefix>ping, example; ./ping or $ping
    aliases: None
    returns: The message "pong"

    :param ctx discord.ctx: Context object
    :returns None: Nothing
    '''

    if client.user.id == ctx.message.author.id:
        await Utils().send_msg(ctx, 'pong', uniform(2,5))
    else:
        Utils().pprint(f'{ctx.message.author}/{ctx.message.author.id} tried executing a Saint command')

if __name__ == '__main__':
    Core.started_at = datetime.now()

    if Utils().check_token():
        Utils().pprint('Loading commands', dotted=True)
        Utils().load_cogs(client)

        Utils().pprint('Connecting to discord...', dotted=True)
        client.run(Configuration().token, bot=False)
    else:
        Utils().pprint('Failed to authenticate, is the token correct?', exit_after=True)