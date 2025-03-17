import ecdsa, os

if not os.path.exists('cipher/ecc/keys'):
    os.makedirs('cipher/ecc/keys')
    
    
class ECCipher:
    def __init__(self):
        pass
    
    def generate_keys(self):
        sk = ecdsa.SigningKey.generate()
        vk = sk.get_verifying_key()
        
        
        with open('cipher/ecc/keys/privateKey.pem', 'wb') as p:
            p.write(sk.to_pem())
            
        with open('cipher/ecc/keys/public.pem', 'wb') as p:
            p.write(vk.to_pem())
            
    def load_keys(self):
        with open('cipher/ecc/keys/privateKey.pem', 'rb') as p:
            sk = ecdsa.SigningKey.from_pem(p.read())
        
        with open('cipher/ecc/keys/public.pem', 'rb') as p:
            vk = ecdsa.VerifyingKey.from_pem(p.read())
            
        return sk, vk
    
    def sign(self, message, sk):
        return sk.sign(message.encode('ascii'))
    
    def verify(self, message, signature, vk):
        try:
            # Kiểm tra message có rỗng không
            if not message or not isinstance(message, str):
                return False
                
            # Kiểm tra signature có hợp lệ không
            if not signature or not isinstance(signature, bytes):
                return False
                
            # Kiểm tra verifying key có hợp lệ không
            if not vk or not isinstance(vk, ecdsa.VerifyingKey):
                return False
                
            # Thực hiện verify chữ ký
            return vk.verify(signature, message.encode('ascii'))
            
        except (ecdsa.BadSignatureError, ValueError, TypeError):
            return False
    

