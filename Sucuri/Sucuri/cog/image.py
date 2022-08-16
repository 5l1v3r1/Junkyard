# https://api.weky.xyz/

import requests, json, asyncio
from Sucuri.util import *
from discord.ext import commands
from random import choice, randint

class image_cog(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(name='gun')
    async def guncmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()
            
            pfp_url = str(self.client.user.avatar_url).strip("webp?size=1024")

            embed = make_embed(
                title='Sucuri Selfbot 1.0', 
                title_prefix=False,
                image=f'https://api.weky.xyz/canvas/gun?image={pfp_url}png',
                footer='Powered by weky.xyz',
                footer_icon='https://cdn.discordapp.com/avatars/809496186905165834/7dbf02cb782c7111b817f329cac0257a.png'
            )
            
            await ctx.send(embed=embed[1], delete_after=4.0) if embed[0] else await ctx.send(embed[1], delete_after=4.0)
        else:
            pass
    
    @commands.command(name='rifle')
    async def riflecmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()
            
            pfp_url = str(self.client.user.avatar_url).strip("webp?size=1024")            
            return await ctx.send(f'https://api.weky.xyz/canvas/rifleshoot?image={pfp_url}png')
        else:
            pass
    
    @commands.command(name='pray')
    async def praycmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()
            
            pfp_url = str(self.client.user.avatar_url).strip("webp?size=1024")            
            embed = make_embed(
                title='Sucuri Selfbot 1.0', 
                title_prefix=False,
                image=f'https://api.weky.xyz/canvas/pray?image={pfp_url}png',
                footer='Powered by weky.xyz',
                footer_icon='https://cdn.discordapp.com/avatars/809496186905165834/7dbf02cb782c7111b817f329cac0257a.png'
            )

            await ctx.send(embed=embed[1], delete_after=4.0) if embed[0] else await ctx.send(embed[1], delete_after=4.0)
        else:
            pass

    @commands.command(name='vr')
    async def vrcmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()
            
            pfp_url = str(self.client.user.avatar_url).strip("webp?size=1024")            
            embed = make_embed(
                title='Sucuri Selfbot 1.0', 
                title_prefix=False,
                image=f'https://api.weky.xyz/canvas/vr?image={pfp_url}png',
                footer='Powered by weky.xyz',
                footer_icon='https://cdn.discordapp.com/avatars/809496186905165834/7dbf02cb782c7111b817f329cac0257a.png'
            )
            
            await ctx.send(embed=embed[1], delete_after=4.0) if embed[0] else await ctx.send(embed[1], delete_after=4.0)
        else:
            pass
    
    @commands.command(name='http.cat')
    async def httpcatcmd(self, ctx, code="206"):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()
                    
            embed = make_embed(
                title='Sucuri Selfbot 1.0', 
                title_prefix=False,
                image=f'https://http.cat/{str(code)}',
                footer='Powered by http.cat',
                footer_icon='https://http.cat/icon192.png'
            )
            
            await ctx.send(embed=embed[1], delete_after=4.0) if embed[0] else await ctx.send(embed[1], delete_after=4.0)
        else:
            pass

    @commands.command(name='dog')
    async def dogcmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()
            
            req = requests.get('https://dog.ceo/api/breeds/image/random')
            dog_url = json.loads(req.content)['message']

            embed = make_embed(
                title='Sucuri Selfbot 1.0', 
                title_prefix=False,
                image=dog_url,
                footer='Powered by dog.ceo',
                footer_icon='https://dog.ceo/img/dog-api-logo.svg'
            )
            
            await ctx.send(embed=embed[1], delete_after=4.0) if embed[0] else await ctx.send(embed[1], delete_after=4.0)
        else:
            pass

    @commands.command(name='cat')
    async def catcmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()
            
            embed = make_embed(
                title='Sucuri Selfbot 1.0', 
                title_prefix=False,
                image='https://cataas.com/cat',
                footer='Powered by cataas.com',
                footer_icon='https://dog.ceo/img/dog-api-logo.svg'
            )

            await ctx.send(embed=embed[1], delete_after=4.0) if embed[0] else await ctx.send(embed[1], delete_after=4.0)
        else:
            pass
    
    @commands.command(name='gif')
    async def gifcmd(self, ctx, *, query=None):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            key = choice(Configuration().giphykeys)
            result_gif = ''
            if query == None or len(query) < 0: # random gif
                response = requests.get(f'https://api.giphy.com/v1/gifs/random?api_key={key}')
                result_gif = json.loads(response.text)['data']['images']['original']['url']
            else:
                query.replace(' ', '+')
                response = requests.get(f'http://api.giphy.com/v1/gifs/search?q={query}&api_key={key}&limit=10')
                data = json.loads(response.text)

                result_gif = data['data'][randint(0, 9)]['images']['original']['url']
            
            embed = make_embed(
                title='Sucuri Selfbot 1.0',
                title_prefix=False,
                image=result_gif,
                footer='Powered by Giphy',
                footer_icon='https://assets.materialup.com/uploads/5d38e79f-3463-4f72-8716-5c62b2d9847b/0x0ss-85.jpg'
            )

            await ctx.send(embed=embed[1], delete_after=4.0) if embed[0] else await ctx.send(embed[1], delete_after=4.0)
        else:
            pass

def setup(bot):
    bot.add_cog(image_cog(bot))