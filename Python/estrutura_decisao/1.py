#Faça um Programa que peça dois números e imprima o maior deles.

nums = input("Informe dois numeros!").split()

num_1 = int(nums[0])
num_2 = int(nums[1])

if num_1 > num_2:
    print(num_1)
else:
    print(num_2)