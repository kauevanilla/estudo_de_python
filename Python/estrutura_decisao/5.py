#Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.

notas = input("Informe as duas notas do aluno, separadas por espaço, por favor").split()

nota_1 = float(notas[0])
nota_2 = float(notas[1])

media = (nota_1 + nota_2) /2

if media > 7:
    print("Aprovado!")
elif media == 10:
    print("Aprovado com Distinção!")
else:
    print("Reprovado! Que decepção!")