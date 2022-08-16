import os, sys
import importlib
import requests

'''
WORK IN PROGRESS!!
'''

if sys.version_info.major <= 2:
    print('[+] Python 3.x needed! Please install before retrying.')
    exit()

if sys.version_info.major == 3 and sys.version_info.minor < 6:
    print('[+] Python 3.6+ needed! Please update before retrying!') 
    exit()

def install(module):
    try:
        importlib.import_module(module)
    except ImportError:
        try:
            os.popen(f'pip install {module}')
            os.popen(f'pip3 install {module}')
            os.popen(f'python -m pip install {module}')
            os.popen(f'python3 -m pip install {module}')
        except:
            return False

if os.name == 'nt': # Windows setup
    print('[+] Windows setup\n')

    print('[+] Installing modules\n')
    for module in [
        'requests',
        'discord.py',
        'asyncio',
        'pygame'
        ]:

        installed = install(module)
        if not installed: print(f'[+] Could not install {module}, please install it yourself')
        else: print(f'[+] Successfully installed module {module}')
    
    print('\n[+] Done installing modules')
        
    if not os.path.isfile('config.json'):
        print('[+] Could not find config file, downloading now.')
        #config = requests.get('https://raw.githubusercontent.com/Nexuzzzz/Sucuri/main/config.json').content
        #with open('config.json', 'w+') as conf:
            #conf.write(config)

    startup = input('\n[+] Add selfbot to startup? ')
    token = input('[+] Enter your discord token: ')
    theme = input('[+] Enter selfbot theme (leave empty for default, sucuri): ')
    #anon_stats = input('[+] Enable anonymous statistics?: ')
    prefix = input('[+] Enter selfbot prefix (leave empty for default, ./): ')
    prefix = input('[+] Enter selfbot prefix (leave empty for default, False): ')
    print('[+] To edit your API keys, open the "config.json" file and add them in there.')

else: # Posix setup
    print('[+] Posix setup\n')

print('[+] Setup finished! This script will now close.')
exit()