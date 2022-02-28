from scripts.helpful_script import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.deploy import deploy_fund_me
from brownie import network, accounts, exceptions
import pytest

def test_can_fund_and_withdraw():
    account = get_account()
    fundMe = deploy_fund_me()
    price = fundMe.getPrice()
    entranceFee = fundMe.getEntranceFee()
    print(f"Account: {account}")
    print(f"Price: {price}")
    print(f"Entrance Fee: {entranceFee}")

    fundTx = fundMe.fund({"from": account, "value": entranceFee})
    fundTx.wait(1)

    assert fundMe.addressToAmountFunded(account.address) == entranceFee

    withdrawalTx = fundMe.withdraw({"from": account})
    withdrawalTx.wait(1)
    
    assert fundMe.addressToAmountFunded(account.address) == 0

def test_only_owner_can_withdraw():
    print(f"Current network: {network.show_active()}")
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing")

    account = get_account()
    fundMe = deploy_fund_me()
    badActor = accounts.add()

    with pytest.raises(exceptions.VirtualMachineError):
        fundMe.withdraw({"from": badActor})