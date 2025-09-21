import asyncio
from os import getenv
from dotenv import load_dotenv

load_dotenv()

import rsa
import hashlib
from eth_account.messages import encode_defunct

from alith.data import encrypt
from alith.data.storage import (
    GetShareLinkOptions,
    PinataIPFS,
    StorageError,
    UploadOptions,
)
from alith.lazai import Client

privacy_data = """\
# The Genesis of Cryptocurrency

Cryptocurrency is a digital or virtual currency that uses cryptography for security. A defining feature of a cryptocurrency, and arguably its most endearing allure, is its organic nature; it is not issued by any central authority, rendering it theoretically immune to government interference or manipulation.

## What is Blockchain?

At the heart of most cryptocurrencies is blockchain technology, a distributed ledger enforced by a disparate network of computers. Each block in the chain contains a number of transactions, and every time a new transaction occurs on the blockchain, a record of that transaction is added to every participant’s ledger. The decentralized database managed by multiple participants is known as Distributed Ledger Technology (DLT).

## How Does Cryptocurrency Work?

- **Transactions**: Transactions are sent between peers using software called cryptocurrency wallets.
- **Verification**: The person sending the transaction uses their private key to sign the transaction, which is a piece of cryptographic information that proves ownership.
- **Mining**: The transaction is then broadcast to the network and included in a block through a process called mining. Miners use powerful computers to solve complex mathematical problems. The first one to solve the problem gets to add the block to the blockchain and is rewarded with a small amount of cryptocurrency.
- **Security**: Once a transaction is added to the blockchain, it cannot be altered. This immutability is a key security feature of blockchain technology.

## Key Concepts

- **Decentralization**: No single entity controls the currency. This makes it resistant to censorship and control.
- **Cryptography**: Secure communication techniques are used to protect transactions and control the creation of new units.
- **Public and Private Keys**: A cryptocurrency wallet contains a set of public and private keys. The public key is like your bank account number and can be shared with others. The private key is secret and is used to authorize transactions.
- **Consensus Mechanisms**: These are protocols that allow the network to agree on the state of the ledger. The most common are Proof of Work (PoW) and Proof of Stake (PoS).

## The Future of Crypto

The world of cryptocurrency is constantly evolving. From decentralized finance (DeFi) applications that aim to rebuild traditional financial systems, to non-fungible tokens (NFTs) that are changing the way we think about ownership of digital assets, the potential applications of this technology are vast and largely untapped. As the technology matures, it has the potential to disrupt a wide range of industries.
"""


async def main():
    client = Client()
    ipfs = PinataIPFS()
    try:
        # 1. Prepare your privacy data and encrypt it
        data_file_name = "your_encrypted_dat2.txt"
        privacy_data_sha256 = hashlib.sha256(privacy_data.encode()).hexdigest()
        encryption_seed = "Sign to retrieve your encryption key"
        message = encode_defunct(text=encryption_seed)
        password = client.wallet.sign_message(message).signature.hex()
        encrypted_data = encrypt(privacy_data.encode(), password)
        # 2. Upload the privacy data to IPFS and get the shared url
        token = getenv("IPFS_JWT", "")
        file_meta = await ipfs.upload(
            UploadOptions(name=data_file_name, data=encrypted_data, token=token)
        )
        url = await ipfs.get_share_link(
            GetShareLinkOptions(token=token, id=file_meta.id)
        )
        # 3. Upload the privacy url to LazAI
        file_id = client.get_file_id_by_url(url)
        if file_id == 0:
            file_id = client.add_file_with_hash(url, privacy_data_sha256)
        print("File ID:", file_id)
        pub_key = client.get_public_key()
        encryption_key = rsa.encrypt(
            password.encode(),
            rsa.PublicKey.load_pkcs1(pub_key.strip().encode(), format="PEM"),
        ).hex()
        tx_hash, _ = client.add_permission_for_file(
            file_id, client.contract_config.data_registry_address, encryption_key
        )
        print("Transaction Hash:", tx_hash.hex())
    except StorageError as e:
        print(f"Error: {e}")
    except Exception as e:
        raise e
    finally:
        await ipfs.close()


if __name__ == "__main__":
    asyncio.run(main())