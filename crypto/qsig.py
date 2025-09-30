from oqs import Signature  
import hashlib  

class QuantumSigner:  
    ALGORITHM = "Dilithium3"  

    def __init__(self):  
        self.signer = Signature(self.ALGORITHM)  
        self.public_key = self.signer.generate_keypair()  
        self.secret_key = self.signer.export_secret_key()  
        self.nonce = 0  

    def sign_transaction(self, data: dict) -> dict:  
        data_str = str(sorted(data.items())).encode()  
        digest = hashlib.sha3_512(data_str).digest()  
        signature = self.signer.sign(digest)  
        self.nonce += 1  
        address = hashlib.sha3_512(self.public_key + self.nonce.to_bytes(8, 'big')).hexdigest()[:40]  
        return {  
            'data': data,  
            'signature': signature.hex(),  
            'public_key': self.public_key.hex(),  
            'address': address,  
            'nonce': self.nonce  

        }  
