import asyncio, discord
from discord.ext import commands
from random import uniform

from src.utils import *
from src.config import *

class cog(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases=['h', 'help', '?', 'helpme', 'commands', 'c'])
    async def help(self, ctx) -> None:    
        '''
        await help(context object) -> None

        about: Shows the commands
        syntax: <prefix>help
        aliases: h, help, ?, helpme, commands, c
        returns: The commands list

        :returns None: Nothing
        '''

        if self.client.user.id == ctx.message.author.id:
            pref = Configuration().prefix
            help_msg = Utils().ansify([
                f'$(cyan) - $(reset)Help commands$(reset)',
                f'$(lcyan) - $(reset){pref}help      : Shows this message',
                f'$(lcyan) - $(reset){pref}help.mod  : Shows the moderation commands menu',
                f'$(lcyan) - $(reset){pref}help.fun  : Shows le funny commands',
                f'$(lcyan) - $(reset){pref}help.copy : Shows all copypasta commands'

                ], 
                fakeshell=True, 
                user=ctx.message.author, 
                message='help'
            )

            await Utils().send_msg(ctx, help_msg, uniform(15,25))
        else:
            Utils().pprint(f'{ctx.message.author}/{ctx.message.author.id} tried executing a Saint command')

def setup(client):
    '''
    setup(client object) -> None

    Adds all the commands in a "commands.Cog" class to the main instance

    :param client discord.ext.commands.Bot:
    :returns None: Nothing
    '''

    client.add_cog(cog(client))