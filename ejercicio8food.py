menu={"Burrito":"Machaca"}
menu["Taco"]="pastor"
menu["Torta"]="milanesa"
pedido=[]

print("Bienvenido este es nuestro menú:")

for key,val,val in menu.items():
	print("Tenemos {} de {}".format(key,val))

orden=input("Que se te antoja? (para salir presiona Q )")
while orden.upper() != "Q":
	if menu.get(orden):
		pedido.append(orden)
	else: 
		print("Esto no se lo vengo manejando") 
	orden=input("Que se te antoja? (para salir presiona Q )")
print("TU pedido es: ")
for num in range(len(pedido)): 
	print (num+1,pedido[num],sep=". ")
