# Honeypot :honey_pot:

A simple experiment that:
- Creates a honeypot contract
- Baits a generalized fronturnning bot with a unique transaction
- Analyze bot behaviour using a black box approach

Final project for ChainShort bootcamp Oct 2021 cohort. 

## Presentation Deck
The project presentation deck is in `presentation` directory. It gives an
overview about the project.

## Experiment addresses and txs
Honeypot contract address:
`0x1e232d5871979eaa715de2c38381574a9c886bad`

Bot contract:
`0x31B7e144b2CF261A015004BEE9c84a98263E2F66`

Bot operator:
`0x0a04e8b4d2014cd2d07a9eaf946945bed1262a99`

Failed tx 1 (block 13710082, index 22):
`0xcc1172506d5b5fa09cbf66d2296deb24958181f186817eb29cbe8385fd55ed51`

Frontrun tx 1 (block 13710082, index 0):
`0x18ec2c2e5720c6d332a0f308f8803e834e06c78dcebdc255178891ead56c6d73`

Failed tx 2 (block 13710542, index 80): 
`0xfce9b77a8c7b8544cb699ce646558dc506e030aaba1533c917d7841bcc3f206a`

Frontrun tx 2 (block 13710542, index 0):
`0x8cda6e76f9a19ce69967d9f74d52402afbafba6ca3469248fe5c9937ef065d47`

## Running contract tests
The contract tests are written in Solidity. To run them:
1. Install `dapptools` on your machine
2. Navigate to the project root directory in terminal, then `dapp install ds-test`
3. Rename `.dapprc.template` to `.dapprc` and add your Ethereum RPC endpoint
4. Use `dapp test` to run the tests.

## PnL dataset
To create or update the PnL dataset:
1. Make sure you have Python 3 and the relevant modules installed on your machine
2. Rename `config.template.py` to `config.py` and add your Etherscan API key and
   Alchemy RPC endpoint
3. Run `python analysis/create_pnl_datasets.py` in your terminal

## Analysis
You can view the analysis files on GitHub. If you want to edit and run them, you
need to run Jupyter Notebook server with `Anaconda` or something similar.

## Known limitations
These limitaitons are known by the time of the final presentation:
- [ ] Unoptimized performance and too many JSON-RPC calls in when fetching data
- [ ] PnL computation is based on heuristic, not EVM state changes
- [ ] Outlier detection is based on manual sample check
- [ ] A few hardcoded simplifications like constant token prices
- [ ] No test for `pnl.py` and `calldata.py`
