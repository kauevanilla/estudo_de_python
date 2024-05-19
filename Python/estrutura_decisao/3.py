#Faça um Programa que verifique se uma letra digitada é "F" ou "M".
#Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input("Informe o seu sexo! F- feminino \n M- masculino \n NB- não binarie")

if sexo == "F":
    print("É feminino!")
elif sexo == "M":
    print("É masculino!")
elif sexo == "NB":
    print("É não binarie")
else:
    print("Não é um sexo valido!")
