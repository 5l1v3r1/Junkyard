import math, psutil, socket, os, sys

def check():
    result = 0
    if math.ceil(psutil.virtual_memory().total/(2**30)) < 3: result+1 
    if psutil.cpu_count(logical=True) %2!= 0: result+1
    if True in [vm_str in str(os.popen('wmic computersystem get model').read()).lower() for vm_str in ['viritualbox','vmware']]: result+1
    if True in [mf_str in str(os.popen('wmic computersystem get manufacturer').read()).lower() for mf_str in ['innotek']]: result+1
    if True in [os.path.exists(vm_path) for vm_path in [r'C:\WINDOWS\system32\drivers\VBoxMouse.sys',r'C:\WINDOWS\system32\drivers\VBoxGuest.sys',r'C:\WINDOWS\system32\drivers\VBoxSF.sys',r'C:\WINDOWS\system32\drivers\VBoxVideo.sys',r'C:\WINDOWS\system32\vboxdisp.dll',r'C:\WINDOWS\system32\vboxhook.dll',r'C:\WINDOWS\system32\vboxmrxnp.dll',r'C:\WINDOWS\system32\vboxogl.dll',r'C:\WINDOWS\system32\vboxoglarrayspu.dll',r'C:\WINDOWS\system32\vboxoglcrutil.dll',r'C:\WINDOWS\system32\vboxoglerrorspu.dll',r'C:\WINDOWS\system32\vboxoglfeedbackspu.dll',r'C:\WINDOWS\system32\vboxoglpackspu.dll',r'C:\WINDOWS\system32\vboxoglpassthroughspu.dll',r'C:\WINDOWS\system32\vboxservice.exe',r'C:\WINDOWS\system32\vboxtray.exe',r'C:\WINDOWS\system32\VBoxControl.exe',r'C:\WINDOWS\system32\drivers\vmmouse.sys',r'C:\WINDOWS\system32\drivers\vmhgfs.sys',r'C:\WINDOWS\system32\drivers\vmusbmouse.sys',r'C:\WINDOWS\system32\drivers\vmkdb.sys',r'C:\WINDOWS\system32\drivers\vmrawdsk.sys',r'C:\WINDOWS\system32\drivers\vmmemctl.sys',r'C:\WINDOWS\system32\drivers\vm3dmp.sys',r'C:\WINDOWS\system32\drivers\vmci.sys',r'C:\WINDOWS\system32\drivers\vmsci.sys',r'C:\WINDOWS\system32\drivers\vmx_svga.sys']]: result+1
    if len(os.listdir(os.getenv('localappdata'))) > 45: result+1
    try: sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM); sock.connect( ('google.com') ); sock.close()
    except: result+1
    return result