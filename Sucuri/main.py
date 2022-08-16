from colorama import init

''' Initialize console/terminal '''
init()

from Sucuri import bot
from Sucuri.util import *
from datetime import datetime
import os, sys, json, time

''' Import pygame, and make it shut up (setting the env variable didn't work) '''
import contextlib
with contextlib.redirect_stdout(None):
    import pygame

''' Initialize the mixer '''
pygame.mixer.init()

if __name__ == '__main__':
    clear()

    token = ''
    author = ''

    with open('config.json', 'r') as config1:

        json_config = json.loads( config1.read() )
        author = json_config['author']
        color = colors[Configuration().console_color]
        if json_config['selfbot']['token'] in ['Your token here', '']:

            setTitle(f'"Sucuri Selfbot | By {author} | https://github.com/Nexuzzzz/Sucuri | Please enter token"')
            print(f'{grey}┌────{color}[{white}Enter Token{color}]{grey}─{color}[{white}{datetime.now().strftime("%Y/%m/%d %H:%M:%S")}{color}]')
            token = input(f'{grey}└─{color}[{white}{os.getlogin()}{color}@{white}sucuri{color}]{white} ~${reset} ')
        
        else:
            token = json_config['selfbot']['token']
        
        #if json_config['anon_statistics'] == 'True':
        #     print(f'{grey}[{white}{datetime.now().strftime("%H:%M:%S")}{grey}] {white}Anonymous statistic sending is enabled!{reset}')
        #else:
        #    pass
        
    setTitle(f'"Sucuri Selfbot | By {author} | https://github.com/Nexuzzzz/Sucuri | Verifying token."')
    time.sleep(1)
    if check(token):
        setTitle(f'"Sucuri Selfbot | By {author} | https://github.com/Nexuzzzz/Sucuri | Token verified."')
        clear()
        
        print(f'{grey}[{white}{datetime.now().strftime("%H:%M:%S")}{grey}] {green}Verified{reset}')
        time.sleep(2); clear()
        bot.start(token)

    else:
        clear()
        setTitle(f'"Sucuri Selfbot | By {author} | https://github.com/Nexuzzzz/Sucuri | Token not verified."')
        print(f'{grey}[{white}{datetime.now().strftime("%H:%M:%S")}{grey}] {color}Not verified{reset}')
        time.sleep(2); sys.exit()