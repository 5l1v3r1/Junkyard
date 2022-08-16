import asyncio, os, discord
from datetime import datetime
from discord.ext import commands
from random import uniform
from src.utils import *
from src.core import *

'''
This file contains the commands related to the bot
'''

class bot_cog(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(name='botinfo')
    async def botinfocmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            
            usrstr = f'{ctx.message.author}@saint'
            await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=f'''```ansi
{ctx.message.author}[0;34m@[0msaint ~> botinfo
[1;30m          _____            
[1;30m         /\    \           
[1;30m        /::\    \          
[1;30m       /::::\    \         
[1;30m      /::::::\    \        [0m{usrstr}
[1;30m     /:::/\:::\    \       [0;34m{"".join("-" for _ in range(len(usrstr)))}
[1;30m    /:::/__\:::\    \      [0mName: Saint Selfbot
[1;30m    \:::\   \:::\    \     [0mVersion: {Core.version}
[1;30m  ___\:::\   \:::\    \    [0mUptime: {str(Core.up_time)}
[1;30m /\   \:::\   \:::\    \   [0mRepository: [0;34m{Core.repository}[0m
[1;30m/::\   \:::\   \:::\____\  [0mAuthor: {Core.author}
[1;30m\:::\   \:::\   \::/    /  [0mCogs loaded: {str(Core.cogs_loaded)}
[1;30m \:::\   \:::\   \/____/   [0m
[1;30m  \:::\   \:::\    \       [0;30m███[0;31m███[0;32m███[0;34m███[0;35m███[0;36m███[0;37m███
[1;30m   \:::\   \:::\____\    
[1;30m    \:::\  /:::/    /    
[1;30m     \:::\/:::/    /     
[1;30m      \::::::/    /      
[1;30m       \::::/    /       
[1;30m        \::/    /        
[1;30m         \/____/          
```''')
            await asyncio.sleep(uniform(10, 20)); await ctx.message.edit(content=didyouknow())
        else:
            pass
    
    @commands.command(name='uptime')
    async def uptimecmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:

            hours, remainder = divmod(int((datetime.utcnow() - Core.start_time).total_seconds()), 3600)
            minutes, seconds = divmod(remainder, 60)
            days, hours = divmod(hours, 24)

            fmt = '{d} days, {h} hours, {m} minutes, and {s} seconds' if days else '{h} hours, {m} minutes, and {s} seconds'
            
            Core.up_time = fmt.format(d=days, h=hours, m=minutes, s=seconds)
            await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=outputstr(ctx.message.author, 'uptime' f'Uptime is: {Core.up_time}'))
            await asyncio.sleep(uniform(5, 10)); await ctx.message.edit(content=didyouknow())
        else:
            pass
    
    @commands.command(name='exit')
    async def exitcmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:

            await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=outputstr(ctx.message.author, 'exit', 'Byebye!'))
            await asyncio.sleep(uniform(5, 10)); await ctx.message.edit(content=didyouknow())
            await self.client.close()
            exit()
        else:
            pass
    
    @commands.command(name='loadcogs')
    async def loadcogscmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:

            await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=outputstr(ctx.message.author, 'loadcogs', 'Loading cog files'))
            for filename in os.listdir('src\cogs'):
                if filename.endswith('.py'):
                    try: self.client.load_extension(f'src.cogs.{filename[:-3]}')
                    except discord.ext.commands.errors.ExtensionAlreadyLoaded:
                        self.client.unload_extension(f'src.cogs.{filename[:-3]}')
                        self.client.load_extension(f'src.cogs.{filename[:-3]}')
                    except: self.client.reload_extension(f'src.cogs.{filename[:-3]}')
            
            await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=outputstr(ctx.message.author, 'loadcogs', 'Loaded cogs'))
            await asyncio.sleep(uniform(5, 10)); await ctx.message.edit(content=didyouknow())
        else:
            pass

def setup(bot):
    bot.add_cog(bot_cog(bot))