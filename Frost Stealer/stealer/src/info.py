import os, json, socket, re, uuid, platform
from datetime import datetime
from src.utils import *

class Info():
    def __init__(self):
        pass

    def cli(self):
        output = {}
        if os.name == 'nt':
            output = {
                'whoami': Utils().run('whoami'),
                'groups': Utils().run('whoami /all'),
                'arp': Utils().run('arp -a'),
                'ipconfig': Utils().run('ipconfig /all'),
                'route': Utils().run('route print'),
                'netstat': Utils().run('netstat -anq'),
                'localgroup': Utils().run('net localgroup'),
                'sysinfo': Utils().run('systeminfo'),
            }
        else:
            output = {
                'whoami': Utils().run('whoami'),
                'groups': Utils().run('id -nG'),
                'arp': Utils().run('arp -a'),
                'ipconfig': Utils().run('ifconfig -a'),
                'route': Utils().run('route'),
                'netstat': Utils().run('netstat -wopa'),
                'sysinfo': Utils().run('uname -a'),
            }
        
        return output
    
    def sys(self):
        def getGPU():
            if os.name == 'nt': return Utils().run('wmic path Win32_VideoController get Caption')
            else: 
                try:
                    raw = Utils().run('lspci -k | grep -EA3 "VGA|3D|Display"')
                    parsed = re.findall(r'VGA compatible controller: .* \[(.*)\] (.*) \(rev c2\)', raw)[0]
                    return parsed[0] if len(parsed) == 1 else f'{parsed[0]}, {parsed[1]}'
                except:
                    return 'Unknown'

        try: pubip = requests.get(choice(['https://api.ipify.org','http://checkip.amazonaws.com','https://api.ipify.org/?format=text','https://myexternalip.com/raw','http://ip.42.pl/raw'])).text.rstrip().replace(' ','')
        except: pubip = '127.0.0.1'
        try: s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM); s.settimeout(0); s.connect(('10.255.255.255', 1)); privip = s.getsockname()[0]; s.close()
        except: privip = '127.0.0.1'

        arch = platform.machine() if len(platform.machine()) != 0 else 'Unknown'
        if 'AMD64' in arch and os.name == 'nt': arch = 'x86_x64'

        bt = datetime.fromtimestamp(psutil.boot_time())
        return {
            'os': platform.system() if len(platform.system()) != 0 else 'Unknown',
            'mac': ':'.join(re.findall('..','%012x' % uuid.getnode())),
            'pubip': pubip,
            'privip': privip,
            'cpu': platform.processor() if platform.processor() != "" else "Unknown",
            'gpu': getGPU().split('\n')[-1],
            'hostname': socket.gethostname(),
            'cores': {
                'physical': psutil.cpu_count(logical=False), 
                'total': psutil.cpu_count(logical=True)
            },
            'ram': {
                'used': str(round(psutil.virtual_memory().used/1000000000,2)), 
                'aviable': str(round(psutil.virtual_memory().available/1000000000,2)),
                'total': str(round(psutil.virtual_memory().total/1000000000,2))
            },
            'swap': {
                'used': str(round(psutil.swap_memory().used/1000000000,2)),
                'free': str(round(psutil.swap_memory().free/1000000000,2)),
                'total': str(round(psutil.swap_memory().total/1000000000,2))
            },
            'boot': f'{bt.hour}:{bt.minute}:{bt.second} {bt.year}/{bt.month}/{bt.day}'
        }

    def scan(self):
        output = {}
        output.update(self.cli())
        output.update(self.sys())

        with open('info.json', 'w+') as fd:
            fd.write(json.dumps(output, indent=4, sort_keys=False))