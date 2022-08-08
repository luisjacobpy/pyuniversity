#Ingresar i guardar datos de un libro

print("Proporciona los siguientes datos del libro")
bookName = input("Proporciona el nombre del libro: ")
print(bookName)
idBook = int(input("Proporciona el ID del libro: "))
print(idBook)
priceBook = float(input("Proporciona el precio del libro incluye los centavos: "))
print(priceBook)
costService = input("El envio es gratuito Si / No: ")

if costService == "Si":
    costService = True
elif costService == "Sí":
    costService = True
elif costService == "no":
    costService = False
else:
    print("Introduce un valor válido.")
print(costService)

print(f'''
    Resumen del pedido
    Nombre: {bookName}
    Id: {idBook}
    Precio: {priceBook}
    Envío Gratuito: {costService}
''')

