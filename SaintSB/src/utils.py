import click
import requests
import sys, os
import ctypes
import json
import contextlib
import psutil
import time
from colorama import Fore
from discord import Embed
from random import choice
from datetime import datetime
from pypresence import Presence, InvalidID, InvalidPipe

''' Stealthy import '''
with contextlib.redirect_stdout(None):
    import pygame

red = Fore.RED
blue = Fore.BLUE
lblue = Fore.LIGHTBLUE_EX
green = Fore.GREEN
black = Fore.BLACK
grey = Fore.LIGHTBLACK_EX
white = Fore.WHITE
reset = Fore.RESET

def outputstr(author, cli, output):
    return f'''```ansi
{author}[0;34m@[0msaint ~> {cli}
[1;30m[[0;34m>[1;30m][0m {output}
```'''

def didyouknow(): # just made to return random facts
    didyouknows = [
        'The closest living relative to humans are chimpanzees, bonobos, and gorillas. We share between 98 and 99.6% of DNA with these species. Gorillas can even catch colds from humans.',
        'Most mammals have reproductive cycles. However, only humans, humpback whales, and elephants experience menopause.',
        'To escape a crocodiles jaw, push your thumb into its eyeballs.',
        'Cats have only lived with people for about 7,000 years. Compared to dogs, whose domestication may have begun as early as 25,000 years ago.',
        'Most of the Earth’s longest-surviving species are found in the ocean. While cyanobacterias are technically the oldest living organisms on Earth, having appeared 2.8 billion years ago, the ocean sponge has also been on Earth for 580 million years, and jellyfish have been here for 550 million years.',
        '85% of plant life is found in the ocean.',
        'The Amazon rainforest is an amazing place. The Amazon produces over 20% of the world’s oxygen, and contains more than half of the world’s species of plants, animals, and insects.',
        'Additionally, up to 73 million sharks per year die due to shark finning, where fishermen catch the shark, cut off its fins, and throw the still-living shark back into the water. Many countries have imposed full or partial bans on finning, mainly that the sharks need to arrive onshore with fins attached. A few countries, notably Israel, Egypt, Ecuador, Honduras, Brunei and the Maldives, have total shark fishing bans.',
        'Many animals exhibit high levels of emotional intelligence. For example, cows form bonds akin to friendships, and often have a “best friend,” and Gentoo Penguins bring a potential mate a pebble to “propose.”',
        'Dog noses are as unique as a human fingerprint.',
        'Paul Revere famously yelled “The British Are Coming!’ at the start of the American Revolution. Or...not. Revere was just one member of a secret militia operation to warn other militias about the British troops. A lot of colonial Americans still considered themselves British at that time, and would have likely been confused if he’d actually said or shouted this.',
        'Many people came forward pretending to be Grand Duchess Anastasia after the Czar fell in the Russian Revolution. But Anastasia impersonators came from a long tradition of royal imposters; Louis XVII of France died during the French Revolution, and years later when the country was discussing a revival of the monarchy, over 100 people came forward claiming to be the prince.',
        'There were more than 600 plots to kill Fidel Castro. Plots were crafted by a variety of enemies, and even included an exploding cigar.',
        'The patent for the first car was filed in 1886 by Karl Benz for a gas-powered, 3-wheel motor car.',
        'Hitler, Mussolini, and Stalin were all nominated for the Nobel Peace Prize. While not all nominees since have been controversy-free, whoever nominated these three probably regretted it.',
        'We know now that the bubonic plague was in part spread by rats. But before the plague, Pope Gregory IX declared that cats were associated with devil worship and ordered that they be exterminated. Unfortunately, people listened and as a result the rat population flourished. It is believed that the increased rat population contributed to the plague. (Ahem, actions have consequences, and don’t mess with cats)',
        'Jeanette Rankin was the first woman elected to Congress in 1916, 4 years before women had the right to vote. She was a pacifist from Montana, and was elected a second time in 1941. Both times, she voted no in regards to entering World Wars 1 and 2.',
        'Seven of the 10 deadliest wars in history have taken place in China. The Taping Rebellion had twice as many deaths as World War 1.',
        'Pineapples are all the rage now, but they were also a fad in the UK in the 1700s. People carried them around to show their wealth and status, and people decorated their homes with pineapples. You could even rent a pineapple as an accessory.',
        '20% of the Earth’s oxygen is produced by the Amazon rainforest.',
        'The Great Barrier Reef is the largest living structure on Earth at 2,000 kilometers long.',
        'Most of us are familiar with the three states of matter: solid, liquid, and gas. But there are actually two dozen known states of matter. Plasma is one example, but scientists have also found other states of matter that only occur under certain conditions.',
        'When helium is cooled to absolute zero (-460 degrees Fahrenheit) it becomes a liquid and starts flowing upward, against gravity.',
        'The moon once had an atmosphere. Volcanic eruptions on the moon released trillions of tons of gas into the air, which created an atmosphere. The gases eventually became lost to space.',
        'When Einstein posed his Theory of Relativity, he didn’t have the resources to prove this theory. However, the theory has been proven correct several times over the years. Most recently in 2018, scientists saw that as a black hole distorted light waves from a nearby star in a way that agrees with the theory.',
        'Scientists have answered the question “what comes first the chicken or the egg?” The chicken came first because the egg shell contains a protein that can only be made from a hen.',
        'It is mainly men who experience colorblindness.1/20 men experience color blindness as opposed to 1/200 women.',
        'Scientists were called “natural philosophers” until the 17th century because science didn’t exist as a concept.',
        'Natalie Portman is a Harvard graduate and has had papers published in two scientific journals, one of which was when she was in high school.',
        'Some of Neil Patrick Harris’ characters are magicians, and so if the actor. His children’s book series, The Magic Misfits, is also about a group of magicians.',
        'Colin Kaepernick got a pet tortoise at age 10, that fit in a shoebox. Today, the tortoise is 115 pounds and may live to be 135 years old.',
        'The Doctor Suess book Green Eggs and Ham uses only 50 different words. Doctor Suess wrote the book on a bet from his publisher that he couldn’t write a book with fewer words than The Cat in the Hat, which has 225.',
        'Woody Harrelson’s father was a hitman, who left the family when the actor was young. Woody didn’t find out about his father’s criminal activity until he heard a radio report on his trial.',
        'Dr. Martin Luther King was a Star Trek fan. He convinced Nichelle Nichols, one of the first black women featured on a major TV show, not to quit, arguing that her role was making history. Mae Jamison, the first black woman to travel into space, later cited Nichols as one of her inspirations.',
        'Queen Elizabeth II is the longest-serving British monarch. She has been on the throne for 67 years. The 93 year old queen’s heir is currently her son Charles, who is 70.',
        'Isaac Asimov published so many books, essays, short fiction, and non-fiction, that if you read one per week it would take you 9 years to read all of his work.',
        'In 2018, 50.3% of eligible voters turned out to vote. This was the highest turnout for a midterm election since 2018.',
        'Also in 2018, 16% of voters said it was the first time they’d voted in a midterm election.',
        'About ⅓ of Americans think the president affects their personal lives, and 63% say he affects the country’s mood.',
        'The U.S. spends more on defense than the other 7 countries combined. Last year, the U.S. spent $649 billion, while China, Saudi Arabia, India, France, Russia, the U.K. and Germany spent a combined $609 billion',
        'Any person born in the United States or to U.S. citizen parents is also a U.S. citizen.',
        'The U.S. Constitution was signed on September 17th, 1787. It was meant not to “grant” rights, but to protect the rights people were born with.',
        'Although the U.S. has a two party system, there are some other third parties. Notable ones now are the tea party and the green party, but the U.S. once had fringe parties like the Bull and Moose party.',
        'Americans throw out 4.4 pounds of trash daily.'
    ]

    return f'**Did you know?** ```\n{choice(didyouknows)}\n```'

