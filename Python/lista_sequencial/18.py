#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade
# de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

tam_arv = float(input("Informe o tamanho do arquivo para dowload (MB):"))
vel_link = float(input("A velocidade do link da internet (Mbps):"))

vel_link = vel_link / 8

tempo_aproximado = tam_arv / vel_link

tempo_aproximado_minutos = tempo_aproximado / 60

print("Tempo aproximado de download: {}".format(tempo_aproximado_minutos))


