import asyncio
from discord.ext import commands
from random import uniform
from src.utils import *

'''
This file contains all the help commands
'''

class help_cog(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(name='help')
    async def helpcmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:

            await asyncio.sleep(uniform(10, 20)); await ctx.message.edit(content=f'''```ansi
{ctx.message.author}[0;34m@[0msaint ~> help
[1;30m[[0;34m>[1;30m][0m Help commands
[0;34m-[0m {Configuration().prefix}help.bot ~ bot stuff
[0;34m-[0m {Configuration().prefix}help.mod ~ moderation
[0;34m-[0m {Configuration().prefix}help.nsfw ~ nsfw
```''')
            await asyncio.sleep(uniform(5, 10)); await ctx.message.edit(content=didyouknow())
        else:
            pass
    
    @commands.command(name='help.bot')
    async def helpcmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:

            await asyncio.sleep(uniform(10, 20)); await ctx.message.edit(content=f'''```ansi
{ctx.message.author}[0;34m@[0msaint ~> help.bot
[1;30m[[0;34m>[1;30m][0m Help commands
[0;34m-[0m {Configuration().prefix}botinfo ~ show bot info
[0;34m-[0m {Configuration().prefix}uptime ~ show uptime
[0;34m-[0m {Configuration().prefix}exit ~ exit the bot
[0;34m-[0m {Configuration().prefix}loadcogs ~ reloads all cogs found in "src/cogs"
```''')
            await asyncio.sleep(uniform(5, 10)); await ctx.message.edit(content=didyouknow())
        else:
            pass
    
    @commands.command(name='help.mod')
    async def helpcmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:

            await asyncio.sleep(uniform(10, 20)); await ctx.message.edit(content=f'''```ansi
{ctx.message.author}[0;34m@[0msaint ~> help.mod
[1;30m[[0;34m>[1;30m][0m Moderation commands
[0;34m-[0m {Configuration().prefix}ban <user> <reason> ~ ban a user
[0;34m-[0m {Configuration().prefix}tempban <user> <duration> <reason> ~ temporary bans a user
[0;34m-[0m {Configuration().prefix}softban <user> <reason> ~ bans, then unbans a user
[0;34m-[0m {Configuration().prefix}unban <user> ~ unbans a user
[0;34m-[0m {Configuration().prefix}kick <user> <reason> ~ kick a user
[0;34m-[0m {Configuration().prefix}addrole <user> <role> ~ adds a role to a user
[0;34m-[0m {Configuration().prefix}delrole <user> <role> ~ removes a role from a user
```''')
            await asyncio.sleep(uniform(10, 20)); await ctx.message.edit(content=didyouknow())
        else:
            pass
    
    @commands.command(name='help.nsfw')
    async def helpcmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:

            await asyncio.sleep(uniform(10, 20)); await ctx.message.edit(content=f'''```ansi
{ctx.message.author}[0;34m@[0msaint ~> help.nsfw
[1;30m[[0;34m>[1;30m][0m NSFW commands
[0;34m-[0m {Configuration().prefix}nekoapi <image type> ~ uses the NekoAPI for images
[0;34m-[0m {Configuration().prefix}r34 <tags> ~ perform a rule34 lookup
[0;34m-[0m {Configuration().prefix}tiddies ~ shows boobs
[0;34m-[0m {Configuration().prefix}htiddies ~ anime boobs
[0;34m-[0m {Configuration().prefix}pussy ~ shows pussy
[0;34m-[0m {Configuration().prefix}hpussy ~ anime pussy
[0;34m-[0m {Configuration().prefix}ass ~ shows ass
[0;34m-[0m {Configuration().prefix}hass ~ anime ass
[0;34m-[0m {Configuration().prefix}prongif ~ sends a random porn gif
[0;34m-[0m {Configuration().prefix}midriff ~ don't ask
[0;34m-[0m {Configuration().prefix}lewdkitsune ~ lewd neko's
[0;34m-[0m {Configuration().prefix}lewdkitsune ~ lewd kitsunes
[0;34m-[0m {Configuration().prefix}thighs ~ irl thighs
[0;34m-[0m {Configuration().prefix}hthighs ~ anime thighs
[0;34m-[0m {Configuration().prefix}anal ~ irl anal
[0;34m-[0m {Configuration().prefix}hanal ~ anime anal
[0;34m-[0m {Configuration().prefix}4kpron ~ caught in 4K
[0;34m-[0m {Configuration().prefix}yaoi ~ gay hentai
[0;34m-[0m {Configuration().prefix}yuri ~ lesbian hentai
```''')
            await asyncio.sleep(uniform(10, 20)); await ctx.message.edit(content=didyouknow())
        else:
            pass

def setup(bot):
    bot.add_cog(help_cog(bot))