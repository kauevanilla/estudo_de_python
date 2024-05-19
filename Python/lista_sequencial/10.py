#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.


def cal_fah(cel):
    fah = 5 * ((cel-32) / 9)
    print("Em Fah: {}".format(fah))


cal_fah(int(input("Informe o valor em Celsius:")))
