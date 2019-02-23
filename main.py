print("este programa calcula el producto de dos nueros enteros y el doble del primer numero")

numa= int(input("ditite el numero entero a"))
numc= int(input("ditite el numero entero c"))

prod= numa*numc
doble= numa*2

print ("el producto de los dos numeros es " + str(prod))

print ("el doble de " + str(numa) + " es " + str(doble))

print("este programa calcula el cuadrado del primer numero y la raiz cuadrada de un segundo numero") 

import math
numb= int(input("ditite el numero entero b"))
numd= int(input("ditite el numero entero d"))

cuad= pow(numb,2)
raiz= math.sqrt(numd) 

print("el cuadrado de " + str(numb) + " es " + str(cuad))
print("la raiz cuadrada de " + str(numd) + " es " + str(raiz))

print("este programa permite calcular la solución de una ecuación cuadrática de tipo    ax2 + bx + c ")

a= int(input("ingres el valor de a"))
b= int(input("ingres el valor de b"))
c= int(input("ingres el valor de c"))

dentro= b*b-(4*a*c)
if(dentro==0):
	x1= -b/(2*a)
	print("existe una riz doble de valor: " + str(x1))
elif(dentro>0):
	dentro= math.sqrt(dentro)
	x1= (-b + dentro)/(2*a)
	x2= (-b - dentro)/(2*a)
	print("las raices son: " + str(x1) + " y " + str(x2))
else:
	x1= -b/(2*a)
	raizc= math.sqrt((-dentro/(2*a)))
	print("las raices imaginarias: " + str(x1) + " + " + str(raizc) + "i  y " + str(x1) + " - " + str(raizc) +"i")

