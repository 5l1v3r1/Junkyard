import asyncio, discord
from datetime import datetime
from discord.ext import commands
from random import uniform
from src.utils import *
from src.core import *
from random import choice

'''
This file contains NSFW commands
'''

class nsfw_cog(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases=['nekoapi','nekobot'])
    async def nekoapicmd(self, ctx, *, img_type='neko'):
        if self.client.user.id == ctx.message.author.id:
            if not img_type.lower() in ['hass', 'hmidriff', 'pgif', '4k', 'hentai', 'holo', 'hneko', 'neko', 'hkitsune', 'kemonomimi', 'anal', 'hanal', 'gonewild', 'kanna', 'ass', 'pussy', 'thigh', 'hthigh', 'gah', 'coffee', 'food', 'paizuri', 'tentacle', 'boobs', 'hboobs', 'yaoi']:
                await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=outputstr(ctx.message.author, f'nekoapi {img_type}', f'{img_type} is not a valid image type! Please choose from the following:\nhass, hmidriff, pgif, 4k, hentai, holo, hneko, neko, hkitsune, kemonomimi, anal, hanal, gonewild, kanna, ass, pussy, thigh, hthigh, gah, coffee, food, paizuri, tentacle, boobs, hboobs, yaoi'))
            else:
                req = requests.get(f'https://nekobot.xyz/api/image?type={img_type}', headers={'user-agent': 'Saint/1.0', 'content-type': 'application/json'}).json()
                await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=req['message'])
            await asyncio.sleep(uniform(20, 30)); await ctx.message.edit(content=didyouknow())
        else:
            pass
    
    @commands.command(aliases=['r34','rule34'])
    async def r34cmd(self, ctx, *, tags='neko'):
        if self.client.user.id == ctx.message.author.id:
            req = requests.get(f'https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&limit=10&json=1&tags={tags.replace(" ","+")}', headers={'user-agent': 'Saint/1.0', 'content-type': 'application/json'}).json()
            await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=choice(req)['file_url'])
            await asyncio.sleep(uniform(20, 30)); await ctx.message.edit(content=didyouknow())
        else:
            pass
    
    @commands.command(aliases=['tiddies','boobs'])
    async def boobcmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            req = requests.get('https://nekobot.xyz/api/image?type=boobs', headers={'user-agent': 'Saint/1.0', 'content-type': 'application/json'}).json()
            await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=req['message'])
            await asyncio.sleep(uniform(20, 30)); await ctx.message.edit(content=didyouknow())
        else:
            pass
    
    @commands.command(aliases=['htiddies','hboobs'])
    async def hboobcmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            req = requests.get('https://nekobot.xyz/api/image?type=hboobs', headers={'user-agent': 'Saint/1.0', 'content-type': 'application/json'}).json()
            await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=req['message'])
            await asyncio.sleep(uniform(20, 30)); await ctx.message.edit(content=didyouknow())
        else:
            pass
    
    @commands.command(aliases=['pussy','vagina'])
    async def pussycmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            req = requests.get('https://nekobot.xyz/api/image?type=pussy', headers={'user-agent': 'Saint/1.0', 'content-type': 'application/json'}).json()
            await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=req['message'])
            await asyncio.sleep(uniform(20, 30)); await ctx.message.edit(content=didyouknow())
        else:
            pass
    
    @commands.command(aliases=['hpussy','hvagina'])
    async def hpussycmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            req = requests.get('https://nekos.life/api/v2/img/pussy', headers={'user-agent': 'Saint/1.0', 'content-type': 'application/json'}).json()
            await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=req['url'])
            await asyncio.sleep(uniform(20, 30)); await ctx.message.edit(content=didyouknow())
        else:
            pass
    
    @commands.command(aliases=['ass','booty'])
    async def asscmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            req = requests.get('https://nekobot.xyz/api/image?type=ass', headers={'user-agent': 'Saint/1.0', 'content-type': 'application/json'}).json()
            await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=req['message'])
            await asyncio.sleep(uniform(20, 30)); await ctx.message.edit(content=didyouknow())
        else:
            pass
    
    @commands.command(aliases=['hass','hbooty'])
    async def hasscmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            req = requests.get('https://nekobot.xyz/api/image?type=hass', headers={'user-agent': 'Saint/1.0', 'content-type': 'application/json'}).json()
            await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=req['message'])
            await asyncio.sleep(uniform(20, 30)); await ctx.message.edit(content=didyouknow())
        else:
            pass
    
    @commands.command(aliases=['prongif','porngif'])
    async def porngifcmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            req = requests.get('https://nekobot.xyz/api/image?type=pgif', headers={'user-agent': 'Saint/1.0', 'content-type': 'application/json'}).json()
            await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=req['message'])
            await asyncio.sleep(uniform(20, 30)); await ctx.message.edit(content=didyouknow())
        else:
            pass
    
    @commands.command(name='midriff')
    async def midriffcmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            req = requests.get('https://nekobot.xyz/api/image?type=hmidriff', headers={'user-agent': 'Saint/1.0', 'content-type': 'application/json'}).json()
            await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=req['message'])
            await asyncio.sleep(uniform(20, 30)); await ctx.message.edit(content=didyouknow())
        else:
            pass
    
    @commands.command(name='lewdneko')
    async def lewdnekocmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            req = requests.get('https://nekobot.xyz/api/image?type=hneko', headers={'user-agent': 'Saint/1.0', 'content-type': 'application/json'}).json()
            await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=req['message'])
            await asyncio.sleep(uniform(20, 30)); await ctx.message.edit(content=didyouknow())
        else:
            pass
    
    @commands.command(name='lewdkitsune')
    async def lewdkitsunecmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            req = requests.get('https://nekobot.xyz/api/image?type=hkitsune', headers={'user-agent': 'Saint/1.0', 'content-type': 'application/json'}).json()
            await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=req['message'])
            await asyncio.sleep(uniform(20, 30)); await ctx.message.edit(content=didyouknow())
        else:
            pass
    
    @commands.command(name='thighs')
    async def thighscmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            req = requests.get('https://nekobot.xyz/api/image?type=thigh', headers={'user-agent': 'Saint/1.0', 'content-type': 'application/json'}).json()
            await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=req['message'])
            await asyncio.sleep(uniform(20, 30)); await ctx.message.edit(content=didyouknow())
        else:
            pass
    
    @commands.command(name='hthighs')
    async def hthighscmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            req = requests.get('https://nekobot.xyz/api/image?type=hthigh', headers={'user-agent': 'Saint/1.0', 'content-type': 'application/json'}).json()
            await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=req['message'])
            await asyncio.sleep(uniform(20, 30)); await ctx.message.edit(content=didyouknow())
        else:
            pass
    
    @commands.command(name='anal')
    async def analcmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            req = requests.get('https://nekobot.xyz/api/image?type=anal', headers={'user-agent': 'Saint/1.0', 'content-type': 'application/json'}).json()
            await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=req['message'])
            await asyncio.sleep(uniform(20, 30)); await ctx.message.edit(content=didyouknow())
        else:
            pass
    
    @commands.command(name='hanal')
    async def hanalcmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            req = requests.get('https://nekobot.xyz/api/image?type=hanal', headers={'user-agent': 'Saint/1.0', 'content-type': 'application/json'}).json()
            await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=req['message'])
            await asyncio.sleep(uniform(20, 30)); await ctx.message.edit(content=didyouknow())
        else:
            pass
    
    @commands.command(aliases=['4k', 'fourk'])
    async def fourkcmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            req = requests.get('https://nekobot.xyz/api/image?type=4k', headers={'user-agent': 'Saint/1.0', 'content-type': 'application/json'}).json()
            await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=req['message'])
            await asyncio.sleep(uniform(20, 30)); await ctx.message.edit(content=didyouknow())
        else:
            pass
    
    @commands.command(aliases=['yaoi', 'gay_hentai'])
    async def yaoicmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            req = requests.get('https://nekobot.xyz/api/image?type=yaoi', headers={'user-agent': 'Saint/1.0', 'content-type': 'application/json'}).json()
            await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=req['message'])
            await asyncio.sleep(uniform(20, 30)); await ctx.message.edit(content=didyouknow())
        else:
            pass
    
    @commands.command(aliases=['yuri', 'lesbian_hentai'])
    async def yuricmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            req = requests.get('https://nekobot.xyz/api/image?type=yuri', headers={'user-agent': 'Saint/1.0', 'content-type': 'application/json'}).json()
            await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=req['message'])
            await asyncio.sleep(uniform(20, 30)); await ctx.message.edit(content=didyouknow())
        else:
            pass

def setup(bot):
    bot.add_cog(nsfw_cog(bot))