from brownie import Lottery, Contract

def read():
    #lottery = Lottery[-1]
    lottery = Contract('0xFD4f9cA245213AB39d43E5D4b33c82E97f767c58')
    min_fee = round(lottery.minFee().to("ether"),3)
    print(f" La tarifa minima para particpar de la loteria es {min_fee}")


def main():
    read()