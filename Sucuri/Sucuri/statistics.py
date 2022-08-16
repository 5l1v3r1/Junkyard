# for all you people who read too fast, this is just for error logging and statistics
# only the os, selfbot version, python version and error will be collected!

# example on how to use with the "traceback" module and "sys" module
'''
try:
    1 + 'c'
except:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
    traceback_exc = ''.join(line for line in lines)

    report(f'{str(exc_type.__name__)}: {str(exc_value)}', traceback_exc)
'''

#url = '[scrubbed]'
#import requests
#import platform
#from Sucuri.util import *

#def report(title, traceback):
#    content = {
#        'username': 'Sucuri Statistics',
#        'avatar_url': 'https://2.bp.blogspot.com/-Pg4lK8P3-sA/XK6ff9Q-uZI/AAAAAAAA1ns/p-SbYlB_3iUzQpWuBWX-rsyWjjAHwEj7wCLcBGAs/w7000/High%2BSchool%2BDxD%2B-%2BRias%2BGremory%2BRender%2B291.png',
#        'embeds': [
#            {
#                'title': title,
#                'thumbnail': {
#                    'url': 'https://blog.sqlauthority.com/wp-content/uploads/2016/01/erroricon1.png'
#                },
#                'fields': [
#                    {
#                        'name': 'Environment',
#                        'value': f'''```brainfuck
#Operating system: {platform.platform()}
#Selfbot version: {Configuration().version}
#Python version (short): {sys.version_info.major}.{sys.version_info.minor}
#Python version (long): {sys.version}
#```''',
#                        'inline': False
#                    },
#                    {
#                        'name': 'Full Traceback', 
#                        'value': f'```py\n{traceback}```', 
#                        'inline': False
#                    }
#                ],
#                'footer': {
#                    'text': 'Sucuri Statistics | Part of the Sucuri Selfbot',
#                    'icon_url': 'https://2.bp.blogspot.com/-Pg4lK8P3-sA/XK6ff9Q-uZI/AAAAAAAA1ns/p-SbYlB_3iUzQpWuBWX-rsyWjjAHwEj7wCLcBGAs/w7000/High%2BSchool%2BDxD%2B-%2BRias%2BGremory%2BRender%2B291.png'
#                }
#3            }
#        ]
#    }
#
#    req = requests.post(url, json=content, timeout=2)