#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota_1 =int(input("informe a primeira nota:"))
nota_2 =int(input("Informe a segunda nota:"))
nota_3 =int(input("Informe a terceira nota:"))
nota_4 =int(input("Informe a quarta nota:"))


soma =  nota_1 + nota_2 + nota_3 + nota_4
media = soma/4

print("A media é {}".format(media))

if media>6:
    print("Você Passou!")
else:
    print("Infelizmente você foi Ausberto!")



