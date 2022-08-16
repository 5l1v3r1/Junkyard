import discord, asyncio, re
from Sucuri.util import *
from discord.ext import commands
from random import randint
from datetime import datetime

class mod_cog(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(name='ban')
    async def bancmd(self, ctx, member: discord.User, *, reason='was acting like a retard'):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()
            
            if member == self.client.user.id:
                print(f'{grey}[{white}{datetime.now().strftime("%H:%M:%S")}{grey}] {give_color()}You can\'t ban yourself dumbass: {white}{ctx.message.content}{reset}')
            else:
                await ctx.guild.ban(user=member, reason=reason)

                embed = make_embed(
                    title='User banned', 
                    values=[('User', str(member.name), False), ('User ID', str(member.id), False), ('Status', 'Banned', False), ('Duration', 'Until unbanned', False), ('Reason', reason, False)] )

                await ctx.send(embed=embed[1], delete_after=4.0) if embed[0] else await ctx.send(embed[1], delete_after=4.0)
        else:
            pass
    
    @commands.command(aliases=['tempban', 'tmpban'])
    async def tempbancmd(self, ctx, member: discord.User, duration='5m', reason='was acting like a retard'):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()
            
            if member == self.client.user.id:
                print(f'{grey}[{white}{datetime.now().strftime("%H:%M:%S")}{grey}] {give_color()}You can\'t tempban yourself dumbass: {white}{ctx.message.content}{reset}')
            else:
                
                seconds = int(duration[:-1])
                duration = duration[-1]
                if duration == "s":
                    seconds = seconds * 1
                elif duration == "m":
                    seconds = seconds * 60
                elif duration == "h":
                    seconds = seconds * 60 * 60
                elif duration == "d":
                    seconds = seconds * 86400
                else:
                    print(f'{grey}[{white}{datetime.now().strftime("%H:%M:%S")}{grey}] {give_color()}You\'ve got to specify a duration, ex: 10s (10 seconds) or 15m (15 minutes): {white}{ctx.message.content}{reset}')
                    return

                await ctx.guild.ban(user=member, reason=reason)
                embed = make_embed(
                    title='User banned', 
                    values=[('User', str(member.name), False), ('Duration', f'{str(seconds)}{duration}', False)] 
                )
                await ctx.send(embed=embed[1], delete_after=4.0) if embed[0] else await ctx.send(embed[1], delete_after=4.0)

                await asyncio.sleep(seconds)
                await ctx.guild.unban(member)

                embed = make_embed(
                    title='User unbanned', 
                    values=[('User', str(member.name), False), ('Duration', 'Finished', False)] 
                )
                await ctx.send(embed=embed[1], delete_after=4.0) if embed[0] else await ctx.send(embed[1], delete_after=4.0)
        else:
            pass

    @commands.command(name='unban')
    async def unbancmd(self, ctx, userid: int):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()
            
            user = await self.client.fetch_user(userid)
            await ctx.guild.unban(user)

            embed = make_embed(
                title='User unbanned', 
                values=[('User', user, False), ('Status', 'Unbanned', False)] 
            )

            await ctx.send(embed=embed[1], delete_after=4.0) if embed[0] else await ctx.send(embed[1], delete_after=4.0)
        else:
            pass
    
    @commands.command(name='kick')
    async def kickcmd(self, ctx, member: discord.User, *, reason='was acting like a retard'):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()
            
            if member == self.client.user.id:
                print(f'{grey}[{white}{datetime.now().strftime("%H:%M:%S")}{grey}] {give_color()}You can\'t kick yourself dumbass: {white}{ctx.message.content}{reset}')
            else:
                await ctx.guild.kick(user=member, reason=reason)

                embed = make_embed(
                    title='User kicked', 
                    values=[('User', str(member.name), False), ('User ID', str(member.id), False), ('Reason', reason, False)] )

                await ctx.send(embed=embed[1], delete_after=4.0) if embed[0] else await ctx.send(embed[1], delete_after=4.0)
        else:
            pass
    
    @commands.command(name='mute')
    async def mutecmd(self, ctx, member: discord.User, reason='was acting like a retard'):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()
            
            if member == self.client.user.id:
                print(f'{grey}[{white}{datetime.now().strftime("%H:%M:%S")}{grey}] {give_color()}You can\'t mute yourself dumbass: {white}{ctx.message.content}{reset}')
            else:

                role = discord.utils.get(ctx.guild.roles, name="muted")
                if not role:
                    role = await ctx.guild.roles.create_role(name="muted")

                    for channel in ctx.guild.channels:
                        await channel.set_permissions(role, speak=False, send_messages=False, read_message_history=True, read_messages=False)

                await member.add_roles(role, reason=reason)

                embed = make_embed(
                    title='User muted', 
                    values=[('User', str(member.name), False)] 
                )

                await ctx.send(embed=embed[1], delete_after=4.0) if embed[0] else await ctx.send(embed[1], delete_after=4.0)
        else:
            pass
    
    @commands.command(aliases=['tempmute', 'tmpmute'])
    async def tempmutecmd(self, ctx, member: discord.User, duration='5m', reason='was acting like a retard'):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()
            
            if member == self.client.user.id:
                print(f'{grey}[{white}{datetime.now().strftime("%H:%M:%S")}{grey}] {give_color()}You can\'t tempmute yourself dumbass: {white}{ctx.message.content}{reset}')
            else:

                role = discord.utils.get(ctx.guild.roles, name="muted")
                if not role:
                    role = await ctx.guild.roles.create_role(name="muted")

                    for channel in ctx.guild.channels:
                        await channel.set_permissions(role, speak=False, send_messages=False, read_message_history=True, read_messages=False)
                
                seconds = int(duration[:-1])
                duration = duration[-1]
                if duration == "s":
                    seconds = seconds * 1
                elif duration == "m":
                    seconds = seconds * 60
                elif duration == "h":
                    seconds = seconds * 60 * 60
                elif duration == "d":
                    seconds = seconds * 86400
                else:
                    print(f'{grey}[{white}{datetime.now().strftime("%H:%M:%S")}{grey}] {give_color()}You\'ve got to specify a duration, ex: 10s (10 seconds) or 15m (15 minutes): {white}{ctx.message.content}{reset}')
                    return

                await member.add_roles(role, reason=reason)
                embed = make_embed(
                    title='User muted', 
                    values=[('User', str(member.name), False), ('Duration', f'{str(seconds)}{duration}', False)] 
                )
                await ctx.send(embed=embed[1], delete_after=4.0) if embed[0] else await ctx.send(embed[1], delete_after=4.0)

                await asyncio.sleep(seconds)
                await member.remove_roles(role)

                embed = make_embed(
                    title='User unmuted', 
                    values=[('User', str(member.name), False), ('Duration', 'Finished', False)] 
                )
                await ctx.send(embed=embed[1], delete_after=4.0) if embed[0] else await ctx.send(embed[1], delete_after=4.0)
        else:
            pass
    
    @commands.command(name='unmute')
    async def unmutecmd(self, ctx, member: discord.User):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()
            
            role = discord.utils.get(ctx.guild.roles, name="muted")
            await member.remove_roles(role)

            embed = make_embed(
                title='User muted', 
                values=[('User', str(member.name), False)] 
            )

            await ctx.send(embed=embed[1], delete_after=4.0) if embed[0] else await ctx.send(embed[1], delete_after=4.0)
        else:
            pass
    
    @commands.command(name='rename')
    async def renamecmd(self, ctx, member: discord.Member, *, nickname):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            old_name = member.display_name
            await member.edit(nick=nickname)

            embed = make_embed(
                title='User renamed', 
                values=[('User', str(member.name), False), ('Old nickname', old_name, False), ('New nickname', nickname, False)] 
            )

            await ctx.send(embed=embed[1], delete_after=4.0) if embed[0] else await ctx.send(embed[1], delete_after=4.0)
        else:
            pass
    
    @commands.command(aliases=['steal', 'addemoji'])
    @commands.has_permissions(manage_emojis=True)
    async def addemojicmd(self, ctx, name, emoji_lnk):
        await asyncio.sleep(float(f'0.{randint(0, 5)}'))
        await ctx.message.delete()

        if emoji_lnk.startswith('http'): # its a url
            req = requests.get(emoji_lnk)
            if req.status_code == 404: print(f'{grey}[{white}{datetime.now().strftime("%H:%M:%S")}{grey}] {give_color()}Could not find emoji: {white}{ctx.message.content}{reset}')
            elif req.status_code == 429: print(f'{grey}[{white}{datetime.now().strftime("%H:%M:%S")}{grey}] {give_color()}Calm down, ur on ratelimit: {white}{ctx.message.content}{reset}')

        else:
            msg = re.sub('<:(.+):([0-9]+)>', '\\2', emoji_lnk)

            match = None
            exact_match = False
            for guild in self.client.guilds:
                for gld_emoji in guild.emojis:
                    if msg.strip().lower() in str(gld_emoji):
                        match = gld_emoji
                    if msg.strip() in (str(gld_emoji.id), gld_emoji.name):
                        match = gld_emoji
                        exact_match = True
                        break
                if exact_match:
                    break

            if not match:
                print(f'{grey}[{white}{datetime.now().strftime("%H:%M:%S")}{grey}] {give_color()}Could not find emoji: {white}{ctx.message.content}{reset}')
                return

            req = requests.get(match.url)
        
        emoji = await ctx.guild.create_custom_emoji(name=name, image=req.content)
        await ctx.send(f'Successfully added the emoji **{name}**: <{"a" if emoji.animated else ""}:{emoji.name}:{emoji.id}>!', delete_after=4.0)

def setup(bot):
    bot.add_cog(mod_cog(bot))