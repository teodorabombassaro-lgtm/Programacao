#Como calcular a quantidade de novelos de lã necessários para produzir cada blusa em uma confecção, 
#considerando que cada blusa requer uma quantidade de 120 metros de fio 
#e que cada novelo contém 125 de metros de fio?
blusa = float(input("Digite quantas blusas você quer: "))
novelo = 125
vblusa = 120
total = blusa * vblusa
quantidade = total / novelo
print("O total de novelos é: ",quantidade)
