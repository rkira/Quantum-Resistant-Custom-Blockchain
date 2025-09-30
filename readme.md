This project is a **Post-Quantum Cryptography (PQC) blockchain prototype** implemented in Python. It includes a blockchain module, quantum-safe signature schemes, and a basic node server for testing networked interactions.


external libraries:  
- https://github.com/open-quantum-safe/liboqs-python for quantum-safe signature support


## Prerequisites

- Ubuntu/Debian system  
- Python 3.10+ recommended  
- CMake (for building liboqs)  
- Git

---

## Installation & Setup

1. Clone the repository  
   $ git clone <your-repo-url>  
   $ cd pqc

2. Set up virtual environment  
   $ python3 -m venv .venv  
   $ source .venv/bin/activate

3. Install Python dependencies  
   $ pip install -r requirements.txt

4. Install liboqs-python  
   $ git clone --depth=1 https://github.com/open-quantum-safe/liboqs-python  
   $ cd liboqs-python  
   $ pip install .  
   $ cd ..

5. Set Python path   
   $ export PYTHONPATH=$(pwd)
    for example:"export PYTHONPATH=/home/rkira/Quantum-Resistant-Custom-Blockchain/"
---

## Running the Node Server

-Note: Make sure `liboqs-python` is installed before running the server.

To start a local node:  
$ python3 node/server.py

This will start the blockchain network.
For Example on: `http://localhost:5000/`

---

## Usage

- Provides a simple form to fill sender,receiver and amount(same as a crypto wallet).After filling in the details once submit add transaction to pending transactions.
<p align="center">
  <img src="https://github.com/user-attachments/assets/c9e1bf1e-ff61-424b-a679-98ba262f408b" alt="image" width="432" height="417">
</p>



- Pending transaction can be mined with `curl http://localhost:5000/mine` in terminal or just refresh `http://localhost:5000/mine` in browser.

- Mined transactions would clear from the Pending Transactions List and would be validated and then gets added to the blockchain and reflect in `http://localhost:5000/chain` that displays the full chain (with only validated transactions inside)

---

## Notes

- This implementation is not a cryptocurrency wallet and does not provide any cryptocurrency functionality. It is intended purely as a demonstration of how a blockchain network might operate using a quantum-safe signature algorithm.

- Multiple nodes can be connected by running `node/server.py` on different terminals or machines.

- The system uses the Open Quantum Safe (OQS) Signature(Dilithium3) of `liboqs-python`, to generate valid post-quantum digital signature.

---

## Important Information

This is a prototype-level implementation not for production use, as:

-The “address” derivation is custom (not a standard like Ethereum/BTC).
-There’s no persistence (keys vanish if you restart).
-Transaction format is simplified (no fee, gas, etc).
-Validation (verify or signature verification) isn’t included.



