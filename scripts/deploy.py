from brownie import Lottery, accounts, config

def deploy():
    account = accounts.add(config["wallets"]["from_key"])
    print(f"La cuenta con la que vamos a trabajar es {account}")
    lottery = Lottery.deploy(
        "0.01 ether",
        {"from":account},
        publish_source = True
    )


def main():
    deploy()