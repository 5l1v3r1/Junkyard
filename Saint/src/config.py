import json

class Configuration():
    '''
    Configuration class, used for loading/editing/parsing/saving the config file
    '''

    def __init__(self, cfgfile='config.json'):
        self.cfgfile = cfgfile
        self.cfg_raw = {}
        self.token = None
        self.prefix = None
        self.theme = None

        self.load()
    
    def parse(self) -> dict:
        '''
        parse() -> dict

        Loads a json configuration file

        :returns dict: The configuration contents
        '''

        with open(self.cfgfile) as fd:
            data = json.loads(fd.read())
        
        return data
    
    def save(self) -> None:
        '''
        save() -> None

        Saves the in-memory-stored configuration to the file

        :returns None: Nothing
        '''

        with open(self.cfgfile, 'w+') as fd:
            json.dump(self.cfg_raw, fd, indent=4)
    
    def load(self) -> None:
        '''
        load() -> None
        
        Loads all keys from the config file

        :returns None: Nothing
        '''

        data = self.parse()
        
        self.cfg_raw = data
        self.token = data['token']
        self.prefix = data['prefix']
        self.theme = data['theme']
    
    def edit(self, key, value) -> None:
        '''
        edit(key to edit, value to set) -> None

        Modifies a key and sets the value to the specified value

        :param key str: Key to modify
        :param value any: Value to set
        :returns None: Nothing
        '''

        self.cfg_raw[key] = value
        self.save()
        self.load()