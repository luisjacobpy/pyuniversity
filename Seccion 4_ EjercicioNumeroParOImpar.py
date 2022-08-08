#Sección 4: Operadores en Python

#Valor dentro de rengo
valor = int(input("Escribe un valor: "))
valueMinimun = 0
valorMaximo = 5

#Los parentesís son opcionales
dentroRango = (valor >= valueMinimun) and (valor <= valorMaximo)

if dentroRango:
    print(f"El valor {valor} está dentro de Rango.")
else:
    print(f"El valor {valor} está fuera de rango.")