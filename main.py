print("Este programa calcula el producto de dos núeros enteros y el doble del primer número.")

numa= int(input("Digite el número entero a"))
numc= int(input("Digite el número entero c"))

prod= numa*numc
doble= numa*2

print ("El producto de los dos números es " + str(prod))

print ("El doble de " + str(numa) + " es " + str(doble))

print("Este programa calcula el cuadrado del primer número y la raíz cuadrada de un segundo número.") 

import math
numb= int(input("Digite el número entero b"))
numd= int(input("Digite el número entero d"))

cuad= pow(numb,2)
raiz= math.sqrt(numd) 

print("El cuadrado de " + str(numb) + " es " + str(cuad))
print("La raíz cuadrada de " + str(numd) + " es " + str(raiz))

print("Este programa permite calcular la solución de una ecuación cuadrática de tipo    ax2 + bx + c. ")

a= int(input("Ingrese el valor de a"))
b= int(input("Ingrese el valor de b"))
c= int(input("Ingrese el valor de c"))

dentro= b*b-(4*a*c)
if(dentro==0):
	x1= -b/(2*a)
	print("Existe una ríz doble de valor: " + str(x1))
elif(dentro>0):
	dentro= math.sqrt(dentro)
	x1= (-b + dentro)/(2*a)
	x2= (-b - dentro)/(2*a)
	print("Las raices son: " + str(x1) + " y " + str(x2))
else:
	x1= -b/(2*a)
	raizc= math.sqrt((-dentro/(2*a)))
	print("Las raíces imaginarias: " + str(x1) + " + " + str(raizc) + "i  y " + str(x1) + " - " + str(raizc) +"i")