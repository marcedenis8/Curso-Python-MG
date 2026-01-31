# DICCIONARIO GESTIÓN DE BODEGA LACTEOS
lista_productos = []

while True:  # True significa "siempre verdadero", se repite infinitamente hasta break
    print("=== MENÚ ===")
    print("1 - Agregar producto")
    print("2 - Quitar producto")
    print("3 - Buscar producto por codigo")
    print("4 - Modificar stock producto")
    print("5 - Listar productos")
    print("6 - Terminar")
    opcion = input("¿Qué quieres hacer?: ")  # Leer lo que escribe el usuario
    if opcion == "1":
      print("Agregar producto:")
      codigo = input("Codigo:")
      nombre = input("Nombre:")
      precio = input("Precio:")
      stock = input("Stock:")
      departamento = input("Departamento:")
      producto = {"codigo":codigo, "nombre":nombre, "precio":precio, "stock":stock, "departamento": departamento}
      lista_productos.append(producto)  # Agrega al FINAL de la lista
      print("¡Producto agregado!")  # Confirma
    elif opcion == "2":  # Si elige 2
        print("Eliminar producto:")
        if len(lista_productos) == 0:  # len() cuenta elementos
            print("No hay productos para eliminar.")
        else:
            print("Lista de productos:")
            for i in range(len(lista_productos)):  # range crea números
                print(f" Posición {i}: {lista_productos[i]}")
            indice = int(input("¿Posición a quitar?: "))
            if 0 <= indice < len(lista_productos):  # Verifica que sea válido
                producto_quitado = lista_productos.pop(indice)  # Quita y guarda la nota
                print(f"Eliminaste el producto {producto_quitado}")
            else:
                print("Posición inválida.")
    elif opcion == "3":  # BUSCAR
        print("Buscar producto:")
        codigo = input("Código:")
        encontrado = False
        for producto in lista_productos:
            if producto["codigo"] == codigo:
                print("\n Encontrado:")
                print(f"   Código: {producto["codigo"]}")
                print(f"   Nombre: {producto["nombre"]}")
                print(f"   Precio: ${producto["precio"]}")
                print(f"   Stock: {producto["stock"]}")
                print(f"   Departamento: {producto["departamento"]}")
                encontrado = True
                break
        if not encontrado:
            print("No encontrado.")
    elif opcion == "4":  # MODIFICAR STOCK
        print("Modificar stock:")
        codigo = input("Código: ")
        nuevo_stock = int(input("Nuevo stock: "))
        encontrado = False
        for producto in lista_productos:
            if producto["codigo"] == codigo:
                anterior = producto["stock"]
                producto["stock"] = nuevo_stock 
                print(f"El producto {producto["nombre"]} fue modificado: {anterior} → {nuevo_stock}")
                encontrado = True
                break
        if not encontrado:
            print("No encontrado.")
    elif opcion == "5":  # MOSTRAR TODO
        if len(lista_productos) == 0:
            print("No hay productos.")
        else:
             for producto in lista_productos:
              print(f"{producto["codigo"]} | {producto["nombre"]} | ${producto["precio"]} | {producto["stock"]} | {producto["departamento"]} ")
    elif opcion == "6":  # Si elige 6
        print("Terminar")
        break  # Sale del while
    else:  # Si escribe algo equivocado
        print("Opción no válida")