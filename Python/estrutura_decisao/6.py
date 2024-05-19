#Faça um Programa que leia três números e mostre o maior deles

numeros = input("Informe três numeros!").split()

num_1 = int(numeros[0])
num_2 = int(numeros[1])
num_3 = int(numeros[2])


if num_1 > num_2 & num_1 > num_3:
    print("O maior numero é o {}".format(num_1))
elif num_2 > num_1 & num_2 > num_3:
    print("O maior numero é o {}".format(num_2))
else:
    print("O maior numero é o {}".format(num_3))