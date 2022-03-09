from torch import baddbmm
from scripts.utils import get_account
from scripts.deploy import deploy_fund_me, PUBLIC_NETS
from brownie import FundMe, network, accounts, exceptions
import pytest

def test_can_fund_and_withdraw():
    if len(FundMe)==0:
        deploy_fund_me()

    fund_me = FundMe[-1]
    account = get_account()

    # fund
    entrance_fee = fund_me.getEntranceFee()+100
    tx = fund_me.fund({"from":account, "value":entrance_fee*2})
    tx.wait(1)

    assert fund_me.addressToAmountFunded(account.address) == entrance_fee*2

    tx2 = fund_me.withdraw({"from":account})
    tx2.wait(1)

    assert fund_me.addressToAmountFunded(account.address) == 0

# run the following to test
# >>> brownie test
# 1 passed in 3.99s

def test_only_owner_can_withdraw():
    if network.show_active() in PUBLIC_NETS:
        pytest.skip("Only run on mainnet")

    account = get_account()
    deploy_fund_me()
    fund_me = FundMe[-1]
    bad_actor = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from":bad_actor})


# on rinkeby
# 1 passed, 1 skipped in 34.49s 

# run the following to test
# >>> brownie test --network mainnet-fork-dev
# 2 passed in 41.35s
    