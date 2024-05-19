#Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

num=int(input("Informe um numero: "))


def informe_numero(num):
    print("O numero informado foi: {}".format(num))


informe_numero(num)