import requests, json, asyncio, string
from Sucuri.util import *
from discord.ext import commands
from random import choice, randint

class fun_cog(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(name='meme')
    async def memecmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()
            
            req = requests.get('https://meme-api.herokuapp.com/gimme')
            data = json.loads(req.text)

            embed = make_embed(
                title=data['title'], 
                title_prefix = False,
                description=f'Taken from **r/{data["subreddit"]}**, posted by **u/{data["author"]}**',
                image=data['url'],
                footer='Powered by Reddit',
                footer_icon='https://www.redditstatic.com/desktop2x/img/favicon/favicon-32x32.png'
            )

            await ctx.send(embed=embed[1], delete_after=4.0) if embed[0] else await ctx.send(embed[1], delete_after=4.0)
        else:
            pass
    
    @commands.command(name='joke')
    async def jokecmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()
            
            req = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})
            joke = json.loads(req.text)['joke']

            return await ctx.send(joke)
        else:
            pass

    @commands.command(name='yomama')
    async def yomamacmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()
            
            req = requests.get('https://api.yomomma.info/')
            joke = json.loads(req.text)['joke']

            return await ctx.send(joke)
        else:
            pass
    
    @commands.command(name='8ball')
    async def eightballcmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()
            
            array = [
                'As I see it, yes.',
                'Ask again later.',
                'Better not tell you now.',
                'Cannot predict now.',
                'Concentrate and ask again.',
                'Don’t count on it.',
                'It is certain.',
                'It is decidedly so.',
                'Most likely.',
                'My reply is no.',
                'My sources say no.',
                'Outlook is not so good.',
                'Outlook seems to look good.',
                'Reply hazy, try again.',
                'Signs point to yes.',
                'Very doubtful.',
                'Without a doubt.',
                'Yes.',
                'No.',
                'Maybe.',
                '¯\_(ツ)_/¯',
                'For sure.',
                'Nah i don\'t think so.',
                'I have no idea.'
                'Yes – definitely.',
                'You may rely on it',
            ]

            return await ctx.send(choice(array))
        else:
            pass    

    @commands.command(name='quote')
    async def quotecmd(self, ctx):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()
            
            rand_int = randint(0, 1)
            if rand_int == 0:
                req = requests.get('https://api.quotable.io/random')
                quote = json.loads(req.content)

                return await ctx.send( f'{quote["content"]} - {quote["author"]}' )
            else:
                return await ctx.send( random_quote() )

        else:
            pass
    
    @commands.command(aliases=['heck', 'hack'])
    async def heckcmd(self, ctx, user):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()
            
            user = await self.client.fetch_user(user.replace('<@!', '').replace('>', ''))
            user_name = str(user).split("#")[0]

            mail_providers = ['protonmail.com', 'keemail.me', 'gmail.com', 'yahoo.com', '420blaze.it', 'cumallover.me', 'cocaine.ninja', 'waifu.club', 'dicksinhisan.us', 'wants.dicksinhisan.us']
            emails = [
                f'{user_name}loves@co.ck',
                f'{user_name}{"".join(str(randint(0, 9)) for _ in range(randint(5, 10)))}@{choice(mail_providers)}',
                f'{user_name}@fbi.gov'
            ]

            passwords = [
                'sm4llw33n31',
                'bestpasswordnocap',
                'password1',
                'root',
                'nexusisdaddy',
                'sucuri'
                ''.join(choice(string.printable) for _ in range(randint(4,20)))
            ]

            rand_cve = f'CVE-{str(randint(1995, 2021))}-{"".join(str(randint(0, 9)) for _ in range(4))}'
            rand_ip = f'{str(randint(0, 256))}.{str(randint(0, 256))}.{str(randint(0, 256))}.{str(randint(0, 256))}'

            msgs = [
                '**[**1%**]** Scanning system for vulnerabilities.',
                f'**[**5%**]** Vulnerability found: `{rand_cve}`.',
                f'**[**7%**]** Exploiting system using `{rand_cve}`.',
                '**[**11%**]** Malware installed on system.',
                '**[**17.2%**]** `Hack.js` injected into Discord.',
                f'**[**20.9%**]** Brute forcing account',
                f'**[**30%**]** Brute force success.\nEmail: `{choice(emails)}`\nPassword: `{choice(passwords)}`',
                '**[**39.2%**]** Logging in.',
                f'**[**45%**]** Changing bio to `Hacked by {self.client.user}`',
                f'**[**53.9%**]** Grabbing IP.',
                f'**[**69%**]** IP found: {rand_ip}',
                f'**[**77%**]** DDoS\'ing IP using LOIC.',
                f'**[**80%**]** IP is offline.',
                f'**[**88.7%**]** Logging out of account.',
                f'**[**94%**]** Clearing traces.',
            ]

            message = await ctx.send(f'**[**0%**]** Hack on {user} started.')
            for msg in msgs:
                await asyncio.sleep(float(f'2.{randint(2, 9)}'))
                await message.edit(content=msg)
            
            await asyncio.sleep(float(f'2.{randint(2, 9)}'))
            await message.edit(content=f'**[**100%**]** Hack on {user} completed.')
        else:
            pass

def setup(bot):
    bot.add_cog(fun_cog(bot))