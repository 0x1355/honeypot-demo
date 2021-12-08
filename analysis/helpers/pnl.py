import numpy as np
import pandas as pd
from web3 import Web3

from .config import *
from .account import Account
from .tx import Tx

operator_addr = '0x0a04e8b4d2014cd2d07a9eaf946945bed1262a99'
bot_addr = '0x31B7e144b2CF261A015004BEE9c84a98263E2F66'.lower()
web3 = Web3(Web3.HTTPProvider(alchemy_url))

def get_bot_transfer_to_operator(tx):
    return tx[(tx['from'] == bot_addr) & (tx['to'] == operator_addr)]


def compute_net_profit_heuristic_1(tx):
    eth_usd = 4300
    net_profit = get_bot_transfer_to_operator(tx)
    value = net_profit['value'].iloc[0]
    asset = net_profit['asset'].iloc[0]
    if asset == 'CETH':
        eth_value = value * 87.39 / eth_usd
    else:
        eth_value = value / eth_usd
    return eth_value


def compute_net_profit_heuristic_2(tx):
    bot_eth_in = tx[(tx['to'] == bot_addr) & (tx['asset'] == 'ETH')]
    bot_eth_out = tx[(tx['from'] == bot_addr) & (tx['asset'] == 'ETH')]
    return sum(bot_eth_in['value']) - sum(bot_eth_out['value'])


def fetch_tx_data(tx_hash):
    tx = Tx(tx_hash)
    tx.fetch_data()
    return tx


def get_miner_tip(tx):
    block_number = int(tx.loc[:, 'blockNumber'].iloc[0])
    block = web3.eth.get_block(block_number)
    miner_addr = block.miner.lower()
    miner_transfer = tx[tx['to'] == miner_addr]
    if (not miner_transfer.empty):
        tip_value = float(miner_transfer['value'])
    else:
        tip_value = 0
    return tip_value


def compute_pnl(tx_hash, tx):
    tip = get_miner_tip(tx)
    if get_bot_transfer_to_operator(tx).empty:
        heuristic = 2
        net_profit = compute_net_profit_heuristic_2(tx)
    else:
        heuristic = 1
        net_profit = compute_net_profit_heuristic_1(tx)

    tx_data = fetch_tx_data(tx_hash)
    return pd.DataFrame({'hash': [tx_hash],
                         'block_number': [tx_data.block_number],
                         'index': [tx_data.index],
                         'status': [tx_data.status],
                         'pnl_heuristic': [heuristic], 
                         'gross_profit': [net_profit + tip],
                         'miner_tip': [tip],
                         'tx_cost': [tx_data.gas_cost],
                         'pnl': [net_profit - tx_data.gas_cost]})


