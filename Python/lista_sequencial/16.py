#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

auxiliar= 0
quant_tinta=0
preco=0

metros = int(input("Informe o tamanho, em metros quadrados,da area a ser pintada:"))

while metros > auxiliar:
    auxiliar = auxiliar + 18 * 3
    quant_tinta+=1
    preco+=80

print("Quantidade de latas: {}".format(quant_tinta))
print("Valor a ser cobrado: {}".format(preco))
