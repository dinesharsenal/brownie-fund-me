from brownie import network, accounts, MockV3Aggregator
from web3 import Web3

FORKED_LOCAL_ENVIRONMETS = ["mainnet-fork", "mainnet-fork-dev"]

LOCAL_BLOCKCHAIN_ENVIRONMENT = ["development", "ganache-local"]


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENT
        or network.show_active() in FORKED_LOCAL_ENVIRONMETS
    ):
        return accounts[0]
    else:
        return accounts.load("dinesh-metamask")


def deploy_mocks():
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(18, Web3.toWei(2000, "ether"), {"from": get_account()})
