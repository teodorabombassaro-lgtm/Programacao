#Construa um algoritmo para calcular a distância entre dois pontos do plano cartesiano. 
#Cada ponto é um par ordenado (x,y).
x1 = float (input("Digite a coordenada x do primeiro par ordenado:"))
y1 = float (input("Digite a coordenada y do primeiro par ordenado:"))
x2 = float (input("Digite a coordenada x do segundo par ordenado:"))
y2 = float (input("Digite a coordenada y do segundo par ordenado:"))

diferenca_x = x2 - x1
diferenca_y = y2 - y1

distancia = ((diferenca_x ** 2) + (diferenca_y ** 2)) **0.5

print("a distancia entre os pontos ({},{}) e ({},{}) é {:.2f} unidades" .format(x1,y1,x2,y2, distancia))
