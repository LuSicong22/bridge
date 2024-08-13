import logging
from typing import Union

from web3 import Web3
from web3.middleware import geth_poa_middleware

# Initialize logging
logging.basicConfig(level=logging.INFO)

class BlockchainTransfer:
    def __init__(self, eth_provider: str, mantle_provider: str, private_key: str):
        self.eth_web3 = Web3(Web3.HTTPProvider(eth_provider))
        self.mantle_web3 = Web3(Web3.HTTPProvider(mantle_provider))
        self.private_key = private_key
        self.eth_web3.middleware_onion.inject(geth_poa_middleware, layer=0)
        self.mantle_web3.middleware_onion.inject(geth_poa_middleware, layer=0)

    def _get_balance(self, web3: Web3, address: str) -> Union[int, None]:
        try:
            balance = web3.eth.get_balance(address)
            return balance
        except Exception as e:
            logging.error(f"Error getting balance: {e}")
            return None

    def _send_transaction(self, web3: Web3, to_address: str, amount: int) -> bool:
        try:
            nonce = web3.eth.get_transaction_count(self.eth_web3.eth.account.privateKeyToAccount(self.private_key).address)
            transaction = {
                'to': to_address,
                'value': amount,
                'gas': 2000000,
                'gasPrice': web3.toWei('20', 'gwei'),
                'nonce': nonce
            }
            signed_txn = web3.eth.account.sign_transaction(transaction, private_key=self.private_key)
            tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
            receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
            logging.info(f"Transaction successful with hash: {receipt.transactionHash.hex()}")
            return True
        except Exception as e:
            logging.error(f"Error sending transaction: {e}")
            return False

    def transfer(self, from_chain: str, to_chain: str, amount: int, to_address: str) -> bool:
        if from_chain == "ethereum" and to_chain == "mantle":
            return self._send_transaction(self.eth_web3, to_address, amount)
        elif from_chain == "mantle" and to_chain == "ethereum":
            return self._send_transaction(self.mantle_web3, to_address, amount)
        else:
            logging.error("Invalid chain names")
            return False

if __name__ == "__main__":
    # Replace with actual provider URLs and private key
    eth_provider_url = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"
    mantle_provider_url = "https://mantle.network/rpc"
    private_key = "YOUR_PRIVATE_KEY"

    transfer_tool = BlockchainTransfer(eth_provider_url, mantle_provider_url, private_key)
    success = transfer_tool.transfer("ethereum", "mantle", 1000000000000000000, "0xRecipientAddressHere")
    if success:
        logging.info("Fund transfer completed successfully")
    else:
        logging.error("Fund transfer failed")