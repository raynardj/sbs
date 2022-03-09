from brownie import network, accounts, config,MockV3Aggregator
from web3 import Web3

# Constants
DECIMALS = 8
STARTING_PRICE = 200000000000
FORKED_LOCAL = ["mainnet-fork-dev",]

def get_account():
    if network.show_active() == "development" or network.show_active() in FORKED_LOCAL:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_mock():
    if len(MockV3Aggregator) == 0:
        MockV3Aggregator.deploy(
            DECIMALS, STARTING_PRICE, {"from": accounts[0]})
    return MockV3Aggregator[-1].address
