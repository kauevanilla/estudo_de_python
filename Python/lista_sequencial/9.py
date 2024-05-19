#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.


def cal_cel(fah):
    cel = 5 * ((fah-32) / 9)
    print("Em celsius: {}".format(cel))


cal_cel(int(input("Informe o valor em Fahrenheit:")))
