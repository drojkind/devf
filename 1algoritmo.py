import math
disco = 700
gb = 1024
print("Cuanto pesa tu disco duro? \n")
totalgb=int(input("Pon la cantidad en GB "))
total = gb * totalgb
totalfinal = total / disco
print(math.ceil(totalfinal))