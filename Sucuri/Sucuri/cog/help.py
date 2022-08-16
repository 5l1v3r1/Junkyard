import asyncio
from Sucuri.util import *
from discord.ext import commands
from random import randint

class help_cog(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(name='help')
    async def helpcmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()
            
            embed = make_embed(
                title='Help Command', 
                values=[('Command List', '''
**help.bot** | Bot commands
**help.mod** | Moderation commands
**help.fun** | Fun commands
**help.image** | Image commands
**help.text** | Text commands
**help.anim** | Animated text commands
**help.nsfw** | NSFW commands
**help.music** | Music commands
**help.networking** | Networking
**help.abuse** | Abusive commands
**help.raid** | Raiding and Nuking
**help.copypasta** | Copy pastas
**help.info** | Info
**help.misc** | Misc commands
            ''', False)] )

            await ctx.send(embed=embed[1], delete_after=10.0) if embed[0] else await ctx.send(embed[1], delete_after=10.0)
        else:
            pass
    
    @commands.command(name='help.bot')
    async def help_bot(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()
            
            embed = make_embed(
                title='Bot Commands', 
                values=[('Command List', '''
**info** | Displays user info
**help** | Displays help message
**upawait asyncio** | Displays bot upawait asyncio
**latency** | Displays API latency
**theme <theme name>** | Sets a custom theme
**themelist** | Lists all aviable themes
**notheme** | Resets the custom theme
**credits** | Displays credits
**exit** | Exits the bot
            ''', False)] )

            await ctx.send(embed=embed[1], delete_after=10.0) if embed[0] else await ctx.send(embed[1], delete_after=10.0)
        else:
            pass

    @commands.command(name='help.mod')
    async def help_mod(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()
            
            embed = make_embed(
                title='Moderation Commands', 
                values=[('Command List', '''
**ban <user> <reason>** | Bans user
**unban <user id>** | Removes ban from user
**kick <user> <reason>** | Kicks user
**mute <user> <reason>** | Mutes user
**unmute <user>** | Unmutes a user
**tempmute <user> <reason> <duration>** | Temporarily mutes somebody
**rename <user> <new nick>** | Renames someone
**addemoji <emoji name> <emoji (emoji or url)>** | Adds a emoji
            ''', False)] )
            
            await ctx.send(embed=embed[1], delete_after=10.0) if embed[0] else await ctx.send(embed[1], delete_after=10.0)
        else:
            pass
    
    @commands.command(name='help.fun')
    async def help_fun(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()
            
            embed = make_embed(
                title='Fun Commands', 
                values=[('Command List', '''
**meme** | Sends a random meme
**joke** | Sends a random joke
**yomama** | Yo mama
**8ball** | Sends a random 8ball response
**quote** | Sends a random quote
**heck <user>** | Fake hacks a user
            ''', False)] )
            
            await ctx.send(embed=embed[1], delete_after=10.0) if embed[0] else await ctx.send(embed[1], delete_after=10.0)
        else:
            pass
    
    @commands.command(name='help.image')
    async def help_image(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()
            
            embed = make_embed(
                title='Image Commands', 
                values=[('Command List', '''
**gun** | Your pfp with a pistol   
**rifle** | Your pfp with a shotgun
**pray** | Spongebob prays to you
**vr** | You are so realistic!
**http.cat <status code>** | Sends a HTTP cat image
**dog** | Sends a image of a dog
**cat** | Sends a image of a cat
**gif <query>** | Sends a random/custom gif
**clyde <text>** | Makes it look like clyde said something
**changemymind <text>** | Puts some custom text on the Change My Mind meme
**deepfry <image url>** | Deepfries a image
**trump <text>** | Makes Trump say stupid shit
            ''', False)] )
            
            await ctx.send(embed=embed[1], delete_after=10.0) if embed[0] else await ctx.send(embed[1], delete_after=10.0)
        else:
            pass
    
    @commands.command(name='help.text')
    async def help_text(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()
            
            embed = make_embed(
                title='text Commands', 
                values=[('Command List', '''
**uwu <text>** | Uwu-ify's your text
**1337 <text>** | Makes your text 1337
**clapclap <text>** | Puts :clap: between every word
**b64enc <text>** | Base64 encodes your text
**b64dec <text>** | Base64 decodes your text
**md5 <text>** | MD5 hashes your text
**purge** | Fake chat clearing
**lmgtfy <text>** | Let me google that for you
**fakenitro** | Sends a fake nitro code
**shrug** | ¯\_(ツ)_/¯
**tableflip** | (╯°□°）╯︵ ┻━┻
**tableunflip** | ┬─┬ ノ( ゜-゜ノ)
**lenny** | ( ͡° ͜ʖ ͡°)
**lennygun** | ( ͡° ͜ʖ ͡°)︻̷┻̿═━一-
**lennyangry** | (╯°□°）╯
**lennywink** | ( ͡~ ͜ʖ ͡°)
**lennydance** | ᕕ(⌐■_■)ᕗ ♪♬
            ''', False)] )

            await ctx.send(embed=embed[1], delete_after=10.0) if embed[0] else await ctx.send(embed[1], delete_after=10.0)
        else:
            pass
    
    @commands.command(name='help.anim')
    async def help_anim(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()
            
            embed = make_embed(
                title='Animated Text Commands', 
                values=[('Command List', '''
**911** | Boom
**cum** | Yucky
            ''', False)] )
            
            await ctx.send(embed=embed[1], delete_after=10.0) if embed[0] else await ctx.send(embed[1], delete_after=10.0)
        else:
            pass
    
    @commands.command(name='help.nsfw')
    async def help_nsfw(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()
            
            embed = make_embed(
                title='NSFW Commands', 
                values=[('Command List', '''
**titties** | Sends some titties
**ass** | Sends some delicious booty
**pussy** | Sends some pussy
**hentai** | Sends some hentai
**r34 <query>** | Does some Rule 34 digging
**kiss <user>** | Kisses a user
**fuck <user>** | Fucks a user
**hold <user>** | Hold hands, very lewd!
**neko** | Sends a NSFW Neko image
**futa** | Ew
            ''', False)] )
            
            await ctx.send(embed=embed[1], delete_after=10.0) if embed[0] else await ctx.send(embed[1], delete_after=10.0)
        else:
            pass

    @commands.command(name='help.music')
    async def help_music(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()
            
            embed = make_embed(
                title='Music Commands', 
                values=[('Command List', '''
**play <url>** | Plays a song
**search <query>** | Searchs for a song
**queue** | Displays the music queue
**clearqueue** | Clears the queue
**stop** | Stops playing music
            ''', False)] )
            
            await ctx.send(embed=embed[1], delete_after=10.0) if embed[0] else await ctx.send(embed[1], delete_after=10.0)
        else:
            pass

    @commands.command(name='help.hecker')
    async def help_hecker(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()
            
            embed = make_embed(
                title='Hecker Commands', 
                values=[('Command List', '''
**tokeninfo <token>** | Gets info from token
**tokenfuck <token>** | RIP token lel
**ping <host>** | ICMP pings a host
**tcpping <host>** | TCP pings a host
**pscan <host>** | Port scans a host
**geo <ip>** | Performs a IP lookup
**isup <url>** | Checks if a site is up
**whflood <webhook> <message> <amount>** | Floods a webhook
**virustotal <file>** | Checks the file on virustotal
            ''', False)] )
            
            await ctx.send(embed=embed[1], delete_after=10.0) if embed[0] else await ctx.send(embed[1], delete_after=10.0)
        else:
            pass
    
    @commands.command(name='help.abuse')
    async def help_abuse(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()
            
            embed = make_embed(
                title='Abuse Commands', 
                values=[('Command List', '''
**nitrosniper <on/off>** | Enable/Disables nitro sniper
**autodisboard <on/off>** | Enable/Disables automated disboard messager
**autodankmemer <on/off>** | Enable/Disables dank memer farmer
            ''', False)] )
            
            await ctx.send(embed=embed[1], delete_after=10.0) if embed[0] else await ctx.send(embed[1], delete_after=10.0)
        else:
            pass
    
    @commands.command(name='help.raid')
    async def help_raid(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()
            
            embed = make_embed(
                title='Raid Commands', 
                values=[('Command List', '''
**nuke** | Nukes the server
**kickall** | Kicks everyone
**banall** | Bans everyone
**delroles** | Deletes every role
**delchannels** | Deletes every channel
**delemojis** | Deletes every emoji
**delinvite** | Deletes every invite
**join <tokens.txt> <invite>** | Makes tokens join a server
**raid <tokens.txt> <message>** | Spams messages using tokens
            ''', False)] )
            
            await ctx.send(embed=embed[1], delete_after=10.0) if embed[0] else await ctx.send(embed[1], delete_after=10.0)
        else:
            pass
    
    @commands.command(name='help.copypasta')
    async def help_copypasta(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()
            
            embed = make_embed(
                title='Copypasta Commands', 
                values=[('Command List', '''
**thefuckdidyousay** | Sends the "the fuck you just say about me" copypasta
**notarealgamer** | Sends the "No, you’re NOT a real gamer" copypasta
**gfapplications** | Sends a "Girlfriend Application"
**notarealwoman** | Sends the copypasta hated by transgenders lol
**veganejaculation** | I have no idea how to explain this
**yaoifangirl** | This makes you look like a retard
**titanfallreference** | This makes you look stupid too
**chinesecommunistparty** | Idk how to explain this (杀了我)
**okand** | Finally a response to "Ok, and?"
**analsquirting** | 😐
**dreamphobic** | Yeah idk
**daddieslittletidepod** | If i see you use this, prepare to get ur kneecaps broken
**donda** | Donda
**itouchedgrass** | OMG I TOUCHED GRASS
**gotthewholechatlaughing** | Damn bro, you got the whole chat laughing 😐😐😐😐😐
            ''', False)] )
            
            await ctx.send(embed=embed[1], delete_after=10.0) if embed[0] else await ctx.send(embed[1], delete_after=10.0)
        else:
            pass
    
    @commands.command(name='help.misc')
    async def help_misc(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()
            
            embed = make_embed(
                title='Misc Commands', 
                values=[('Command List', '''
Coming soon.
            ''', False)] )
            
            await ctx.send(embed=embed[1], delete_after=10.0) if embed[0] else await ctx.send(embed[1], delete_after=10.0)
        else:
            pass

def setup(bot):
    bot.add_cog(help_cog(bot))