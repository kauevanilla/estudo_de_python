#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

hora = int(input("Voce ganha quanto por hora?"))
mes = int(input("Voce trabalha quantas horas no mês?"))

salario = hora * mes

print("Salario final:{}".format(salario))
