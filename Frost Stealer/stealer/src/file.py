import os, shutil
from src.config import *
from src.utils import *

class File():
    def __init__(self):
        pass

    def scan(self):
        if os.path.isdir('pictures'):
            shutil.rmtree('pictures', ignore_errors=True)
        
        os.mkdir('pictures')

        for _dir, _files in cfg.filesources:
            if not os.path.isdir(_dir):
                continue

            for root, _, files in os.walk(_dir):

                for file in files:

                    path = os.path.join(root, file)
                    dest = os.path.join('pictures', file)

                    for _file in _files:
                        if (_file in file or _files == '*') and (not dest in path):

                            if os.path.isfile(dest):
                                dest += '_'+Utils().randstr(5)

                            try: shutil.copyfile(path, dest, follow_symlinks=True)
                            except Exception: pass

                            continue