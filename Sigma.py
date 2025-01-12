import os
from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip44, Bip44Coins, Bip44Changes
import requests

# Constants
ACTIVE_FILE_PREFIX = "active_wallets"
FILE_LIMIT = 1000  # Maximum addresses per file

def get_file_path(prefix, index):
    return f"{prefix}_{index}.txt"

def get_next_file(prefix):
    index = 1
    while os.path.exists(get_file_path(prefix, index)):
        if sum(1 for _ in open(get_file_path(prefix, index))) < FILE_LIMIT:
            return get_file_path(prefix, index)
        index += 1
    return get_file_path(prefix, index)

def save_to_file(prefix, address, private_key):
    file_path = get_next_file(prefix)
    with open(file_path, "a") as file:
        file.write(f"{address},{private_key}\n")

def generate_valid_mnemonic():
    return Bip39MnemonicGenerator().FromWordsNumber(12)

def generate_wallet(mnemonic, index=0):
    seed_bytes = Bip39SeedGenerator(mnemonic).Generate()
    bip44_mst = Bip44.FromSeed(seed_bytes, Bip44Coins.BITCOIN)
    bip44_acc = bip44_mst.Purpose().Coin().Account(0).Change(Bip44Changes.CHAIN_EXT)
    bip44_addr = bip44_acc.AddressIndex(index)
    address = bip44_addr.PublicKey().ToAddress()
    private_key = bip44_addr.PrivateKey().ToWif()
    return "bc" + address, private_key

def get_btc_balance(address):
    try:
        api_url = f"https://api.blockcypher.com/v1/btc/main/addrs/{address}/balance"
        response = requests.get(api_url)
        if response.status_code == 200:
            balance_info = response.json()
            return balance_info.get("balance", 0)
        return 0
    except Exception as e:
        print(f"Error fetching balance: {e}")
        return 0

while True:
    mnemonic = generate_valid_mnemonic()
    print(f"Generated Mnemonic: {mnemonic}")

    for index in range(10):  # Try 10 addresses from the same mnemonic
        wallet_address, wallet_private_key = generate_wallet(mnemonic, index)
        print(f"Wallet Address: {wallet_address}")

        balance = get_btc_balance(wallet_address)
        print(f"Balance: {balance} satoshis")

        if balance > 0:
            print(f"Active wallet found! Address: {wallet_address}, Balance: {balance}")
            save_to_file(ACTIVE_FILE_PREFIX, wallet_address, wallet_private_key)
            break
    else:
        # Continue to the next mnemonic if no active wallet is found
        continue
    break
