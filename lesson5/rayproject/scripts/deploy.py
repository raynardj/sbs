from brownie import accounts, config, SimpleStorage, network


def deploy_simple_storage():
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.load('sbs')


def main():
    deploy_simple_storage()

# Transaction sent: 0xb6a6302a427ef9c445dd8af2aef27d30bcd8594afe6b1f4cb3308d5247bdbde8
#   Gas price: 1.099999998 gwei   Gas limit: 372554   Nonce: 23
#   SimpleStorage.constructor confirmed   Block: 10279743   Gas used: 338686 (90.91%)
#   SimpleStorage deployed at: 0xF7a54Ae0E963e8E8C8723C60721aabbB312095CC

# 0
# Transaction sent: 0xc4ad039e960a1144b9d20c951b174c14b66dc8466f1654f732142d7655d803e4
#   Gas price: 1.099999998 gwei   Gas limit: 47880   Nonce: 24
#   SimpleStorage.store confirmed   Block: 10279744   Gas used: 43528 (90.91%)

#   SimpleStorage.store confirmed   Block: 10279744   Gas used: 43528 (90.91%)

# 15