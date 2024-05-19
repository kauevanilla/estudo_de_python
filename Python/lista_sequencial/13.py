#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

sexo=input("Você é do sexo masculino ou feminino?")

if sexo == 'masculino':
    altura=float(input("Informe sua altura:"))
    peso= (72.7*altura) - 58
    print("Peso ideal: {}".format(peso))

elif sexo == "feminino":
    altura = float(input("Informe sua altura:"))
    peso = (62.1 * altura) - 44.7
    print("Peso ideal: {}".format(peso))
else:
    print("Por favor, informe um sexo valido!")


