# Fund Transfer Tool

## Overview

This tool allows you to programmatically transfer funds between the Ethereum mainnet and the Mantle chain using Python and Web3.py. It is designed to be simple, with basic error handling, and can be easily deployed using Docker.

## Features

- Transfers funds between Ethereum and Mantle blockchains.
- Includes basic logging for transactions.
- Error handling for common scenarios.
- Containerized using Docker for easy deployment.

## Prerequisites

- **Docker**: Ensure Docker is installed on your machine.
- **Python 3.9 or later**: Required if you want to run the script outside of Docker.
- **Ethereum and Mantle Node Providers**: Access to Ethereum and Mantle node URLs (e.g., via Infura or Alchemy for Ethereum).
- **Private Key**: The private key of the account from which funds will be transferred.

## File Structure

- `Dockerfile`: Contains Docker instructions for building the container.
- `requirements.txt`: Lists Python dependencies.
- `fund_transfer.py`: Main script for handling fund transfers.
- `README.md`: Project documentation (this file).

## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-repo/fund_transfer_tool.git
   cd fund_transfer_tool
   ```

2. **Configure Environment:**

   Edit the `fund_transfer.py` file to set up your provider URLs and private key:

   ```python
   eth_provider_url = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
   mantle_provider_url = "https://mantle.network/rpc"
   private_key = "YOUR_PRIVATE_KEY"
   ```

   **Note:** Keep your private key secure and do not expose it in public repositories.

3. **Build the Docker Image:**

   ```bash
   docker build -t fund-transfer-tool .
   ```

4. **Run the Docker Container:**

   ```bash
   docker run --rm fund-transfer-tool
   ```

   This command will start the container and execute the fund transfer script.

## Usage

The tool is currently configured to transfer 1 ETH from Ethereum to Mantle. You can modify the `transfer_tool.transfer` call in `fund_transfer.py` to change the amount or direction of the transfer:

```python
success = transfer_tool.transfer("ethereum", "mantle", 1000000000000000000, "0xRecipientAddressHere")
```

Replace `"0xRecipientAddressHere"` with the recipient's address on the target blockchain.

## Security Considerations

- **Private Keys**: Ensure your private key is stored securely and not exposed in the code.
- **Network Fees**: Monitor gas prices to ensure transactions are processed efficiently without overpaying.
- **Production Use**: Consider additional security and error handling measures for production environments.

## Troubleshooting

- Ensure that your provider URLs are correct and that you have access to Ethereum and Mantle nodes.
- Verify that the private key corresponds to the correct account with sufficient funds for the transaction and gas fees.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- [Web3.py](https://github.com/ethereum/web3.py) for providing the blockchain interaction capabilities.

### Customization

- **Provider URLs and Private Key**: You need to replace placeholders in `fund_transfer.py` with actual node URLs and a private key. Ensure that these credentials are stored securely, especially when deploying in a production environment.
- **Network Conditions**: Keep an eye on network congestion and adjust gas prices accordingly. Consider implementing dynamic gas price adjustment if the tool will be used in varying network conditions.
- **Further Enhancements**: For a production-ready tool, consider implementing features such as dynamic gas price adjustments, retry mechanisms, and improved logging and error handling. 
