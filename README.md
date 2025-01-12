# README: Sigma-wallet-generator

## Overview

This script generates Bitcoin wallet addresses using BIP-39 mnemonics, checks their balances via the Blockcypher API, and saves active wallets (addresses with a positive balance) to text files. It is designed for educational and exploratory purposes only.

## Features

- **Mnemonic Generation**: Generates 12-word BIP-39 mnemonics.
- **Address Generation**: Derives Bitcoin wallet addresses and private keys using BIP-44.
- **Balance Checking**: Queries the balance of each generated address using the Blockcypher API.
- **Active Wallet Storage**: Saves active wallets (address and private key) to text files, each containing up to 1000 entries.
- **Efficient File Management**: Automatically creates new files when the current file reaches the limit.

## Requirements

- Python 3.7+
- Internet connection (for querying the Blockcypher API)

## Installation

### Step 1: Clone the Repository

```bash
# Clone the repository or download the script
$ git clone https://github.com/RICHMAKERZ/Sigma-wallet-generator.git>
$ cd <repository-folder>
```

### Step 2: Install Dependencies

Install the required Python libraries using pip:

```bash
$ pip install bip-utils requests
```

## Usage

### Step 1: Run the Script

Execute the script directly:

```bash
$ python sigma.py
```

### Step 2: Monitor Output

- The script will generate mnemonics, derive wallet addresses, and check balances.
- Active wallets (addresses with positive balances) will be saved to files named `active_wallets_X.txt`, where `X` is the file index.

### File Details

- **Active Wallets**: Saved in files named `active_wallets_X.txt`. Each line contains an address and its private key, separated by a comma.
- **File Limit**: Each file stores up to 1000 entries before a new file is created.

## Script Flow

1. **Generate Mnemonic**: A random 12-word mnemonic is created.
2. **Generate Wallets**: Up to 10 addresses are derived from the mnemonic.
3. **Check Balances**: Each address's balance is queried.
4. **Save Active Wallets**: If an address has a positive balance, it is saved with its private key.
5. **Repeat or Exit**: The script continues until an active wallet is found.

## Configuration

- **File Limit**: Adjust the maximum entries per file by modifying the `FILE_LIMIT` constant in the script.
- **Addresses Per Mnemonic**: Change the number of addresses derived per mnemonic by modifying the range in the `for index in range(10)` loop.

## Notes

- **Educational Use Only**: This script is for learning and experimentation. Do not use it for illegal or unethical activities.
- **API Rate Limits**: Be mindful of the Blockcypher API rate limits to avoid being blocked.
- **Private Key Security**: Handle private keys with care to avoid unauthorized access.

## Troubleshooting

- **Dependency Issues**: Ensure all required libraries are installed.
- **API Errors**: Verify your internet connection and ensure the Blockcypher API is accessible.
- **File Permissions**: Ensure the script has write permissions in the working directory.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Happy experimenting, and may your journey with Bitcoin exploration be as bright as a full moon! 🌕

