import time  
import json  
import hashlib  
from crypto.qsig import QuantumSigner  

class QuantumBlockchain:  
    def __init__(self):  
        self.chain = []  
        self.pending_txs = []  
        self.signer = QuantumSigner()  
        self.create_genesis_block()  

    def create_genesis_block(self):  
        genesis = {  
            'index': 0,  
            'timestamp': time.time(),  
            'transactions': [],  
            'previous_hash': '0'*128,  
            'quantum_safe': True  
        }  
        self.chain.append(genesis)  

    def new_transaction(self, sender: str, recipient: str, amount: float):  
        tx = self.signer.sign_transaction({  
            'sender': sender,  
            'recipient': recipient,  
            'amount': amount,  
            'timestamp': time.time()  
        })  
        self.pending_txs.append(tx)  
        return tx  

    def mine_block(self):  
        last_block = self.chain[-1]  
        new_block = {  
            'index': len(self.chain),  
            'timestamp': time.time(),  
            'transactions': self.pending_txs,  
            'previous_hash': self.hash_block(last_block),  
            'quantum_safe': True  
        }  
        self.chain.append(new_block)  
        self.pending_txs = []  
        return new_block  

    @staticmethod  
    def hash_block(block: dict) -> str:  

        return hashlib.sha3_512(json.dumps(block, sort_keys=True).encode()).hexdigest()  
