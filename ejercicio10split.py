lista=list(map(int,input("Dame una lista de numeros").split(" ")))
print(lista)
total_suma=0
for num in lista:
	total_suma+=num
print(total_suma)