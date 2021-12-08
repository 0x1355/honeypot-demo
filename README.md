# Honeypot :honey_pot:

A simple experiment that:
- Create a honeypot contract
- Bait a generalized frontrunning bot with a profitable transaction
- Analyze bot behaviour with a blackbox perspective 

Final project for ChainShort bootcamp Oct 2021 cohort. 

## Demo slides
The project presentation slide is in `presentation` directory. It gives an
overview about the project.

## Honeypot contract
Contract and tests are written in Solidity. Install `dapptools` to run the
tests.

## PnL dataset
To create or update the PnL dataset, run `create_pnl_datasets.py`. You need to
use `web3.py` and include your Etherscan API key and Alchemy RPC endpoint in
`config.py`

## Analysis
You can view the analysis files on GitHub. If you want to edit and run them, you
need to run Jupyter Notebook server with `Anaconda` or something similar.

## Known limitations
There limitaitons are known by the time of the final presentation:
- [ ] Unoptimized performance and too many JSON-RPC calls in when fetching data
- [ ] PnL computation is based on heuristic, not EVM state changes
- [ ] Outlier detection is based on manual sample check
- [ ] A few hardcoded simplifications like constant token prices
- [ ] No test for `helper.py`
