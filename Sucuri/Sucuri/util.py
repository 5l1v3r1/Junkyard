import click
import requests
import sys, os
import ctypes
import json
import contextlib
import psutil
import time
from Sucuri import bot
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

colors = {
    'red': '\033[31m',
    'green': '\033[32m',
    'orange': '\033[33m',
    'blue': '\033[34m',
    'purple': '\033[35m',
    'cyan': '\033[36m',
    'lightgrey': '\033[37m',
    'darkgrey': '\033[90m',
    'lightred': '\033[91m',
    'lightgreen': '\033[92m',
    'yellow': '\033[93m',
    'lightblue': '\033[94m',
    'pink': '\033[95m',
    'lightcyan': '\033[96m',
}

def config_parse():
    ''' Function to parse config file '''

    try:
        with open('config.json', 'r') as cfg:
            data = json.loads(cfg.read())
        
        return data
    except FileNotFoundError:
        print(f'{red}[{white}{datetime.now().strftime("%H:%M:%S")}{red}] {white}Config not found, exiting.{reset}')
        sys.exit()

def theme_parse(newTheme):
    ''' Function to parse theme file '''

    themes = []
    for filename in os.listdir('Sucuri/themes'):
        themes.append(filename)

    if f'{newTheme}.json' not in themes:
        print(f'{red}[{white}{datetime.now().strftime("%H:%M:%S")}{red}] [{white}{newTheme}{red}]{white} is not an existing theme, using default theme.{reset}')
        with open('Sucuri/themes/sucuri.json', 'r') as theme_json:
            _theme = json.loads(theme_json.read())
    else:
        try:
            with open(f'Sucuri/themes/{newTheme}.json', 'r') as theme_json: # vulnerable ik, but it will result in errors if the user tries escaping the string
                _theme = json.loads(theme_json.read())
        except Exception: # catch every exception
            print(f'{red}[{white}{datetime.now().strftime("%H:%M:%S")}{red}] {white}Failed to parse theme {red}[{white}{newTheme}{red}]{white}, using default theme.{reset}')
            with open('Sucuri/themes/sucuri.json', 'r') as theme_json:
                _theme = json.loads(theme_json.read())
    
    return _theme

def clear():
    ''' Function to clear the terminal '''
    os.system('cls' if os.name == 'nt' else 'clear')

class Configuration():
    ''' Configuration class '''

    def __init__(self):
        self.config = config_parse()

        ''' Selfbot info '''
        self.author = self.config['author']
        self.prefix = self.config['selfbot']['prefix']
        self.token = self.config['selfbot']['token']
        self.theme = self.config['selfbot']['theme']
        self.startup = self.config['selfbot']['startup']
        self.text_mode = True if self.config['selfbot']['text_mode'] == 'True' else False
        self.anon_statistics = True if self.config['selfbot']['anon_statistics'] == 'True' else False
        self.afk_message = self.config['selfbot']['afk_message']

        ''' Detections '''
        self.webhook_url = self.config['detections']['webhook_url']
        self.nitro_sniper = True if self.config['detections']['nitro_sniper'] == 'True' else False
        self.token_sniper = True if self.config['detections']['token_sniper'] == 'True' else False
        self.ghostping_notify = True if self.config['detections']['ghostping_notify'] == 'True' else False
        self.ban_notify = True if self.config['detections']['ban_notify'] == 'True' else False
        self.kick_notify = True if self.config['detections']['kick_notify'] == 'True' else False
        self.unfriend_notify = True if self.config['detections']['unfriend_notify'] == 'True' else False

        ''' Rich presence '''
        self.rich_presence_enabled = True if self.config['rich_presence']['enabled'] == 'True' else False
        self.rich_presence_id = self.config['rich_presence']['id']
        self.rich_presence_details = self.config['rich_presence']['details']
        self.rich_presence_state = self.config['rich_presence']['state']
        self.rich_presence_small_img_key = self.config['rich_presence']['small_image_key']
        self.rich_presence_small_img_text = self.config['rich_presence']['small_image_text']
        self.rich_presence_large_img_key = self.config['rich_presence']['large_image_key']
        self.rich_presence_large_img_text = self.config['rich_presence']['large_image_text']

        ''' API keys '''
        self.giphykeys = self.config['api_keys']['giphy']
        self.shodankeys = self.config['api_keys']['shodan']

        ''' Theme info '''
        self.theme_info = theme_parse(self.theme)
        self.theme_name = self.theme_info['theme_name']
        self.theme_author = self.theme_info['theme_author']
        self.embed_color = self.theme_info['embed']['color']
        self.embed_image = self.theme_info['embed']['image']
        self.embed_thumbnail = self.theme_info['embed']['thumbnail']
        self.embed_footer = self.theme_info['embed']['footer']
        self.embed_footer_icon = self.theme_info['embed']['footer_icon']
        self.console_color = self.theme_info['console']['color']

    def config_save(self, data):
        ''' Function to save config, and reload it '''

        try:
            with open('config.json', 'w+') as cfg:
                cfg.write(data)
        except Exception as e:
            print(f'{red}[{white}{datetime.now().strftime("%H:%M:%S")}{red}] {white}Exception while saving config: {red}{str(e)}{reset}')
            sys.exit()
        
        # re-load the entire config
        self.config = config_parse()
        self.author = self.config['author']
        self.prefix = self.config['selfbot']['prefix']
        self.token = self.config['selfbot']['token']
        self.theme = self.config['selfbot']['theme']
        self.startup = self.config['selfbot']['startup']
        self.text_mode = True if self.config['selfbot']['text_mode'] == 'True' else False
        self.anon_statistics = True if self.config['selfbot']['anon_statistics'] == 'True' else False
        self.afk_message = self.config['selfbot']['afk_message']
        self.webhook_url = self.config['detections']['webhook_url']
        self.nitro_sniper = True if self.config['detections']['nitro_sniper'] == 'True' else False
        self.token_sniper = True if self.config['detections']['token_sniper'] == 'True' else False
        self.ghostping_notify = True if self.config['detections']['ghostping_notify'] == 'True' else False
        self.ban_notify = True if self.config['detections']['ban_notify'] == 'True' else False
        self.kick_notify = True if self.config['detections']['kick_notify'] == 'True' else False
        self.unfriend_notify = True if self.config['detections']['unfriend_notify'] == 'True' else False
        self.rich_presence_enabled = True if self.config['rich_presence']['enabled'] == 'True' else False
        self.rich_presence_id = self.config['rich_presence']['id']
        self.rich_presence_details = self.config['rich_presence']['details']
        self.rich_presence_state = self.config['rich_presence']['state']
        self.rich_presence_small_img_key = self.config['rich_presence']['small_image_key']
        self.rich_presence_small_img_text = self.config['rich_presence']['small_image_text']
        self.rich_presence_large_img_key = self.config['rich_presence']['large_image_key']
        self.rich_presence_large_img_text = self.config['rich_presence']['large_image_text']
        self.giphykeys = self.config['api_keys']['giphy']
        self.shodankeys = self.config['api_keys']['shodan']
        self.theme_info = theme_parse(self.theme)
        self.theme_name = self.theme_info['theme_name']
        self.theme_author = self.theme_info['theme_author']
        self.embed_color = self.theme_info['embed']['color']
        self.embed_image = self.theme_info['embed']['image']
        self.embed_thumbnail = self.theme_info['embed']['thumbnail']
        self.embed_footer = self.theme_info['embed']['footer']
        self.embed_footer_icon = self.theme_info['embed']['footer_icon']
        self.console_color = self.theme_info['console']['color']

        clear()
        bot.banner()

    def config_edit(self, key, value):
        ''' Function to edit config '''

        cfg = self.config # get config
        cfg[key] = value
        #print(cfg)
        self.config_save(cfg)

