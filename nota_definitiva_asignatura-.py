# Programa para realizar los operadores, usando las diferentes formulas 

print("..........................................")
print("...El resultado de las operaciones son:...")
print("..........................................")
# input 
nc = int(input("Digite el valor de la nota procedimental: "))
cp = int(input("Digite el valor de cognitivo: "))
na = int(input("Digite el valor de actitudinal: " ))
au = int(input("Digite el valor de autoevaluacion: "))
bi = int(input("Digite el valor de bimestral: "))
# processing 
nd = (0.3*nc) + (0.3*cp) + (0.1*na) + (0.1*au) + (0.2*bi)
# output 
print("..................")
print("....RESULTADOS....")
print("..................")
print("NOTA DEFINITIVA " + str(nd))
