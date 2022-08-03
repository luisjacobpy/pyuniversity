
"""
Instrucciones de la tarea
Calcular el área y el perimetro de un Rectángulo, para ello deberemos crear las siguientes variables:
alto(int)
ancho(int)

Las formulas para calcular el area y el perimetro
Area: alto * ancho
Perimetro: (alto + ancho) + 2

"""
print("A continuación introduce los siguientes valores")

alto = int(input("Introduce el ALTO del Rectáncgulo: "))
ancho = int(input("Introduce el ANCHO del Rectángulo: "))

area = alto * ancho
perimetro = (alto + ancho) * 2

print("El Área del Rectangulo es:", area)
print("El Perimetro del Rectangulo es:", perimetro)