def give_color():
    ''' Self explanatory '''

    return colors[Configuration().console_color]

def make_embed(title, title_prefix=True, values=None, description=None, color=None, thumbnail=None, image=None, footer=None, footer_icon=None):
    ''' Function to make embed'''

    # IM SORRY OK!? THIS WAS THE ONLY THING THAT WORKED AFTER 50 MINUTES OF PURE DEBUGGING PAIN
    if description is None: description = f'Prefix: **{Configuration().prefix}**\nTheme loaded: **{Configuration().theme_name}**\nTheme created by: **{Configuration().theme_author}**'
    if color is None: color = Configuration().embed_color
    if image is None: image = Configuration().embed_image
    if thumbnail is None: thumbnail = Configuration().embed_thumbnail
    if footer is None: footer = Configuration().embed_footer
    if footer_icon is None: footer_icon = Configuration().embed_footer_icon
    
    if not Configuration().text_mode:

        if title_prefix: 
            title = f'Sucuri Selfbot | {title}'

        em = Embed(title=title, description=description, color=int(color, base=16))
        em.set_thumbnail(url=thumbnail)
        em.set_image(url=image)
        
        if values != None:
            for value in values:
                em.add_field(name=value[0], value=value[1], inline=value[2])

        em.set_footer(icon_url=footer_icon, text=footer)
        return True, em
    else:
        if title_prefix: 
            title = f'Sucuri Selfbot | {title}'

        txt_values = ''
        if values != None:
            for value in values:
                txt_values += f'<{value[0]}>\n{value[1].replace("*","")}\n'

        result = f'```brainfuck\n[ {title} ]\n_________________________________\n{description.replace("*", "")}\n'

        if not len(txt_values) <= 0:
             result += f'__________________________________\n{txt_values}'

        result += f'__________________________________\n[ {footer} ]```'
        return False, result

def random_quote():
    ''' Function to return random quote '''

    with open('Sucuri/quotes.txt', 'r') as quotefile:
        quote = choice(quotefile.readlines())
    
    return quote

def check(token):
    ''' Function to check if token is valid '''

    req = requests.get('https://discordapp.com/api/v7/users/@me', headers={'authorization': token})
    if req.status_code == 200: return True
    else: return False

def setTitle(title):
    ''' Function to set terminal/console title '''

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
    ''' Function to play sound effect '''
    
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
                sys.exit(f'{red}[{white}{datetime.now().strftime("%H:%M:%S")}{red}] {white}Exception while setting rich presence: {red}{str(e)}{reset}')

    def stopPresence(Self):
        self.stoppresence = True