#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Informe uma letra!")
i=0
vogal = ["A","a","E","e","I","i","O","o","U","u"]


for letra in vogal:
    if letra in vogal:
        i =+1

if i == 1:
    print("É vogal")
else:
    print("É consoante")

