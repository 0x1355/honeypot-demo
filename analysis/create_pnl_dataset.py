import numpy as np, pandas as pd, os
from helpers.config import *
from helpers.account import Account
from helpers.tx import Tx
from helpers.helpers import *


operator_addr = '0x0a04e8b4d2014cd2d07a9eaf946945bed1262a99'
bot_addr = '0x31B7e144b2CF261A015004BEE9c84a98263E2F66'.lower()

bot = Account(bot_addr)
bot_txs = bot.fetch_txs()

unique_hashes = np.unique(bot_txs['hash'])
pnl_list = []

for tx_hash in unique_hashes:
    tx = bot_txs[bot_txs['hash'] == tx_hash]
    pnl = compute_pnl(tx_hash, tx)
    pnl_list.append(pnl)
    
all_pnl = pd.concat(pnl_list)

mev_pnl = all_pnl[all_pnl['miner_tip'] > 0]
non_mev_pnl = all_pnl[all_pnl['miner_tip'] <= 0]

outliers = ['0x77cca0ffc9f3ea3de0100b4a9802e05f1026da2be61efe7239d3433bbdf7420f',
            '0x36d2f3aaf7d160ea9bd072692555e6d3ff9b76139c8dfa83a475b23cc39cf8e6',
            '0x5ca8362ea279bf7f908ca35436533cf7ebcd93ed150f11abf45ebd6d72a5ab79']

mev_pnl_wo_outliers = mev_pnl[~mev_pnl['hash'].isin(outliers)]
mev_pnl_outliers = mev_pnl[mev_pnl['hash'].isin(outliers)]

mev_pnl_wo_outliers.to_csv(os.path.join('data', 'mev-pnl.csv'), index=False)
mev_pnl_outliers.to_csv(os.path.join('data', 'mev-outliers.csv'), index=False)
non_mev_pnl.to_csv(os.path.join('data', 'non-mev-pnl.csv'), index=False)



