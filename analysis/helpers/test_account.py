import pytest
import pandas as pd
from config import *
from account import Account

account_addr = '0x0Ac0A666ECE6C5EEE85B60A6c73A66d353680B74'
account = Account(account_addr)

contract_addr = '0x1e232D5871979eaA715De2c38381574a9C886BaD'
contract = Account(contract_addr)


def test_alchemy_endpoint_imported():
    assert(alchemy_url)


def test_new_wallet_address():
    assert(account.address == account_addr)

    
@pytest.fixture(scope="module")
def txs():
    yield account.fetch_txs()


def test_fetch_txs_type(txs):
    assert(isinstance(txs, pd.DataFrame))

    
def test_fetch_txs_cols(txs):
    cols = ['blockNumber', 'hash', 'from', 'to', 'value', 'asset', 'category', 'contract']
    assert(list(txs) == cols)
    

@pytest.fixture(scope="module")
def eth_tx(txs):
    sample = txs[txs.hash == "0xcf1e0b4e504fdc1c4b41aec4983b92e6310c69bbf8db28246f9c9f70c922722b"]
    yield sample.iloc[0]

    
def test_eth_tx_basic_info(eth_tx):
    assert((eth_tx['blockNumber'] == 10770357) &
           (eth_tx['from'] == "0x0ac0a666ece6c5eee85b60a6c73a66d353680b74") &
           (eth_tx['to'] == "0x905e769ad6e62a693f2a82975573fccf157f7416"))
    

def test_eth_tx_value(eth_tx):
    assert((eth_tx['value'] == 0.5) &
           (eth_tx['asset'] == 'ETH'))


@pytest.fixture(scope="module")
def erc20_tx(txs):
    sample = txs[txs.hash == "0xc3c4a419d0c49a6fdac949c743fff9a6f77a23ed71110db1e0ee341bf0e22776"]
    yield sample.iloc[0]


def test_erc20_tx_basic_info(erc20_tx):
    assert((erc20_tx['blockNumber'] == 12662178) &
           (erc20_tx['from'] == "0xdfd5293d8e347dfe59e90efd55b2956a1343963d") &
           (erc20_tx['to'] == '0x0ac0a666ece6c5eee85b60a6c73a66d353680b74'))


def test_erc20_tx_value(erc20_tx):
    assert((erc20_tx['value'] == 178.172) &
           (erc20_tx['asset'] == 'SNM') &
           (erc20_tx['contract'] == '0x46d0dac0926fa16707042cadc23f1eb4141fe86b'))

    
