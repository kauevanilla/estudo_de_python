#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.


print("Este é um programa para calculara a area de um circulo")

raio = int(input("Primeiro, me informe o raio do seu circulo:"))

pi = 3.14

raio_2 = raio ** 2

area = raio_2 * pi
print("A area do circulo é: {}".format(area))