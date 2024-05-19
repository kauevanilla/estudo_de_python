#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados
# 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

val_hora = int(input("Informe quanto voce ganha por hora:"))
hora_mes = int(input("Informe quantas horas você trabalha por mes:"))

opcao = input("Selecione uma opção: a-Salario Bruto \n b-Valor ao INSS \n c-Quanto pagou ao sindicato \n d-Salario Liquido")

sal_bruto = val_hora * hora_mes
imposto = sal_bruto * 0.11
inss = sal_bruto * 0.08
sindicato = sal_bruto * 0.05
liquido = sal_bruto - imposto - inss - sindicato



match opcao:
    case "a":
        print("Salario Bruto: {}".format(sal_bruto))
    case "b":
        print("Valor ao INSS: {}".format(inss))
    case"c":
        print("Valor para o sindicato:".format(sindicato))
    case"d":
        print("Salario liquido: {}".format(liquido))
