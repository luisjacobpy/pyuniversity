"""
Instrucciones de tareas:
Solicitar al usuario dos valores, y determinar cual número
Solicitar al usuario dos valores:
numero1 (int)
numero2 (int)
Se debe imprimir el mayor de los dos numeros

"""
"""(--------ESTA ES MI SOLUCIÓN-----------)"""
numero1 = int(input("Ingresa el valor del PRIMER número: "))
numero2 = int(input("Ingresa el valor del SEGUNDO número: "))

if numero1 > numero2:
    print(f"El numero mayor es:{numero1}.")
elif numero1 == numero2:
    print(f"Los valores de los numeros es igual: {numero1}, {numero2}")
else:
    print(f"El numero mayor es:{numero2}.")
