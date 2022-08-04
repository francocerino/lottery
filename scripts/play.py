from brownie import Lottery, accounts, config

def play():
    account = accounts.add(config["wallets"]["from_key"])
    lottery = Lottery[-1]
    lottery.play({
        "from": account,
        "value": "0.03 ether"
    })


def main():
    play()