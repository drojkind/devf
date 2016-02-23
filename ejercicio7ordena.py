lista = [3, 2, 4, 6, 20, 30,0]
lista_ordenada=[]
while len(lista)>0:
	mini=lista[0]
	for num in lista[1:]:
		if num<mini:
			mini=num
	lista_ordenada.append(mini)
	lista.remove(mini)
print(lista_ordenada) 