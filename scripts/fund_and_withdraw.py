from brownie import FundMe
from scripts.helpful_script import get_account

def fund():
    fundMe = FundMe[-1]
    account = get_account()
    entraceFee = fundMe.getEntranceFee()
    
    print(f"FundMe contract Address: {fundMe.address}")
    print(f"Account address: {account.address}")
    print(f"Entrance fee: {entraceFee}")

def main():
    fund()