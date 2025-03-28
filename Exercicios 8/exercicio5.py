class SaldoInsuficienteError(Exception):
    pass

try:
    saldo = 1000.0
    saque = float(input("Digite o valor que quer sacar do seu saldo! Lembrando que seu saldo atual é de 1000 reais! : "))
    if saldo - saque < 0:
        raise SaldoInsuficienteError("Saldo Insuficiente!")
    else:
        saldo = saldo - saque
        print("Saque efetuado! Seu saldo agora é de",saldo,"reais!")
except ValueError:
    print("O valor deve ser númerico!")
except SaldoInsuficienteError:
    print("Saldo insuficiente, tente outro valor!")

