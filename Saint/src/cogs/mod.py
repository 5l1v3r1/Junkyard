import asyncio, discord
from discord.ext import commands
from random import uniform

from src.utils import *
from src.config import *

class cog(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases=['help.mod', 'help.moderation', 'h.mod', 'commands.mod'])
    async def help(self, ctx) -> None:    
        '''
        await help_mod(context object) -> None

        about: Shows the moderation commands
        syntax: <prefix>help.mod
        aliases: help.mod, help.moderation, h.mod, commands.mod
        returns: The moderation commands

        :returns None: Nothing
        '''

        if self.client.user.id == ctx.message.author.id:
            pref = Configuration().prefix
            help_msg = Utils().ansify([
                f'$(cyan) - $(reset)Moderation commands',
                f'$(lcyan) - $(reset){pref}ban <user> <reason>                : Bans an user',
                f'$(lcyan) - $(reset){pref}tempban <user> <reason> <duration> : Temporary bans an user',
                f'$(lcyan) - $(reset){pref}softban <user> <reason>            : Bans, then unbans an user',
                f'$(lcyan) - $(reset){pref}unban <user>                       : Unbans an user',
                f'$(lcyan) - $(reset){pref}kick <user> <reason>               : Kicks an user',
                f'$(lcyan) - $(reset){pref}addrole <user> <role name>         : Adds the specified role to the user',
                f'$(lcyan) - $(reset){pref}delrole <user> <role name>         : Removes the specified role from the user'
                ], 
                fakeshell=True, 
                user=ctx.message.author, 
                message='help.mod'
            )

            await Utils().send_msg(ctx, help_msg, uniform(15,25))
        else:
            Utils().pprint(f'{ctx.message.author}/{ctx.message.author.id} tried executing a Saint command')
    
    @commands.command(aliases=['ban', 'banuser', 'beam'])
    async def ban(self, ctx, user: discord.User, *, reason='furry') -> None:    
        '''
        await ban(context object, user, ban reason) -> None

        about: Bans the specified user
        syntax: <prefix>ban <user> <reason>
        aliases: ban, banuser, beam
        returns: A message with the ban status

        :returns None: Nothing
        '''

        if self.client.user.id == ctx.message.author.id:
            if self.client.user.id == user.id:
                await Utils().send_msg(ctx, Utils().ansify('You can\'t ban yourself, dipshit', fakeshell=True, user=ctx.message.author, message=f'ban {user} {reason}'), uniform(5,10))            
            else:
                try:
                    await ctx.guild.ban(user=user, reason=reason)
                    await Utils().send_msg(ctx, Utils().ansify(f'Banned user {user}, because "{reason}"', fakeshell=True, user=ctx.message.author, message=f'ban {user} {reason}'), uniform(5,10))  
                except:
                    await Utils().send_msg(ctx, Utils().ansify(f'Failed to ban {user}, maybe missing permissions?', fakeshell=True, user=ctx.message.author, message=f'ban {user} {reason}'), uniform(5,10))
        else:
            Utils().pprint(f'{ctx.message.author}/{ctx.message.author.id} tried executing a Saint command')
    
    @commands.command(aliases=['tempban', 'tmpban', 'tempbanuser', 'tempbeam'])
    async def tempban(self, ctx, user: discord.User, duration='5m', *, reason='furry') -> None:    
        '''
        await tempban(context object, user, ban reason) -> None

        about: Temp-bans the specified user
        syntax: <prefix>tempban <user> <duration> <reason>
        aliases: tempban, tmpban, tempbanuser, tempbeam
        returns: A message with the temporary ban status

        :returns None: Nothing
        '''

        if self.client.user.id == ctx.message.author.id:
            if self.client.user.id == user.id:
                await Utils().send_msg(ctx, Utils().ansify('You can\'t temp-ban yourself, dipshit', fakeshell=True, user=ctx.message.author, message=f'tempban {user} {reason}'), uniform(5,10))
            else:
                try:
                    seconds = int(duration[:-1])
                    duration = duration[-1].lower()
                    if duration == "s": seconds = seconds * 1
                    elif duration == "m": seconds = seconds * 60
                    elif duration == "h": seconds = seconds * 60 * 60
                    elif duration == "d": seconds = seconds * 86400

                    await ctx.guild.ban(user=user, reason=reason)
                    await Utils().send_msg(ctx, Utils().ansify(f'Temporary banned {user}, because "{reason}"', fakeshell=True, user=ctx.message.author, message=f'tempban {user} {reason}'), uniform(5,10))
                    await asyncio.sleep(seconds)

                    await ctx.guild.unban(ctx.get_ban(user).user)

                    await Utils().send_msg(ctx, Utils().ansify(f'Unbanned {user}', fakeshell=True, user=ctx.message.author, message=f'tempban {user} {reason}'), uniform(5,10))
                except:
                    await Utils().send_msg(ctx, Utils().ansify(f'Failed to temp-ban {user}, maybe missing permissions?', fakeshell=True, user=ctx.message.author, message=f'tempban {user} {reason}'), uniform(5,10))
        else:
            Utils().pprint(f'{ctx.message.author}/{ctx.message.author.id} tried executing a Saint command')
    
    @commands.command(aliases=['softban', 'softbanuser', 'softbeam'])
    async def softban(self, ctx, user: discord.User, *, reason='furry') -> None:    
        '''
        await softban(context object, user, ban reason) -> None

        about: Bans the specified user for 5 seconds
        syntax: <prefix>softban <user> <reason>
        aliases: softban, softbanuser, softbeam
        returns: A message with the softban status

        :returns None: Nothing
        '''

        if self.client.user.id == ctx.message.author.id:
            if self.client.user.id == user.id:
                await Utils().send_msg(ctx, Utils().ansify('You can\'t softban yourself, dipshit', fakeshell=True, user=ctx.message.author, message=f'softban {user} {reason}'), uniform(5,10))            
            else:
                try:
                    await ctx.guild.ban(user=user, reason=reason)
                    await Utils().send_msg(ctx, Utils().ansify(f'Softbanned user {user}, because "{reason}"', fakeshell=True, user=ctx.message.author, message=f'softban {user} {reason}'), uniform(5,10))  

                    await asyncio.sleep(5)

                    await ctx.guild.unban(ctx.get_ban(user).user)
                    await Utils().send_msg(ctx, Utils().ansify(f'Unbanned {user}', fakeshell=True, user=ctx.message.author, message=f'softban {user} {reason}'), uniform(5,10))
                except:
                    await Utils().send_msg(ctx, Utils().ansify(f'Failed to softban {user}, maybe missing permissions?', fakeshell=True, user=ctx.message.author, message=f'softban {user} {reason}'), uniform(5,10))
        else:
            Utils().pprint(f'{ctx.message.author}/{ctx.message.author.id} tried executing a Saint command')
    
    @commands.command(aliases=['unban', 'unbanuser', 'unbeam'])
    async def unban(self, ctx, user: discord.User) -> None:    
        '''
        await ban(context object, user) -> None

        about: Unbans the specified user
        syntax: <prefix>unban <user>
        aliases: unban, unbanuser, unbeam
        returns: A message with the ban status

        :returns None: Nothing
        '''

        if self.client.user.id == ctx.message.author.id:
            if self.client.user.id == user.id:
                await Utils().send_msg(ctx, Utils().ansify('You can\'t unban yourself, dipshit', fakeshell=True, user=ctx.message.author, message=f'unban {user}'), uniform(5,10))            
            else:
                try:
                    await ctx.guild.unban(ctx.get_ban(user).user)
                    await Utils().send_msg(ctx, Utils().ansify(f'Unbanned user {user}', fakeshell=True, user=ctx.message.author, message=f'unban {user}'), uniform(5,10))  
                except:
                    await Utils().send_msg(ctx, Utils().ansify(f'Failed to unban {user}, maybe missing permissions?', fakeshell=True, user=ctx.message.author, message=f'unban {user}'), uniform(5,10))
        else:
            Utils().pprint(f'{ctx.message.author}/{ctx.message.author.id} tried executing a Saint command')
    
    @commands.command(aliases=['kick', 'kickuser', 'yeet'])
    async def kick(self, ctx, user: discord.User, *, reason='furry') -> None:    
        '''
        await kick(context object, user, ban reason) -> None

        about: Kicks the specified user
        syntax: <prefix>ban <user> <reason>
        aliases: kick, kickuser, yeet
        returns: A message with the kick status

        :returns None: Nothing
        '''

        if self.client.user.id == ctx.message.author.id:
            if self.client.user.id == user.id:
                await Utils().send_msg(ctx, Utils().ansify('You can\'t kick yourself, dipshit', fakeshell=True, user=ctx.message.author, message=f'kick {user} {reason}'), uniform(5,10))            
            else:
                try:
                    await ctx.guild.kick(user=user, reason=reason)
                    await Utils().send_msg(ctx, Utils().ansify(f'Kicked user {user}, because "{reason}"', fakeshell=True, user=ctx.message.author, message=f'kick {user} {reason}'), uniform(5,10))  
                except:
                    await Utils().send_msg(ctx, Utils().ansify(f'Failed to kick {user}, maybe missing permissions?', fakeshell=True, user=ctx.message.author, message=f'kick {user} {reason}'), uniform(5,10))
        else:
            Utils().pprint(f'{ctx.message.author}/{ctx.message.author.id} tried executing a Saint command')
    
    @commands.command(aliases=['addrole', 'appendrole'])
    async def addrole(self, ctx, user: discord.Member, *, rolename) -> None:    
        '''
        await addrole(context object, user, role name) -> None

        about: Adds a role to the specified user
        syntax: <prefix>addrole <user> <role name>
        aliases: addrole, appendrole
        returns: A message with the role status

        :returns None: Nothing
        '''

        if self.client.user.id == ctx.message.author.id:
            role = discord.utils.find(lambda m: rolename.lower() in m.name.lower(), ctx.message.guild.roles)
            if not role:
                return await Utils().send_msg(ctx, Utils().ansify(f'Error, role {rolename} not found', fakeshell=True, user=ctx.message.author, message=f'addrole {user} {rolename}'), uniform(5,10))            
            
            try:
                await user.add_roles(rolename)
                await Utils().send_msg(ctx, Utils().ansify(f'Added role {rolename} to  {user}', fakeshell=True, user=ctx.message.author, message=f'addrole {user} {rolename}'), uniform(5,10))  
            except:
                await Utils().send_msg(ctx, Utils().ansify(f'Failed to add role {rolename} to {user}, maybe missing permissions?', fakeshell=True, user=ctx.message.author, message=f'addrole {user} {rolename}'), uniform(5,10))
        else:
            Utils().pprint(f'{ctx.message.author}/{ctx.message.author.id} tried executing a Saint command')
    
    @commands.command(aliases=['delrole', 'deleterole', 'rmrole'])
    async def delrole(self, ctx, user: discord.Member, *, rolename) -> None:    
        '''
        await delrole(context object, user, role name) -> None

        about: Removes a role from the specified user
        syntax: <prefix>delrole <user> <role name>
        aliases: delrole, delerole, rmrole
        returns: A message with the role status

        :returns None: Nothing
        '''

        if self.client.user.id == ctx.message.author.id:
            role = discord.utils.find(lambda m: rolename.lower() in m.name.lower(), ctx.message.guild.roles)
            if not role:
                return await Utils().send_msg(ctx, Utils().ansify(f'Error, role {rolename} not found', fakeshell=True, user=ctx.message.author, message=f'delrole {user} {rolename}'), uniform(5,10))            
            
            try:
                await user.remove_roles(rolename)
                await Utils().send_msg(ctx, Utils().ansify(f'Removed role {rolename} from {user}', fakeshell=True, user=ctx.message.author, message=f'delrole {user} {rolename}'), uniform(5,10))  
            except:
                await Utils().send_msg(ctx, Utils().ansify(f'Failed to remove role {rolename} from {user}, maybe missing permissions?', fakeshell=True, user=ctx.message.author, message=f'delrole {user} {rolename}'), uniform(5,10))
        else:
            Utils().pprint(f'{ctx.message.author}/{ctx.message.author.id} tried executing a Saint command')

def setup(client):
    '''
    setup(client object) -> None

    Adds all the commands in a "commands.Cog" class to the main instance

    :param client discord.ext.commands.Bot:
    :returns None: Nothing
    '''

    client.add_cog(cog(client))