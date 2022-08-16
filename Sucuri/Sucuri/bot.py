import discord, time, os, threading
from discord.ext import commands
from datetime import datetime
from Sucuri.util import *
from random import randint
from Sucuri.statistics import *
import traceback

#anon_statistics = config['anon_statistics']

client = commands.Bot(command_prefix=Configuration().prefix, self_bot=True)
client.remove_command('help')

start_time = datetime.utcnow()

# Will come in future update!
'''
def tui_handler():
    while 1:
        try:
            color = give_color()
            print(f'{grey}┌────[{white}Enter command{color}]{grey}─{color}[{white}{datetime.now().strftime("%Y/%m/%d %H:%M:%S")}{color}]')
            cmd = input(f'{grey}└─{color}[{white}{os.getlogin()}{color}@{white}sucuri{color}]{white} ~${reset} ')
            if cmd == 'exit': sys.exit()
        except KeyboardInterrupt:
            sys.exit()
'''

def banner():

    color = give_color()
    print(f'''               
{color}   d888888o.       {white}| 
{color} .`8888:' `88.     {white}| Welcome to {color}Sucuri Selfbot
{color} 8.`8888.   Y8     {white}| Theme loaded: {color}{Configuration().theme_name}{white}, created by {color}{Configuration().theme_author}
{color} `8.`8888.         {white}|
{color}  `8.`8888.        {white}| [{lblue}https://github.com/Nexuzzzz/Sucuri{white}]
{color}   `8.`8888.       {white}|
{color}    `8.`8888.      {white}| Welcome {color}{client.user}{white},
{color}8b   `8.`8888.     {white}| Selfbot prefix: {color}{Configuration().prefix}{white}
{color}`8b.  ;8.`8888     {white}|
{color} `Y8888P ,88P'     {white}| Quote of the day; {color}{random_quote()}{reset}
{reset}
''')
    
    counter = 0
    for filename in os.listdir('Sucuri/themes'):
        if filename.endswith('.json'):
            counter += 1

    print(f'{grey}[{white}{datetime.now().strftime("%H:%M:%S")}{grey}] {white}{str(counter)} themes loaded.{reset}\n')
    #thr = threading.Thread(target=tui_handler, daemon=True).start()

@client.event
async def on_ready():
    clear()
    setTitle(f'" Sucuri Selfbot | By {Configuration().author} | https://github.com/Nexuzzzz/Sucuri | Logged in as {client.user}"')
    banner()

@client.event
async def on_command_error(ctx, error): # inspired by the "exeter selfbot"
    color = give_color()

    if isinstance(error, commands.CommandNotFound):
        await ctx.message.delete()
        print(f'{color}[{white}{datetime.now().strftime("%H:%M:%S")}{color}] {white}Unknown command: {color}{ctx.message.content}{reset}')
    
    elif isinstance(error, commands.CheckFailure): 
        await ctx.message.delete()
        print(f'{color}[{white}{datetime.now().strftime("%H:%M:%S")}{color}] {white}Missing permissions: {color}{ctx.message.content}{reset}')
    
    elif isinstance(error, commands.MissingRequiredArgument): 
        await ctx.message.delete()
        print(f'{color}[{white}{datetime.now().strftime("%H:%M:%S")}{color}] {white}Missing arguments: {color}{ctx.message.content}{reset}')
    
    elif isinstance(error, discord.errors.Forbidden):
        await ctx.message.delete()
        print(f'{color}[{white}{datetime.now().strftime("%H:%M:%S")}{color}] {white}Forbidden: {color}{ctx.message.content}{reset}')
    
    elif isinstance(error, discord.errors.HTTPException):
        await ctx.message.delete()
        print(f'{color}[{white}{datetime.now().strftime("%H:%M:%S")}{color}] {white}HTTP Exception: {color}{ctx.message.content}{reset}')
    
    elif 'Cannot send an empty message' in str(error):
        print(f'{color}[{white}{datetime.now().strftime("%H:%M:%S")}{color}] {white}Message cannot be empty: {color}{ctx.message.content}{reset}')
    
    else: 
        print(f'{color}[{white}{datetime.now().strftime("%H:%M:%S")}{color}] {white}{str(error)}{reset}')

    pass

@client.command() # Dev command to reload commands without needing to restart the selfbot
async def loadcogs(ctx):
    if client.user.id == ctx.message.author.id:
        time.sleep(float(f'0.{randint(0, 5)}'))
        await ctx.message.delete()

        for filename in os.listdir('Sucuri\cog'):
            if filename.endswith('.py'):
                try:
                    client.load_extension(f'Sucuri.cog.{filename[:-3]}')
                except discord.ext.commands.errors.ExtensionAlreadyLoaded:
                    client.unload_extension(f'Sucuri.cog.{filename[:-3]}')
                    client.load_extension(f'Sucuri.cog.{filename[:-3]}')
                except:
                    client.reload_extension(f'Sucuri.cog.{filename[:-3]}')

        await ctx.send('Cogs reloaded.', delete_after=10.0)
    else:
        pass

@client.command()
async def test(ctx):
    if client.user.id == ctx.message.author.id:
        time.sleep(float(f'0.{randint(0, 5)}'))
        await ctx.message.delete()

        embed = make_embed(title='hello world!', values=[('Test title', 'Test message', False)])

        await ctx.send(embed=embed[1], delete_after=10.0) if embed[0] else await ctx.send(embed[1], delete_after=10.0)
    else:
        pass

@client.command()
async def cfg(ctx, key, value):
    if client.user.id == ctx.message.author.id:
        time.sleep(float(f'0.{randint(0, 5)}'))
        await ctx.message.delete()

        Configuration().config_edit(key, value)

        await ctx.send('config edited!', delete_after=10.0)
    else:
        pass

def start(token):
    setTitle(f'"Sucuri Selfbot | By {Configuration().author} | https://github.com/Nexuzzzz/Sucuri | Loading..."')

    for filename in os.listdir('Sucuri\cog'):
        if filename.endswith('.py'):
            client.load_extension(f'Sucuri.cog.{filename[:-3]}')

    client.run(token, bot=False)