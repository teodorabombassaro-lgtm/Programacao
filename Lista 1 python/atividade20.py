#Como calcular a quantidade de novelos de lã necessários para produzir cada blusa em uma confecção, 
#considerando que cada blusa requer uma quantidade de 120 metros de fio 
#e que cada novelo contém 125 de metros de fio?
quantidade_blusa = float (input("Quantas blusas deseja produzir?"))
novelo = 125
blusa = quantidade_blusa * 120
quantidade_novelos = blusa / novelo
print (f"A quantidade de novelos necessaros para {quantidade_blusa} blusas é de:", quantidade_novelos)
