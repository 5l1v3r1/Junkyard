import time, asyncio
from discord.ext import commands
from Sucuri import bot
from Sucuri.util import *
from random import randint
from datetime import datetime

class main_cog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='info')
    async def infocmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            uptime = datetime.utcnow() - bot.start_time
            uptime = str(uptime).split('.')[0]
            hours, minutes, seconds = uptime.split(':')
            
            embed = make_embed(
                title='Bot Info',
                values=[('Bot Info', f'''```
                Sucuri Selfbot
                Version: 1.0
                Creator: {Configuration().author}
                Repo: https://github.com/Nexuzzzz/Sucuri
                Uptime: {hours} hours, {minutes} minutes and {seconds} seconds
                ```''', False)]
            )

            await ctx.send(embed=embed[1], delete_after=10.0) if embed[0] else await ctx.send(embed[1], delete_after=10.0)
        else:
            pass
    
    @commands.command(name='uptime')
    async def uptimecmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            uptime = datetime.utcnow() - bot.start_time
            uptime = str(uptime).split('.')[0]

            hours, minutes, seconds = uptime.split(':')
            
            embed = make_embed(
                title='Uptime', 
                values=[('Uptime', f'{hours} hours, {minutes} minutes and {seconds} seconds', False)]
            )

            await ctx.send(embed=embed[1], delete_after=10.0) if embed[0] else await ctx.send(embed[1], delete_after=10.0)
        else:
            pass
    
    @commands.command(name='latency')
    async def latencycmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            before = time.monotonic()
            embed = make_embed(
                title='Latency', 
                values=[('Latency', 'Pinging....', False)]
            )

            message = await ctx.send(embed=embed[1], delete_after=10.0) if embed[0] else await ctx.send(embed[1], delete_after=10.0)

            ping = (time.monotonic() - before) * 1000
            await asyncio.sleep(0.5)

            embed = make_embed(
                title='Latency', 
                values=[('Latency', f'The latency is: `{str(ping)} ms`', False)]
            )
            await message.edit(embed=embed[1]) if embed[0] else await ctx.send(embed[1])
            
        else:
            pass
    
    @commands.command(name='theme')
    async def themecmd(self, ctx, theme):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            Configuration().config_edit('theme', theme)

            embed = make_embed(
                title='Theme set.', 
            )

            await ctx.send(embed=embed[1], delete_after=10.0) if embed[0] else await ctx.send(embed[1], delete_after=10.0)
            
        else:
            pass
    
    @commands.command(aliases=['themelist', 'themes'])
    async def themelisrtcmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            themes = ''
            for filename in os.listdir('Sucuri/themes'):
                if filename.endswith('.json'):
                    info = theme_parse(filename.replace('.json',''))
                    themes += f'{info["theme_name"]}, by {info["theme_author"]}\n'

            embed = make_embed(
                title='Theme List', 
                values=[('List', f'```{themes}```', False)]
            )

            await ctx.send(embed=embed[1], delete_after=10.0) if embed[0] else await ctx.send(embed[1], delete_after=10.0)
            
        else:
            pass
    
    @commands.command(name='notheme')
    async def nothemecmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            Configuration().config_edit('theme', 'sucuri')

            embed = make_embed(
                title='Theme set.', 
            )

            await ctx.send(embed=embed[1], delete_after=10.0) if embed[0] else await ctx.send(embed[1], delete_after=10.0)
            
        else:
            pass
    
    @commands.command(name='credits')
    async def creditscmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            embed = make_embed(
                title='Credits', 
                values=[('Credits', '''```
Nexus: for creating the selfbot
Cuts: for the embed idea
TrustyJAID: for some cogs
NeuroAssassin: for some cogs
```''', False)]
            )
            
            await ctx.send(embed=embed[1], delete_after=10.0) if embed[0] else await ctx.send(embed[1], delete_after=10.0)
        else:
            pass
    
    @commands.command(aliases=['exit', 'logout', 'shutdown', 'close'])
    async def exitcmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            await self.client.close()
            exit()
            
        else:
            pass

def setup(bot):
    bot.add_cog(main_cog(bot))