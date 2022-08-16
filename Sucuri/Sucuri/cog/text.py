import string, asyncio
from discord.ext import commands
from random import choice, choices
from base64 import b64encode, b64decode
from hashlib import md5
from random import randint

class text_cog(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(name='uwu')
    async def uwucmd(self, ctx, *, message):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            for old, new in {'r': 'w', 'R': 'W', 'l': 'w', 'L': 'W', ' n': ' ny', ' N': ' NY', 'ove': 'uv', 'OVE': 'OV' }.items():
                message = message.replace(old, new)
                
            message += ' '+choice(['owo', 'OwO', 'uwu', 'UwU', '>w<', '^w^', '♥w♥', 'O3O', '-w-', 'XwX'])

            return await ctx.send(message)
        else:
            pass
    
    @commands.command(name='1337')
    async def _1337cmd(self, ctx, *, message):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            for old, new in {
                'e':'3', 'E':'3', 'l':'1', 'L':'1',
                'o':'0', 'O':'0', 'a':'4', 'A':'4', 
                'i':'1', 'I':'1'
                }.items():
                message = message.replace(old, new)

            return await ctx.send(message)
        else:
            pass
    
    @commands.command(name='clapclap')
    async def clapclapcmd(self, ctx, *, message):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            msg = ':clap:'
            msg += message.replace(' ', ':clap:')
            msg += ':clap:'

            return await ctx.send(msg)
        else:
            pass
    
    @commands.command(aliases=['b64enc', 'base64enc', 'b64encode'])
    async def b64enccmd(self, ctx, *, message):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            return await ctx.send( b64encode(message.encode()).decode() )
        else:
            pass
    
    @commands.command(aliases=['b64dec', 'base64dec', 'b64decode'])
    async def b64deccmd(self, ctx, *, message):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            return await ctx.send( b64decode(message.encode()).decode() )
        else:
            pass
    
    @commands.command(name='md5')
    async def md5cmd(self, ctx, *, message):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            return await ctx.send( md5(message.encode()).hexdigest() )
        else:
            pass
    
    @commands.command(name='purge')
    async def purgecmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            return await ctx.send('ﾠﾠ'+'\n' * 400 + 'ﾠﾠ')
        else:
            pass
    
    @commands.command(name='lmgtfy')
    async def lmgtfycmd(self, ctx, *, text):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            text = text.replace(' ', '%20')
            return await ctx.send(f'https://lmgtfy.app/?qtype=search&q={text}')
        else:
            pass
    
    @commands.command(name='fakenitro')
    async def fakenitrocmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            code = ''.join(choices(string.ascii_letters + string.digits, k=16))
            return await ctx.send(f'https://discord.com/gifts/{code}')
        else:
            pass
    
    @commands.command(name='shrug')
    async def shrugcmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            return await ctx.send('¯\_(ツ)_/¯')
        else:
            pass
    
    @commands.command(name='tableflip')
    async def tableflipcmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            return await ctx.send('(╯°□°）╯︵ ┻━┻')
        else:
            pass
    
    @commands.command(name='tableunflip')
    async def tableunflipcmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            return await ctx.send('┬─┬ ノ( ゜-゜ノ)')
        else:
            pass
    
    @commands.command(name='lenny')
    async def lennycmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            return await ctx.send('( ͡° ͜ʖ ͡°)')
        else:
            pass
    
    @commands.command(name='lennygun')
    async def lennyguncmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            return await ctx.send('( ͡° ͜ʖ ͡°)︻̷┻̿═━一-')
        else:
            pass
    
    @commands.command(name='lennyangry')
    async def lennyangrycmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            return await ctx.send('(╯°□°）╯')
        else:
            pass
    
    @commands.command(name='lennywink')
    async def lennywinkcmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            return await ctx.send('( ͡~ ͜ʖ ͡°)')
        else:
            pass
    
    @commands.command(name='lennydance')
    async def lennydancecmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            return await ctx.send('ᕕ(⌐■_■)ᕗ ♪♬')
        else:
            pass

def setup(bot):
    bot.add_cog(text_cog(bot))