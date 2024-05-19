#Faça um Programa que peça dois números e imprima a soma.

def soma_dois_num():
    num_1 = int(input("informe um numero:"))
    num_2 = int(input("informe um numero:"))
    soma = num_1 + num_2
    print("{} + {} = {}".format(num_1,num_2,soma))

soma_dois_num()