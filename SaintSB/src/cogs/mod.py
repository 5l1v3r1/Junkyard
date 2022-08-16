import asyncio, discord
from datetime import datetime
from discord.ext import commands
from random import uniform
from src.utils import *
from src.core import *

'''
This file contains moderation commands
'''

class mod_cog(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(name='ban')
    async def bancmd(self, ctx, user: discord.User, *, reason='was acting like a retard'):
        if self.client.user.id == ctx.message.author.id:
            if self.client.user.id == user.id:
                await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=outputstr(ctx.message.author, f'ban {user} {reason}', 'You can\'t ban yourself!'))
            else:
                try:
                    await ctx.guild.ban(user=user, reason=reason)
                    await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=outputstr(ctx.message.author, f'ban {user} {reason}', f'Ban "{user}" with reason "{reason}"'))
                except:
                    await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=outputstr(ctx.message.author, f'ban {user} {reason}', f'Failed to ban "{user}", maybe missing permissions?'))
            await asyncio.sleep(uniform(5, 10)); await ctx.message.edit(content=didyouknow())
        else:
            pass
    
    @commands.command(name='tempban')
    async def tempbancmd(self, ctx, user: discord.User, duration='5m', *, reason='was acting like a retard'):
        if self.client.user.id == ctx.message.author.id:
            if self.client.user.id == user.id:
                await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=outputstr(ctx.message.author, f'tempban {user} {reason}', 'You can\'t tempban yourself!'))
            else:
                try:
                    seconds = int(duration[:-1])
                    duration = duration[-1].lower()
                    if duration == "s":   seconds = seconds * 1
                    elif duration == "m": seconds = seconds * 60
                    elif duration == "h": seconds = seconds * 60 * 60
                    elif duration == "d": seconds = seconds * 86400

                    await ctx.guild.ban(user=user, reason=reason)
                    await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=outputstr(ctx.message.author, f'tempban {user} {reason}', f'Tempbanned "{user}" with reason "{reason}"'))
                    await asyncio.sleep(duration)
                    await ctx.guild.unban(member)

                    await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=outputstr(ctx.message.author, '', f'Un-tempbanned {user}'))
                except:
                    await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=outputstr(ctx.message.author, f'tempban {user} {reason}', f'Failed to tempban "{user}" , maybe missing permissions?'))
            await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=didyouknow())
        else:
            pass
    
    @commands.command(name='softban')
    async def softbancmd(self, ctx, user: discord.User, *, reason='was acting like a retard'):
        if self.client.user.id == ctx.message.author.id:
            if self.client.user.id == user.id:
                await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=outputstr(ctx.message.author, f'softban {user} {reason}', 'You can\'t softban yourself!'))
            else:
                try:
                    await ctx.guild.kick(user=user, reason=reason)
                    await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=outputstr(ctx.message.author, f'softban {user} {reason}', f'Softbanned "{user}" with reason "{reason}"'))
                    await asyncio.sleep(5)
                    await ctx.guild.unban(ctx.get_ban(user).user)

                    await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=outputstr(ctx.message.author, '', f'Un-softbanned "{user}"'))
                except:
                    await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=outputstr(ctx.message.author, f'softban {user} {reason}', f'Failed to softban "{user}", maybe missing permissions?'))
            await asyncio.sleep(uniform(5, 10)); await ctx.message.edit(content=didyouknow())
        else:
            pass
    
        
    @commands.command(name='unban')
    async def unbancmd(self, ctx, user):
        if self.client.user.id == ctx.message.author.id:
            try:
                await ctx.guild.unban(user=ctx.get_ban(user).user)
                await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=outputstr(ctx.message.author, f'unban {user}', f'Unbanned "{user}"'))
            except:
                await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=outputstr(ctx.message.author, f'unban {user}', f'Failed to unban "{user}", maybe missing permissions?'))
            await asyncio.sleep(uniform(5, 10)); await ctx.message.edit(content=didyouknow())
        else:
            pass

    @commands.command(name='kick')
    async def kickcmd(self, ctx, user: discord.User, *, reason='was acting like a retard'):
        if self.client.user.id == ctx.message.author.id:
            if self.client.user.id == user.id:
                await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=outputstr(ctx.message.author, f'kick {user} {reason}', 'You can\'t kick yourself!'))
            else:
                try:
                    await ctx.guild.kick(user=user, reason=reason)
                    await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=outputstr(ctx.message.author, f'kick {user} {reason}', f'Kicked "{user}" with reason "{reason}"'))
                except:
                    await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=outputstr(ctx.message.author, f'kick {user} {reason}', f'Failed to kick "{user}", maybe missing permissions?'))
            await asyncio.sleep(uniform(5, 10)); await ctx.message.edit(content=didyouknow())
        else:
            pass
    
    @commands.command(name='addrole')
    async def addrolecmd(self, ctx, user: discord.Member, *, rolename):
        if self.client.user.id == ctx.message.author.id:
            role = discord.utils.find(lambda m: rolename.lower() in m.name.lower(), ctx.message.guild.roles)
            if not role:
                await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=outputstr(ctx.message.author, f'addrole {user} {rolename}', f'Couldn\'t find role "{rolename}"'))
            
            try:
                await user.add_roles(rolename)
                await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=outputstr(ctx.message.author, f'addrole {user} {rolename}', f'Added role "{rolename}" to user "{user}"'))
            except:
                 await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=outputstr(ctx.message.author, f'addrole {user} {rolename}', f'Failed to add role "{rolename}" to user, maybe missing permissions?'))
            await asyncio.sleep(uniform(5, 10)); await ctx.message.edit(content=didyouknow())
        else: 
            pass
    
    @commands.command(name='delrole')
    async def delrolecmd(self, ctx, user: discord.Member, *, rolename):
        if self.client.user.id == ctx.message.author.id:
            role = discord.utils.find(lambda m: rolename.lower() in m.name.lower(), ctx.message.guild.roles)
            if not role:
                await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=outputstr(ctx.message.author, f'delrole {user} {rolename}', f'Couldn\'t find role "{rolename}"'))
            
            try:
                await user.remove_roles(rolename)
                await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=outputstr(ctx.message.author, f'delrole {user} {rolename}', f'Removed role "{rolename}" from user "{user}"'))
            except:
                 await asyncio.sleep(uniform(2, 5)); await ctx.message.edit(content=outputstr(ctx.message.author, f'delrole {user} {rolename}', f'Failed to remove role "{rolename}" from user, maybe missing permissions?'))
            await asyncio.sleep(uniform(5, 10)); await ctx.message.edit(content=didyouknow())
        else: 
            pass

def setup(bot):
    bot.add_cog(mod_cog(bot))