def config_parse():
    try:
        with open('config.json', 'r') as cfg:
            data = json.loads(cfg.read())
        
        return data
    except FileNotFoundError:
        sys.exit('[/!\] Config not found, exiting.')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class Configuration():

    def __init__(self):
        self.config = config_parse()
        self.token = self.config['token']
        self.prefix = self.config['prefix']

    def config_save(self, data):

        try:
            with open('config.json', 'w+') as cfg:
                json.dump(data, cfg, indent=4)
        except Exception as e:
            print(f'[/!\] Exception while saving config: [{str(e)}]')
            sys.exit()
        
        # re-load the entire config
        self.config = config_parse()
        self.token = self.config['token']
        self.prefix = self.config['prefix']

        clear()

    def config_edit(self, key, value):

        cfg = self.config
        cfg[key] = value
        self.config_save(cfg)

def check(token):

    req = requests.get('https://discordapp.com/api/v9/users/@me', headers={'authorization': token})
    if req.status_code == 200: return True
    else: return False

def setTitle(title):

    try:
        if os.name == 'nt':
            try: ctypes.windll.kernel32.SetConsoleTitleW(title)
            except:  os.system(f'title {title}')
        else:
            try: sys.stdout.write(f'\x1b]2;{title}\x07')
            except: pass
    except:
        pass

def playSound(path):
    
    try:
        pygame.mixer.music.load(path)
        pygame.mixer.music.play(1)
    except:
        pass

class rpc:
    def __init__(self):
        self.stoppresence = False

    def setPresence(self, rpcClient_id, details=None, state=None, large_image=None, large_image_text=None, small_image=None, small_image_text=None, party_id=None, party_size=None, join=None, spectate=None, match=None, buttons=None, instance=None, start=time.time(), delay=15):
        while not self.stoppresence:
            try:
                RPC = Presence(rcpClient_id)
                RPC.connect()

                try:
                    RPC.update(
                        details=details, 
                        state=state, 
                        large_image=large_image, 
                        large_image_text=large_image_text, 
                        small_image=small_image, 
                        small_image_text=small_image_text, 
                        party_id=party_id,
                        party_size=party_size,
                        join=join,
                        spectate=spectate,
                        match=match,
                        buttons=buttons,
                        instance=instance,
                        start=timer
                    )
                except(InvalidPipe, InvalidID):
                    RPC = Presence(rcpClient_id)
                    RPC.connect()

                time.sleep(delay)
            except:
                sys.exit(f'[/!\] Exception while setting rich presence: [{str(e)}]')

    def stopPresence(Self):
        self.stoppresence = True