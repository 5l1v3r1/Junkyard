import contextlib
with contextlib.redirect_stdout(None): from pygame import mixer
from mutagen.mp3 import MP3
from mutagen.wave import WAVE
import time, threading, json, keyboard, os, ctypes
from colorama import Fore, Back, init; init()

mixer.init()
mixer.quit()
#mixer.init(devicename='Luidsprekers (Realtek(R) Audio)')
mixer.init(devicename='CABLE Input (VB-Audio Virtual Cable)')

class Sphere:
    def __init__(self):
        self.audiolength = ''
        self.currentaudio = ''
        self.audioconfig = {}
        self.isplaying = False
    
    def setTitle(self, title):
        if os.name == 'nt':
            try:os.system(f'title {title}')
            except:ctypes.windll.kernel32.SetConsoleTitleW(title)
        else:
            try: sys.stdout.write(f'\x1b]2;{title}\x07')
            except: pass

    def playaudio(self, audio):
        if not self.isplaying:
            try:
                self.currentaudio = audio
                self.audiolength = MP3(audio).info.length if audio.endswith('.mp3') else WAVE(audio).info.length if audio.endswith('.wav') else '0:00'

                self.isplaying = True
                print(f'{Fore.RESET}\n[ ~ ] Now playing: {self.currentaudio}. Length: {str(self.audiolength)}')
                mixer.music.load(audio) #Load the mp3
                mixer.music.play() #Play it
                time.sleep(self.audiolength)
                self.isplaying = False
            except Exception as e:
                self.currentaudio = 'Error while loading file'
                self.audiolength = '0.00'
                print(f'[ ~ ] Error while playing audio: {str(e).strip()}.')

    def loadconfig(self, config):
        with open(f'configs/{config}', 'r') as config_file:
            self.audioconfig = json.loads(config_file.read())

    def main(self):
        def startThread(audio):
            threading.Thread(target=self.playaudio, args=(audio,)).start()

        conflist = []
        print('')
        for _, _, conf_files in os.walk('configs'):
            for conf_file in conf_files:
                conflist.append(conf_file)
                print(f'{Fore.RESET}[ ~ ] Loaded config "{conf_file}"')
        
        while 1:
            conftoload = input('\nWhat config do you want to load? ')
            if not conftoload in conflist:
                print('\n[ ~ ] Invalid config, please try again.')
            else:    
                self.loadconfig(conftoload)
                break

        # add some default hotkeys
        print('\n[ ~ ] To pause all sounds, type "pause"')
        print('[ ~ ] To resume all sounds, type "resume" or "unpause"')
        print('[ ~ ] To stop all sounds, type "stop"')
        print('[ ~ ] To close the soundboard, press "exit" or "close"\n')

        for confkey in self.audioconfig.items():
            print(f'{Fore.RESET}[ ~ ] "{confkey[0]}" bound to [{confkey[1]["keys"]}], which plays [{confkey[1]["path"]}]')
            keyboard.add_hotkey(confkey[1]["keys"], startThread, args=[confkey[1]["path"]])
        
        print('')
        helpmsg = '''
[ 1 ] help > show this
[ 2 ] pause > pause all sounds
[ 3 ] unpause/resume > resume all sounds
[ 4 ] stop > stop all sounds
[ 5 ] exit/close > exit the soundboard
[ 6 ] play [audio path] > play audio
[ 7 ] clear > clear the screen
'''
        while 1:
            try:
                cmd = input('Command > ').split(' ')

                match cmd[0]:
                    case 'help': print(helpmsg)
                    case 'pause': print('[ ~ ] Audio paused.'); mixer.music.pause()
                    case ('resume'|'unpause'): print('[ ~ ] Audio unpaused.'); mixer.music.unpause()
                    case 'stop': print('[ ~ ] Audio stopped.'); self.isplaying = False; mixer.music.stop()
                    case ('exit'|'close'): print('[ ~ ] Byebye!');exit()
                    case 'play': threading.Thread(target=self.playaudio, args=(cmd[1],)).start()
                    case ('cls'|'clear'): os.system('cls' if os.name == 'nt' else 'clear'); print(helpmsg)
            except KeyboardInterrupt:
                exit()
            except Exception as e:
                print(f'[ ~ ] Uh oh! An exception appeared! {str(e).strip()}')

if __name__ == '__main__':
    Sphere().setTitle('Sphere Soundboard v1.0.0')
    Sphere().main()