#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo

int_1=int(input("Informe um numero int"))
int_2=int(input("Informe um segundo int"))
real=float(input("Informe um numero real"))

def prod(int_1,int_2):
    produto= (int_1 * 2) + int_2/2
    print("#o produto do dobro do primeiro com metade do segundo:{}".format(produto))

prod(int_1,int_2)

def trip(int_1,real):
    triplo = (int_1 * 3) + real
    print("a soma do triplo do primeiro com o terceiro: {}".format(triplo))

trip(int_1,real)

def cubo(real):
    cube = real ** 3
    print("O cubo é :{}".format(cube))

cubo(real)