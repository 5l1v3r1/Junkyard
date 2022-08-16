import binascii, base64
from Crypto.Cipher import AES
from io import StringIO

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
        return base64.b32encode(aes.encrypt(FKDL.encode(data)))[::-1].decode().replace('=','-')

    def decrypt(data):
        aes_decrypter = AES.new(b"\x80I\xc3\xc9\xc2\xb3\'Y\xbb\x84\xb4\xb7\xa4r13\x11TY\x85)\xc1\xf7\xedG\xbck\x08\x06[7\x11", AES.MODE_OCB, b"\xad\x83\xeb\xbc\x08'\xa5\x15\x94\\\x0c3\x84\xa5`")
        aes_decrypter.block_size = 512
        return FKDL.decode(aes_decrypter.decrypt(base64.b32decode(data.replace('-','=')[::-1]))).decode()

encrypted = FKDL.encrypt(b'test')
print('Encrypted: ', encrypted)
print('Decrypted: ', FKDL.decrypt(encrypted))