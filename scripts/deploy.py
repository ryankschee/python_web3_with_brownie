from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_script import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS

def deploy_fund_me():
    account = get_account()

    # If we are on a persistent network like rinkeby, ropsten, mainnet, then use the associated address;
    # otherwise, deploy mocks
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
    print(f"Price feed address: {price_feed_address}")

    fundMe = FundMe.deploy(
        price_feed_address, 
        {"from": account}, 
        publish_source=config["networks"][network.show_active()].get("verify")
    )
    print(f"FundMe Contract deployed to {fundMe.address}")

    return fundMe

def main():
    deploy_fund_me()