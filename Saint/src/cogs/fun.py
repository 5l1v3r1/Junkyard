import asyncio, discord, json
from discord.ext import commands
from random import uniform, choice, randint

from src.utils import *
from src.config import *

class cog(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases=['help.fun', 'h.fun', 'commands.fun'])
    async def help(self, ctx) -> None:    
        '''
        await help_fun(context object) -> None

        about: Shows the fun commands
        syntax: <prefix>help.fun
        aliases: help.fun, h.fun, commands.fun
        returns: The fun commands

        :returns None: Nothing
        '''

        if self.client.user.id == ctx.message.author.id:
            pref = Configuration().prefix
            help_msg = Utils().ansify([
                f'$(cyan) - $(reset)Fun commands',
                f'$(lcyan) - $(reset){pref}8ball                : Answers with messages such as "yes", "no", "not too sure", "maybe"',
                f'$(lcyan) - $(reset){pref}leetspeak <message>  : M4K3S Y0UR M3SS4G3S M0R3 L33T',
                f'$(lcyan) - $(reset){pref}rainbowify <message> : Makes your text GAY',
                f'$(lcyan) - $(reset){pref}zoomify <message>    : Makes your text cool on god fr fr, no cap',
                f'$(lcyan) - $(reset){pref}ghostping <user>     : Ghostpings the specified user',
                f'$(lcyan) - $(reset){pref}meme                 : Grabs a random meme from reddit',
                f'$(lcyan) - $(reset){pref}yomama               : Gets a random "Yo mama" meme',
                f'$(lcyan) - $(reset){pref}dadjoke              : Gets a random dad joke',
                f'$(lcyan) - $(reset){pref}fakehack <user>      : Hacks the root kernel chain of the specified user',
                ], 
                fakeshell=True, 
                user=ctx.message.author, 
                message='help.fun'
            )

            await Utils().send_msg(ctx, help_msg, uniform(15,25))
        else:
            Utils().pprint(f'{ctx.message.author}/{ctx.message.author.id} tried executing a Saint command')
    
    @commands.command(aliases=['8ball', 'eightball'])
    async def _8ball(self, ctx) -> None:    
        '''
        await _8ball(context object) -> None

        about: Shows the fun commands
        syntax: <prefix>8ball
        aliases: 8ball, eightball
        returns: A random message

        :returns None: Nothing
        '''

        if self.client.user.id == ctx.message.author.id:
            rand_msg = choice([
            'As I see it, yes.',
            'As I see it, no.',
            'Ask again later.',
            'Better not tell you now.',
            'Cannot predict now.',
            'Concentrate and ask again.',
            'Don\'t count on it.',
            'It is certain.',
            'It is decidedly so.',
            'Most likely.',
            'My reply is no.',
            'My sources say no.',
            'Outlook not so good.',
            'Outlook good.',
            'Reply hazy, try again.',
            'Signs point to yes.',
            'Very doubtful.',
            'Without a doubt.',
            'Yes.',
            'No.',
            'Maybe.',
            '¯\\_(ツ)_/¯',
            'For sure.',
            'Nah i don\'t think so.',
            'I have no idea.'
            'Yes - definitely.',
            'For sure',
            'You may rely on it',
            'Hmm, i have no idea actually',
            'Yes on god fr fr'
            ])

            await Utils().send_msg(ctx, rand_msg, False)
        else:
            Utils().pprint(f'{ctx.message.author}/{ctx.message.author.id} tried executing a Saint command')
    
    @commands.command(aliases=['leetspeak', 'leetify'])
    async def leetspeak(self, ctx, *, message) -> None:    
        '''
        await leetspeak(context object, message) -> None

        about: Makes your text 1337
        syntax: <prefix>leetspeak <text>
        aliases: leetspeak, leetify
        returns: Original message, but M0R3 L33T

        :returns None: Nothing
        '''

        if self.client.user.id == ctx.message.author.id:

            leet_msg = message
            for normal, leet in {
                    'a':'4', 'A':'4',
                    'e':'3', 'E':'3',
                    'i':'1', 'I':'1',
                    'o':'0', 'O':'0',
                }.items():
                leet_msg = leet_msg.replace(normal, leet)

            await Utils().send_msg(ctx, leet_msg, False)
        else:
            Utils().pprint(f'{ctx.message.author}/{ctx.message.author.id} tried executing a Saint command')
    
    @commands.command(aliases=['rainbowify', 'gayify'])
    async def rainbowify(self, ctx, *, message) -> None:    
        '''
        await rainbowify(context object, message) -> None

        about: Makes your text GAY
        syntax: <prefix>rainbowify <text>
        aliases: rainbowify, gayify
        returns: Original message, but GAY

        :returns None: Nothing
        '''

        if self.client.user.id == ctx.message.author.id:
            await Utils().send_msg(ctx, Utils().rainbowify(message), False)
        else:
            Utils().pprint(f'{ctx.message.author}/{ctx.message.author.id} tried executing a Saint command')
    
    @commands.command(aliases=['zoomify', 'retardify'])
    async def zoomify(self, ctx, *, message) -> None:    
        '''
        await zoomify(context object, message) -> None

        about: Makes your text cool on god fr fr no cap
        syntax: <prefix>zoomify <text>
        aliases: zoomify, retardify
        returns: Original message, but cooler fr fr

        :returns None: Nothing
        '''

        if self.client.user.id == ctx.message.author.id:
            zoomer_msg = message

            for normal, retarded in {
                    'i swear': choice(['on god', 'no cap']),
                    'for real': 'fr fr',
                    'not lying': 'no cap',
                    'good': 'bussin\'',
                    'racist': 'based' # lol
                }.items():
                zoomer_msg=zoomer_msg.replace(normal, retarded)

            await Utils().send_msg(ctx, zoomer_msg, False)
        else:
            Utils().pprint(f'{ctx.message.author}/{ctx.message.author.id} tried executing a Saint command')
    
    @commands.command(name='ghostping')
    async def ghostping(self, ctx, *, user: discord.User) -> None:    
        '''
        await ghostping(context object, user) -> None

        about: Pings the specified user, then removes the message
        syntax: <prefix>ghostping <user>
        aliases: ghostping
        returns: Nothing

        :returns None: Nothing
        '''

        if self.client.user.id == ctx.message.author.id:
            msg = await ctx.send(f'<@{user}> nibba you got ghostpinged')

            await asyncio.sleep(uniform(0,1)) # waits a few nano seconds before removing the message

            await msg.delete()
        else:
            Utils().pprint(f'{ctx.message.author}/{ctx.message.author.id} tried executing a Saint command')
    
    @commands.command(aliases=['meme','getmeme','grabmeme','meem'])
    async def meme(self, ctx) -> None:    
        '''
        await meme(context object) -> None

        about: Grabs a meme from reddit
        syntax: <prefix>meme
        aliases: meme, getmeme, grabmeme, meem
        returns: Nothing

        :returns None: Nothing
        '''

        if self.client.user.id == ctx.message.author.id:
            req = json.loads(Utils().make_request('GET', 'https://meme-api.herokuapp.com/gimme', False).text)

            await Utils().send_msg(ctx, req['url'], False)
        else:
            Utils().pprint(f'{ctx.message.author}/{ctx.message.author.id} tried executing a Saint command')
    
    @commands.command(aliases=['yomama','joemama','yoommaa','yomamajoke'])
    async def yomama(self, ctx) -> None:    
        '''
        await yomama(context object) -> None

        about: Yoo mama so tech illiterate, she thanks google for the cookies!
        syntax: <prefix>yomama
        aliases: yomama, joemama, yoomama, yomamajoke
        returns: Yo mama joke

        :returns None: Nothing
        '''

        if self.client.user.id == ctx.message.author.id:
            req = json.loads(Utils().make_request('GET', 'https://api.yomomma.info/', False).text)

            await Utils().send_msg(ctx, req['joke'], False)
        else:
            Utils().pprint(f'{ctx.message.author}/{ctx.message.author.id} tried executing a Saint command')
    
    @commands.command(name='dadjoke')
    async def dadjoke(self, ctx) -> None:    
        '''
        await dadjoke(context object) -> None

        about: Dad jokes are the best, not gonna lie
        syntax: <prefix>dadjoke
        aliases: dadjoke
        returns: The joke

        :returns None: Nothing
        '''

        if self.client.user.id == ctx.message.author.id:
            req = json.loads(Utils().make_request('GET', 'https://icanhazdadjoke.com/', False).text)

            await Utils().send_msg(ctx, req['joke'], False)
        else:
            Utils().pprint(f'{ctx.message.author}/{ctx.message.author.id} tried executing a Saint command')
    
    @commands.command(aliases=['fakehack','hack','haxor','heck'])
    async def fakehack(self, ctx, user) -> None:    
        '''
        await fakehack(context object, username) -> None

        about: Pwns the specified users root kernel chain
        syntax: <prefix>fakehack <username>
        aliases: fakehack, hack, haxor, heck
        returns: Le epic pwnage

        :returns None: Nothing
        '''

        if self.client.user.id == ctx.message.author.id:
            user = await self.client.fetch_user(user.replace('<@!', '').replace('>', ''))
            user_name = str(user).split("#")[0]

            mail_providers = ['protonmail.com', 'keemail.me', 'gmail.com', 'mail.ru', 'yahoo.com', '420blaze.it', 'cumallover.me', 'cocaine.ninja', 'waifu.club', 'dicksinhisan.us', 'wants.dicksinhisan.us', 'fbi.gov']
            email = f'{user_name}{str(Utils().randint(randint(4,10)))}@{choice(mail_providers)}'

            passwords = [
                'sm4llw33n31',
                'bestpasswordnocap',
                'password1',
                'root',
                'nexusisdaddy',
                'saint',
                'saintbestselfbot',
                Utils().randstr(randint(2,20)),
                'password1234321'
            ]

            rand_cve = f'CVE-{str(randint(1995, 2021))}-{str(Utils().randint(4))}'
            rand_ip = '.'.join([str(randint(1,255)) for _ in range(4)])

            msgs = [ # TODO: make the % ints random, makes it feel much more "alive"
                '**[**1%**]** Scanning system for vulnerabilities.',
                f'**[**5%**]** Vulnerability found: `{rand_cve}`.',
                f'**[**7%**]** Exploiting system using `{rand_cve}`.',
                '**[**11%**]** Malware installed on system.',
                f'**[**17.2%**]** `Hack{Utils().randstr(randint(2,7))}.js` injected into Discord.',
                f'**[**20.9%**]** Brute forcing account',
                f'**[**25%**]** Downloading RAM and upgrading CPU to speed up bruteforcing.',
                f'**[**30.6%**]** Brute force success.\nEmail: `{email}`\nPassword: `{choice(passwords)}`',
                '**[**39.2%**]** Logging in.',
                f'**[**45%**]** Changing biography to `Hacked by {self.client.user}`',
                f'**[**53.9%**]** Grabbing IP.',
                f'**[**69%**]** IP found: {rand_ip}',
                f'**[**77.1%**]** DDoS\'ing IP using {choice(["LOIC","HOIC","UDP Unicorn","Figlet","HULK","Cerberus","Amyntas"])}.',
                f'**[**80%**]** IP is offline.',
                f'**[**88.4%**]** Logging out of account.',
                f'**[**94%**]** Clearing traces.',
                f'**[**96.7%**]** Removing system logs.',
            ]

            await ctx.send(f'**[**0%**]** Hack on {user} started.')
            for msg in msgs:
                await Utils().send_msg(ctx, msg, False)
            
            await Utils().send_msg(ctx, f'**[**100%**]** Hack on {user} completed.', False)
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