from web3 import Web3
from .config import alchemy_url

class Tx:

    
    def __init__(self, hash):
        self.hash = hash

        
    def fetch_data(self):
        data, receipt = self._get_raw_data()
        self.block_number = data.blockNumber
        self.status = receipt.status
        self.gas_used = receipt.gasUsed
        self.gas_price = receipt.effectiveGasPrice
        self.gas_cost = self.gas_used * self.gas_price / 10**18
        self.index = receipt.transactionIndex
        self.calldata = data.input


    def _get_raw_data(self):
        web3 = Web3(Web3.HTTPProvider(alchemy_url))
        data = web3.eth.get_transaction(self.hash)
        receipt = web3.eth.get_transaction_receipt(self.hash)
        return data, receipt
