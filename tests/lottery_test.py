from brownie import Lottery, accounts

def test_deploy():
    account = accounts[0]
    lottery = Lottery.deploy("0.01 ether",
    {"from":account}
    )
    valor_inicial = lottery.minFee()
    esperado = "0.01 ether"
    assert valor_inicial == esperado

def test_play():
    account = accounts[0]
    lottery = Lottery.deploy("0.01 ether",
    {"from":account}
    )
    lottery.play(
        {
            "from":account,
            "value": "0.03 ether"}
            )
    saldo_esperado = "0.03 ether"
    saldo = lottery.getBalance()
    assert saldo == saldo_esperado