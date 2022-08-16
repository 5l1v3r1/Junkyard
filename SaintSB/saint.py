'''
               _________      .__        __                
    .__       /   _____/____  |__| _____/  |_      .__     
  __|  |___   \_____  \\__  \ |  |/    \   __\   __|  |___ 
 /__    __/   /        \/ __ \|  |   |  \  |    /__    __/ 
    |__|     /_______  (____  /__|___|  /__|       |__|    
                     \/     \/        \/

[ + ] Saint Selfbot
[ + ] Developed by Nexus
[ + ] You are free to modify, or edit the source. You have to leave some credits tho :)
'''

# imports
from discord.ext import commands
from random import randint
from datetime import datetime
import traceback, json, asyncio, sys
from src.utils import *
from src.core import *
from random import uniform

client = commands.Bot(command_prefix=Configuration().prefix, self_bot=True)
client.remove_command('help')

@client.event
async def on_ready():
    clear()
    print('[ + ] Saint selfbot online.')

@client.command()
async def ping(ctx):    
    # command to test if the bot works    
    if client.user.id == ctx.message.author.id:

        await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content='pong!')
        await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=didyouknow())
    else:
        pass

@client.command()
async def cfg(ctx, key, value):
    if client.user.id == ctx.message.author.id:
        passed = True
        try: Configuration().config_edit(key, value)
        except: passed = False
        
        await asyncio.sleep(uniform(2, 5))
        if passed: await ctx.message.edit(content=f'```ansi\n{ctx.message.author}[0;34m@[0msaint ~> cfg {key} {value}\n[1;30m[[0;34m>[1;30m][0m [1;32mSuccess![0m\n```')
        else: await ctx.message.edit(content=f'```ansi\n{ctx.message.author}[0;34m@[0msaint ~> cfg {key} {value}\n[1;30m[[0;34m>[1;30m][0m [1;31mError![0m\n```')
        await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=didyouknow())
    else:
        pass

if __name__ == '__main__':
    
    if check(Configuration().token):
        for filename in os.listdir('src\cogs'):
            if filename.endswith('.py'):
                client.load_extension(f'src.cogs.{filename[:-3]}')
        Core.start_time = datetime.utcnow()
        client.run(Configuration().token, bot=False)
    else:
        sys.exit('[ + ] Invalid token.')