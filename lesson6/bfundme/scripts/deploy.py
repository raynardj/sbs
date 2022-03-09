from brownie import FundMe, accounts, network, config
from scripts.utils import get_account, deploy_mock, FORKED_LOCAL

PUBLIC_NETS = ["mainnet", "ropsten", "rinkeby", "kovan"]


def get_price_feed_address():
    net = network.show_active()
    if net in PUBLIC_NETS:
        return config['networks'][net]['eth_usd_price_feed']
    elif net in FORKED_LOCAL:
        return config['networks'][net]['eth_usd_price_feed']
    else:
        return deploy_mock()


def deploy_fund_me():
    account = get_account()
    price_feed_address = get_price_feed_address()
    print(f"Deploying FundMe contract with {account}")
    fund_me = FundMe.deploy(price_feed_address, {"from": account},
                            publish_source=config["networks"][network.show_active()]["verify"])
    print(f"Contract deployed at: {fund_me.address}")


def main():
    deploy_fund_me()

# ===========================Verify==================================
# Running 'scripts/deploy.py::main'...
# Deploying FundMe contract with 0x3Ca11126482b8899A1C70293b2fb78A9e06bB2Fe
# Transaction sent: 0xaa7f762cc6bdc014c8b01022ba5589641be3bd5c14800856f5b6222a3d91fd30
#   Gas price: 1.000000029 gwei   Gas limit: 608822   Nonce: 29
#   FundMe.constructor confirmed   Block: 10293529   Gas used: 553475 (90.91%)
#   FundMe deployed at: 0x1BB5252F1270A5302B999dA0A4C07fCe7482eE5c

# Waiting for https://api-rinkeby.etherscan.io/api to process contract...
# Verification submitted successfully. Waiting for result...
# Verification pending...
# Verification pending...
# Verification complete. Result: Pass - Verified
# Contract deployed at: 0x1BB5252F1270A5302B999dA0A4C07fCe7482eE5c

# ===========================With mock==================================
# Running 'scripts/deploy.py::main'...
# Transaction sent: 0x7a7bc07f5eff3034a161c4d18bc9558fbe6882afdc70ca8f5e4878c193a846cf
#   Gas price: 0.0 gwei   Gas limit: 12000000   Nonce: 0
#   MockV3Aggregator.constructor confirmed   Block: 1   Gas used: 457693 (3.81%)
#   MockV3Aggregator deployed at: 0x3194cBDC3dbcd3E11a07892e7bA5c3394048Cc87

# Deploying FundMe contract with 0x66aB6D9362d4F35596279692F0251Db635165871
# Transaction sent: 0xe15471b603208a3341feed4ea3b15510750442c9172084b00381b8b51befd5f2
#   Gas price: 0.0 gwei   Gas limit: 12000000   Nonce: 1
#   FundMe.constructor confirmed   Block: 2   Gas used: 551158 (4.59%)
#   FundMe deployed at: 0x602C71e4DAC47a042Ee7f46E0aee17F94A3bA0B6

# Contract deployed at: 0x602C71e4DAC47a042Ee7f46E0aee17F94A3bA0B6
# Terminating local RPC client...


# add forked mainnet
# 