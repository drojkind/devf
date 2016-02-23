import random
# Piedra papel o python
opciones=["PIEDRA", "PAPEL", "PYTHON"]
print("Vamos a jugar \n")
usuario_op=input("Qué escoges? (Piedra, Papel o Python) ")
usuario_op=usuario_opcion.upper()
pc_op=opciones[random.randint(0,2)]
print(pc_op)
if usuario_opcion==pc_op:
	print("EMPATE")
elif usuario_opcion=="PIEDRA" and pc_op=="PAPEL":
	print("PERDISTE")
elif usuario_opcion=="PAPEL" and pc_op=="PYTHON":
	print("PERDISTE")
elif usuario_opcion=="PYTHON" and pc_op=="PIEDRA":
	print("PERDISTE")
else:
	print("GANASTE")

