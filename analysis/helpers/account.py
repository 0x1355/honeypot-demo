from .config import *
import pandas as pd
import requests, json

headers = {'Content-Type': 'application/json'}
method = 'alchemy_getAssetTransfers'
category = ('external', 'internal', 'erc20')
from_block = '0x1'
cols = ['blockNumber', 'hash', 'from', 'to', 'value', 'asset', 'category', 'contract']

class Account:
    

    def __init__(self, addr):
        self.address = addr

        
    def fetch_txs(self):
        from_txs = self._fetch_raw_txs(self.address, '')
        to_txs = self._fetch_raw_txs('', self.address)
        txs = pd.concat([from_txs, to_txs])
        txs['contract'] = txs['rawContract.address']
        txs['blockNumber'] = txs['blockNum'].apply(int, base=0)
        return txs[cols]
    

    def _add_next_page_txs(self, txs, page_id, page_key, from_address, to_address):

        if (not from_address and not to_address):
            raise ValueError('Do not leave both from_address and to_address empty. Too many calls')
        
        call_data = self._create_txs_call_data(txs, page_id, page_key,
                                      from_address, to_address)
        
        call_result = self._fetch_result(call_data)

        new_txs = pd.json_normalize(call_result['transfers'])
        txs = pd.concat([txs, new_txs])
        page_id += 1

        try:
            page_key = call_result['pageKey']
        except KeyError:
            page_key = ''

        return txs, page_id, page_key


    def _create_txs_call_data(self, txs, page_id, page_key, from_address, to_address):
        
        params = [{
            'category': category,
            'fromBlock': from_block
        }]
        
        if page_key:
            params[0]['pageKey'] = page_key

        if from_address:
            params[0]['fromAddress'] = from_address

        if to_address:
            params[0]['toAddress'] = to_address
        
        data = {
            'jsonrpc': '2.0',
            'method': method,
            'params': params,
            'id': page_id
        }

        return data


    def _fetch_result(self, call_data):
        call_response = requests.post(alchemy_url,
                                    headers=headers,
                                    data=json.dumps(call_data))
        return call_response.json()['result']

    
    
    def _fetch_raw_txs(self, from_address, to_address):
        page_id = 1
        page_key = ''
        txs = pd.DataFrame()

        while ((page_id == 1) | (page_key != '')):
            txs, page_id, page_key = self._add_next_page_txs(txs, page_id, page_key, from_address, to_address)

        return txs


