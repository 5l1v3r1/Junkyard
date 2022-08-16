import asyncio, requests, os, sys, ctypes, contextlib, glob, time, socket
from datetime import datetime, timedelta
from colorama import Fore, init
from random import uniform, choice, shuffle

from src.config import *
from src.core import *

with contextlib.redirect_stdout(None):
    import pygame # because pygame is a dick and prints a banner when getting imported, this is the only way

# initialize colorama
init()

class Utils():
    def __init__(self):
        self.didyouknows = [
            'The closest living relative to humans are chimpanzees, bonobos, and gorillas. We share between 98 and 99.6% of DNA with these species. Gorillas can even catch colds from humans.',
            'Most mammals have reproductive cycles. However, only humans, humpback whales, and elephants experience menopause.',
            'To escape a crocodiles jaw, push your thumb into its eyeballs.',
            'Cats have only lived with people for about 7,000 years. Compared to dogs, whose domestication may have begun as early as 25,000 years ago.',
            'Most of the Earth\'s longest-surviving species are found in the ocean. While cyanobacterias are technically the oldest living organisms on Earth, having appeared 2.8 billion years ago, the ocean sponge has also been on Earth for 580 million years, and jellyfish have been here for 550 million years.',
            '85% of plant life is found in the ocean.',
            'The Amazon rainforest is an amazing place. The Amazon produces over 20% of the world\'s oxygen, and contains more than half of the world\'s species of plants, animals, and insects.',
            'Additionally, up to 73 million sharks per year die due to shark finning, where fishermen catch the shark, cut off its fins, and throw the still-living shark back into the water. Many countries have imposed full or partial bans on finning, mainly that the sharks need to arrive onshore with fins attached. A few countries, notably Israel, Egypt, Ecuador, Honduras, Brunei and the Maldives, have total shark fishing bans.',
            'Many animals exhibit high levels of emotional intelligence. For example, cows form bonds akin to friendships, and often have a “best friend,” and Gentoo Penguins bring a potential mate a pebble to “propose.”',
            'Dog noses are as unique as a human fingerprint.',
            'Paul Revere famously yelled “The British Are Coming!\' at the start of the American Revolution. Or...not. Revere was just one member of a secret militia operation to warn other militias about the British troops. A lot of colonial Americans still considered themselves British at that time, and would have likely been confused if he\'d actually said or shouted this.',
            'Many people came forward pretending to be Grand Duchess Anastasia after the Czar fell in the Russian Revolution. But Anastasia impersonators came from a long tradition of royal imposters; Louis XVII of France died during the French Revolution, and years later when the country was discussing a revival of the monarchy, over 100 people came forward claiming to be the prince.',
            'There were more than 600 plots to kill Fidel Castro. Plots were crafted by a variety of enemies, and even included an exploding cigar.',
            'The patent for the first car was filed in 1886 by Karl Benz for a gas-powered, 3-wheel motor car.',
            'Hitler, Mussolini, and Stalin were all nominated for the Nobel Peace Prize. While not all nominees since have been controversy-free, whoever nominated these three probably regretted it.',
            'We know now that the bubonic plague was in part spread by rats. But before the plague, Pope Gregory IX declared that cats were associated with devil worship and ordered that they be exterminated. Unfortunately, people listened and as a result the rat population flourished. It is believed that the increased rat population contributed to the plague. (Ahem, actions have consequences, and don\'t mess with cats)',
            'Jeanette Rankin was the first woman elected to Congress in 1916, 4 years before women had the right to vote. She was a pacifist from Montana, and was elected a second time in 1941. Both times, she voted no in regards to entering World Wars 1 and 2.',
            'Seven of the 10 deadliest wars in history have taken place in China. The Taping Rebellion had twice as many deaths as World War 1.',
            'Pineapples are all the rage now, but they were also a fad in the UK in the 1700s. People carried them around to show their wealth and status, and people decorated their homes with pineapples. You could even rent a pineapple as an accessory.',
            '20% of the Earth\'s oxygen is produced by the Amazon rainforest.',
            'The Great Barrier Reef is the largest living structure on Earth at 2,000 kilometers long.',
            'Most of us are familiar with the three states of matter: solid, liquid, and gas. But there are actually two dozen known states of matter. Plasma is one example, but scientists have also found other states of matter that only occur under certain conditions.',
            'When helium is cooled to absolute zero (-460 degrees Fahrenheit) it becomes a liquid and starts flowing upward, against gravity.',
            'The moon once had an atmosphere. Volcanic eruptions on the moon released trillions of tons of gas into the air, which created an atmosphere. The gases eventually became lost to space.',
            'When Einstein posed his Theory of Relativity, he didn\'t have the resources to prove this theory. However, the theory has been proven correct several times over the years. Most recently in 2018, scientists saw that as a black hole distorted light waves from a nearby star in a way that agrees with the theory.',
            'Scientists have answered the question “what comes first the chicken or the egg?” The chicken came first because the egg shell contains a protein that can only be made from a hen.',
            'It is mainly men who experience colorblindness. 1/20 men experience color blindness as opposed to 1/200 women.',
            'Scientists were called “natural philosophers” until the 17th century because science didn\'t exist as a concept.',
            'Natalie Portman is a Harvard graduate and has had papers published in two scientific journals, one of which was when she was in high school.',
            'Some of Neil Patrick Harris\' characters are magicians, and so is the actor. His children\'s book series, The Magic Misfits, is also about a group of magicians.',
            'Colin Kaepernick got a pet tortoise at age 10, that fit in a shoebox. Today, the tortoise is 115 pounds and may live to be 135 years old.',
            'The Doctor Suess book Green Eggs and Ham uses only 50 different words. Doctor Suess wrote the book on a bet from his publisher that he couldn\'t write a book with fewer words than The Cat in the Hat, which has 225.',
            'Woody Harrelson\'s father was a hitman, who left the family when the actor was young. Woody didn\'t find out about his father\'s criminal activity until he heard a radio report on his trial.',
            'Dr. Martin Luther King was a Star Trek fan. He convinced Nichelle Nichols, one of the first black women featured on a major TV show, not to quit, arguing that her role was making history. Mae Jamison, the first black woman to travel into space, later cited Nichols as one of her inspirations.',
            'Queen Elizabeth II is the longest-serving British monarch. She has been on the throne for 67 years. The 93 year old queen\'s heir is currently her son Charles, who is 70.',
            'Isaac Asimov published so many books, essays, short fiction, and non-fiction, that if you read one per week it would take you 9 years to read all of his work.',
            'In 2018, 50.3% of eligible voters turned out to vote. This was the highest turnout for a midterm election since 2018. Also in 2018, 16% of voters said it was the first time they\'d voted in a midterm election.',
            'About ⅓ of Americans think the president affects their personal lives, and 63% say he affects the country\'s mood.',
            'The U.S. spends more on defense than the other 7 countries combined. Last year, the U.S. spent $649 billion, while China, Saudi Arabia, India, France, Russia, the U.K. and Germany spent a combined $609 billion',
            'Any person born in the United States or to U.S. citizen parents is also a U.S. citizen.',
            'The U.S. Constitution was signed on September 17th, 1787. It was meant not to “grant” rights, but to protect the rights people were born with.',
            'Although the U.S. has a two party system, there are some other third parties. Notable ones now are the tea party and the green party, but the U.S. once had fringe parties like the Bull and Moose party.',
            'Americans throw out 4.4 pounds of trash daily.'
        ]
    
    ### ----SYNCHRONOUS FUNCTIONS---- ###

    def get_uptime(self, raw=False) -> str | dict:
        '''
        get_uptime() -> str | dict

        Gets the bots uptime, not to be confused with `get_contime()`

        :param raw bool: Wether to return a raw dictionary
        :returns str or dict: Formatted string, or a dictionary holding the  weeks, days, hours, minutes seconds and remainder
        '''

        hours, remainder = divmod(int((datetime.now() - Core.started_at).total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        weeks, days = divmod(days, 7)

        if raw:
            return {'weeks': weeks, 'days': days, 'hours': hours, 'minutes': minutes, 'seconds': seconds, 'remainder': remainder}
        else:
            final = f'{str(seconds)} second{"s"if seconds!=1 else""}'
            if minutes != 0: final = f'{str(minutes)} minute{"s"if minutes!=1 else""}, {final}'
            if hours != 0: final = f'{str(hours)} hour{"s"if hours!=1 else""}, {final}'
            if days != 0: final = f'{str(days)} day{"s"if days!=1 else""}, {final}'
            if weeks != 0: final = f'{str(weeks)} week{"s"if weeks!=1 else""}, {final}'

            return final
    
    def get_contime(self, raw=False) -> str | dict:
        '''
        get_contime(raw) -> str | dict

        Gets the bots connection time, not to be confused with `get_uptime()`

        :param raw bool: Wether to return a raw dictionary
        :returns str or dict: Formatted string, or a dictionary holding the weeks, days, hours, minutes seconds and remainder
        '''

        hours, remainder = divmod(int((datetime.now() - Core.connected_at).total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        weeks, days = divmod(days, 7)

        if raw:
            return {'weeks': weeks, 'days': days, 'hours': hours, 'minutes': minutes, 'seconds': seconds, 'remainder': remainder}
        else:
            final = f'{str(seconds)} second{"s"if seconds!=1 else""}'
            if minutes != 0: final = f'{str(minutes)} minute{"s"if minutes!=1 else""}, {final}'
            if hours != 0: final = f'{str(hours)} hour{"s"if hours!=1 else""}, {final}'
            if days != 0: final = f'{str(days)} day{"s"if days!=1 else""}, {final}'
            if weeks != 0: final = f'{str(weeks)} week{"s"if weeks!=1 else""}, {final}'

            return final

    def load_cogs(self, client, _dir=os.path.join('src','cogs')) -> list:
        '''
        load_cogs(directory) -> list

        Loads all commands/cogs from a specific folder

        :param client discord.ext.commands.Bot: Client object
        :param _dir str: Directory to load from, defaults to /src/cogs
        :returns list: List of cogs that loaded without error
        '''

        loaded = []
        for file in glob.glob(os.path.join(_dir, '*')):
            if file.endswith('.py') and not '__' in file:
                loaded.append(file)

                client.load_extension(f'src.cogs.{file[:-3]}')
            
        return loaded

    def format(self, text) -> str:
        '''
        format(text to format) -> str

        Replaces certain placeholders in text

        :param text str: Text to format
        :returns str: The formatted string
        '''

        text=text
        token = Configuration().token; prefix = Configuration().prefix; theme = Configuration().theme
        for old, new in [
                ## --- bot/config info --- ##
                (['$(dev)', '$(author)', '$(creator)'], 'https://github.com/Nexuzzz'),
                (['$(repo)', '$(repository)'], 'https://github.com/Nexuzzzz/Saint'),
                ('$(token)', token if token else 'unknown'),
                ('$(prefix)', prefix if prefix else 'unknown'),
                ('$(theme)', theme if theme else 'unknown'),
                ('$(uptime)', self.get_uptime()),
                ('$(contime)', self.get_contime()),
                ('$(started_at)', Core.started_at.strftime("%d/%M/%Y %H:%M:%S")),
                ('$(connected_at)', Core.connected_at.strftime("%d/%M/%Y %H:%M:%S")),

                ## --- colors --- ##
                ('$(red)', Fore.RED),
                ('$(lred)', Fore.LIGHTRED_EX),
                ('$(blue)', Fore.BLUE),
                ('$(lblue)', Fore.LIGHTBLUE_EX),
                ('$(green', Fore.GREEN),
                ('$(lgreen)', Fore.LIGHTGREEN_EX),
                ('$(white', Fore.WHITE),
                ('$(cyan)', Fore.CYAN),
                ('$(lcyan)', Fore.LIGHTCYAN_EX),
                ('$(magenta)', Fore.MAGENTA),
                ('$(lmagenta)', Fore.LIGHTMAGENTA_EX),
                ('$(yellow)', Fore.YELLOW),
                ('$(lyellow)', Fore.LIGHTYELLOW_EX),
                ('$(reset)', Fore.RESET),

                ## --- system stuff --- ##
                ('$(os)', sys.platform),
                ('$(os_2)', sys.platform.capitalize()),
                ('$(now)', datetime.now().strftime("%d/%M/%Y %H:%M:%S")),
                ('$(cwd)', os.getcwd()),
                (['$(~/)', '$(~)', '$(home)'], os.path.expanduser('~')),
                ('$(pcname)', socket.gethostname()),

                ## ---  misc --- ##
                (['$(didyouknow)', '$(dyk)'], self.didyouknow()),
                (['$(didyouknow_2)', '$(dyk2)'], self.didyouknow(False)),
            ]:

            if type(old) == list:
                for x in old: 
                    text=text.replace(x, new)
            else:
                text=text.replace(old, new)
        
        return text

    def pprint(self, msg, add_time=True, icon='+', exit_after=False, dotted=False, dotted_delay=0.5) -> None:
        '''
        pprint(message, include timestamp in the displayed message) -> None

        Helper function that wraps around `print()`

        :param msg str: Message to display
        :param add_time bool: Wether to include a timestamp in the text
        :param icon str: Icon
        :param exit_after bool: Exit after sending a message
        :param dotted bool: Wether to add 3 dots after the message
        :param dotted_delay int or float: Delay between appending the dots, only works when "dotted" is set to True
        :returns None: Nothing
        '''

        msg = f'[ {icon} ] {msg}'
        if add_time:
            msg = f'[{datetime.now().strftime("%d/%M/%Y %H:%M:%S")}] {msg}'
        
        formatted = self.format(msg)
        if not dotted: print(formatted)
        else:
            for i in range(3):
                i+=1

                print(formatted+'.'*i, end='\r')
                time.sleep(dotted_delay)
        
            print('')

        if exit_after:
            try: sys.exit()
            except: os.kill(os.getpid(), 9)

    def didyouknow(self, include=True) -> str:
        '''
        didyouknow(include the message) -> str

        Returns a random "did you know?" fact

        :param include bool: Wether to include the message "Did you know? <fact here>"
        :returns str: The fact
        '''

        rand = choice(self.didyouknows)

        if include: return f'**Did you know?** ```\n{rand}\n```'
        else: return rand
    
    def make_request(self, method='GET', url='https://discordapp.com', use_token=True, headers=None, verify=False, timeout=(10, 20), proxies={'http':None, 'https':None}, allow_redirects=True) -> requests.Response | None:
        '''
        make_request(http method, url, headers, verify ssl cert, timeout, proxies, allow redirects) -> requests.Response or None

        Creates and sends a HTTP request using Requests

        :param method str: HTTP method
        :param url str: Url to send the request to
        :param use_token bool: If True "Configuration().token" will be passed in the Authorization, if False the "Authorization" header will be stripped
        :param headers dict or None: Headers to send, if None the default headers will be used
        :param verify bool: Wether to verify the SSL certificate of the remote url
        :param timeout int or tuple: (connection timeout, read timeout) or a single integer for both
        :param proxies dict: Proxies to use, set to None to disable proxies
        :param allow_redirects bool: Allow requests to follow redirects
        :returns requests.Response or None: The request response object, will be None if any exceptions occured
        '''

        if not headers:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
                'Authorization': Configuration().token if use_token else 'to strip, or not to strip. thats the question',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8,application/json',
                'Accept-Language': 'en-US,en;q=0.5',
                'Dnt': '1',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Sec-Gpc': '1',
                'Te': 'trailers'
            }

            if not use_token:
                del headers['Authorization']

        resp = None
        try:
            resp = requests.request(
                method, 
                url,
                headers=headers,
                verify=verify,
                timeout=timeout,
                proxies=proxies,
                allow_redirects=allow_redirects
            )
        except Exception:
            resp = None
        
        return resp
    
    def check_token(self) -> bool:
        '''
        check_token(token to check) -> bool

        Checks if the discord token set in the config, is a valid token

        :returns bool: True if the token is valid, False if not
        '''

        req = self.make_request('GET', 'https://discordapp.com/api/v9/users/@me')
        return req.status_code == 200 if req else False
    
    def clear(self) -> None:
        '''
        clear() -> None

        Clears the screen, duhh

        :returns None: Nothing
        '''

        if os.name == 'nt': os.system('cls')
        else: os.system('clear')
    
    def set_title(self, title) -> None:
        '''
        set_title(title text) -> None

        Sets the title, duhh

        :param title str: Title to set
        :returns None: Nothing
        '''

        title = self.format(title)

        try:
            if os.name == 'nt':
                try: ctypes.windll.kernel32.SetConsoleTitleW(title)
                except:  os.system(f'title {title}')
            else:
                try: sys.stdout.write(f'\x1b]2;{title}\x07')
                except: pass
        except:
            pass
    
    def play_sound(self, path) -> None:
        '''
        play_sound(file path to .wav file) -> None
        
        Plays a sound using PyGame's mixer module

        :param path str: Path to the .wav sound file
        :returns None: Nothing
        '''

        pygame.mixer.music.load(path)
        pygame.mixer.music.play(1)
    
    def rainbowify(self, text, colors=[Fore.RED,Fore.BLUE,Fore.GREEN,Fore.YELLOW,Fore.MAGENTA,Fore.WHITE,Fore.CYAN,Fore.LIGHTCYAN_EX,Fore.LIGHTBLUE_EX,Fore.LIGHTGREEN_EX,Fore.LIGHTMAGENTA_EX]) -> str:
        '''
        rainbowify(text, list of colors to pick from) -> str

        Makes text gay

        :param text str: Text to make gay
        :param colors list: List of ANSI escape sequences/color codes
        :returns str: Gay text
        '''

        text=self.format(text)

        shuffle(colors)

        gay = ''
        for char in text:
            gay += f'{choice(colors)}{char}{Fore.RESET}'
        
        return gay

    def ansify(self, text, fakeshell=False, user=None, message=None) -> str:
        '''
        ansify(text to convert, put a fake shell prompt on top, user to put in the prompt, message to put in the prompt) -> str

        Turns the specified text into a format used by Discords parser

        :param text str or list: Text to convert, if type is list it will join them with a newline
        :param fakeshell bool: Put a fake prompt/shell on top
        :param user str: User to put in the prompt
        :param message str: Text to put in the prompt
        :returns str: Converted text
        '''

        # just replace some things in the text, such as placeholders
        if type(text) == list:
            text = '\n'.join(text)

        text = self.format(text)
        result = f'```ansi'
        if fakeshell:
            result += f'\n{user}[0;34m@[0msaint:~$ {message}\n'

        result += f'\n{text}\n'
        result += '```'

        return result
    
    def randstr(self, length, chars='qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789') -> str:
        '''
        randstr(length, characters) -> str

        Builds a random string

        :param length int: Length of the final string
        :param chars str or list: List of characters to use
        :returns str: The created string
        '''

        return ''.join([choice(chars) for _ in range(length)])
    
    def randint(self, length, ints='0123456789') -> int:
        '''
        randint(length, integers) -> int

        Builds a random chunk of integers

        :param length int: Length of the chunk
        :param ints str or list: List of integers to use
        :returns int: Big ass integer chunk
        '''

        return int(''.join([choice(ints) for _ in range(length)]))
    
    ### ----ASYNCHRONOUS FUNCTIONS---- ###

    async def send_msg(self, ctx, message, edit_after, stealthy=True) -> None:
        '''
        send_msg(context object, message, edit after x seconds) -> None

        Overwrites the command message (eg; ./help) with the command output, then overwrites it with a random did you "know?" fact

        :param ctx discord.ctx: Discord context, usually passed in the function as an argument
        :param message str: Text to send
        :param edit_after int or float or bool: Seconds to wait before editing the message, if set to False nothing is overwritten
        :param stealthy bool: Add some extra sleeps to prevent macro detections
        :returns None: Nothing
        '''

        if stealthy:
            await asyncio.sleep(uniform(2, 5)) # wait between 2-5 seconds

        #await ctx.message.edit(content=message) # overwrite the previous message with our new message
        print(self.format(message))

        if stealthy:
            await asyncio.sleep(uniform(4, 7)) # wait between 4-7 seconds

        if edit_after:
            await asyncio.sleep(edit_after) # remove the message after the specified seconds
            await ctx.message.edit(content=self.didyouknow()) # overwrite it with a random fact