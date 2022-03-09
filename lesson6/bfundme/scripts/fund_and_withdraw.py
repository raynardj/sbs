from brownie import FundMe
from scripts.utils import get_account, deploy_mock
import logging
from scripts.deploy import deploy_fund_me

logging.getLogger().setLevel(logging.INFO)

def fund():
    fund_me = FundMe[-1]
    logging.info(f"Fund me contract address: {fund_me.address}")
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()
    logging.info(f"Entrance Fee: {entrance_fee}")

    fund_me.fund({"from":account, "value":entrance_fee})

def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.withdraw({"from":account})

def main():
    if len(FundMe)==0:
        deploy_fund_me()
    fund()
    withdraw()