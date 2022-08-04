#Con este codigo revisamos dentro de que rango de edad esta el usuario
edad = int(input("¿Cuántos años tienes?: "))

#veintes = edad >= 20 and edad < 30
#treintas = edad >= 30 and edad < 40


#Simplificamos la sintaxis, quitando and y modificando la estructura
if (20 <= edad < 30) or (30 <= edad < 40):
    print("Dentro del rango de (20\'s) o (30\'s))")
    #if veintes:
    #    print("Tú estás: Dentro de los 20\'s.")
    #elif treintas:
     #   print(("Tú estás: Dentro de los 30\'s."))
else:
    print("No está dentro de los 20's o 30's.")