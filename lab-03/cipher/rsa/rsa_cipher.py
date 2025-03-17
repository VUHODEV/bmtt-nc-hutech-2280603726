import os
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.Cipher import PKCS1_OAEP
import base64

if not os.path.exists('cipher/rsa/keys'):
    os.makedirs('cipher/rsa/keys')

class RSACipher:
    def __init__(self):
        pass
    
    def generate_keys(self):
        key = RSA.generate(2048)
        private_key = key.export_key()
        public_key = key.publickey().export_key()
        
        with open('cipher/rsa/keys/privateKey.pem', 'wb') as p:
            p.write(private_key)
            
        with open('cipher/rsa/keys/public.pem', 'wb') as p:
            p.write(public_key)
            
    def load_keys(self):
        with open('cipher/rsa/keys/privateKey.pem', 'rb') as p:
            private_key = RSA.import_key(p.read())
        
        with open('cipher/rsa/keys/public.pem', 'rb') as p:
            public_key = RSA.import_key(p.read())
            
        return private_key, public_key
    
    def encrypt(self, message, key):
        cipher = PKCS1_OAEP.new(key)
        return cipher.encrypt(message.encode('ascii'))
    
    def decrypt(self, ciphertext, key):
        cipher = PKCS1_OAEP.new(key)
        return cipher.decrypt(ciphertext).decode('ascii')
    
    def sign(self, message, private_key):
        hash_obj = SHA256.new(message.encode('ascii'))
        signer = PKCS1_v1_5.new(private_key)
        return signer.sign(hash_obj)
    
    def verify(self, message, signature, public_key):
        try:
            hash_obj = SHA256.new(message.encode('ascii'))
            verifier = PKCS1_v1_5.new(public_key)
            verifier.verify(hash_obj, signature)
            return True
        except (ValueError, TypeError):
            return False