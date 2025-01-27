#!/usr/bin/env python3
from Crypto import Random
from Crypto.Cipher import AES
import base64
import sys
import hashlib

class AESCipher(object):

    def __init__(self, key):
        self.bs = 32
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('wtf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * bytes([self.bs - len(s) % self.bs])

    @staticmethod
    def _unpad(s):
        return s[:-int(s[len(s)-1:])]

def encrypt(data):
    n = 'totalpasecatotalcrypto324'
    a = AESCipher(n)
    return a.encrypt(data)
	
if __name__ == "__main__":
    img = sys.argv[1]
    while True:
        with open(img, "rb") as f:
            d = encrypt(f.read())
        keyprss = input("Press enter to encrypt it..")
        sys.stdout.flush()
        with open(img, "wb") as f:
            f.write(d)
        print("Encryp777ed!!\x18\x21")

