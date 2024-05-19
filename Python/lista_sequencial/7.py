#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

print("Este programa irá caclular a area de um quadrado e seu dobro")


def area_quadrado(lado):
    area = lado * lado
    dobro = area * 2
    print("A area e {} e seu dobro e {}".format(area,dobro))

area_quadrado(int((input("Informe um lado:"))))
