# GESTIÓN DE BODEGA: LISTA DE 8 PRODUCTOS LÁCTEOS 
# Producto: código, nombre, precio, stock, departamento

producto1 = [101, "Leche entera 1L", 1200, 120, "Producción"]
producto2 = [102, "Leche descremada 1L", 1250, 85, "Producción" ]
producto3 = [103, "Yogurt natural 125g", 800, 200, "Envasado"]
producto4 = [104, "Queso fresco 200g", 2200, 45, "Queseria"]
producto5 = [105, "Mantequilla 250g", 3500, 30, "Envasado"]
producto6 = [106, "Leche condensada 395g", 2800, 60, "Producción"]
producto7 = [107, "Yogurt griego 150g", 1400, 75, "Enavasado"]
producto8 = [108, "Queso rallado 100g", 1800, 90, "Queseria"]


# Lista principal de inventario
inventario = [producto1, producto2, producto3, producto4, 
              producto5, producto6, producto7, producto8]

while True:
   
    print("MENÚ INVENTARIO BODEGA LÁCTEOS")
    print("1 - Ingresar nuevo artículo")
    print("2 - Eliminar artículo por código")
    print("3 - Buscar artículo por código")
    print("4 - Modificar stock")
    print("5 - Mostrar inventario completo")
    print("6 - Salir")
    
    opcion = input("Elige opción: ").strip()
    
    if opcion == "1":  # NUEVO ARTÍCULO
        print("\n--- NUEVO PRODUCTO ---")
        codigo = input("Código (3 dígitos): ")
        nombre = input("Nombre: ")
        precio = int(input("Precio: "))
        stock = int(input("Stock: "))
        departamento = input("depantamento: ")
        
        nuevo_producto = [codigo, nombre, precio, stock, departamento]
        inventario.append(nuevo_producto)
        print(f"{nombre} agregado. Stock: {stock}")
    
    elif opcion == "2":  # ELIMINAR
        print("\n--- ELIMINAR ---")
        codigo = input("Código a eliminar: ")
        encontrado = False
        for i in range(len(inventario)):
            if inventario[i][0] == codigo:  # [0] = código
                print(f" Eliminando: {inventario[i][1]} (${inventario[i][2]}, stock: {inventario[i][3]}), departamen {inventario [i][4]}")
                inventario.pop(i)
                encontrado = True
                break
        if not encontrado:
            print(" No encontrado.")
    
    elif opcion == "3":  # BUSCAR
        print("\n--- BUSCAR ---")
        codigo = input("Código: ")
        encontrado = False
        for producto in inventario:
            if producto[0] == codigo:
                print("\n ENCONTRADO:")
                print(f"   Código: {producto[0]}")
                print(f"   Nombre: {producto[1]}")
                print(f"   Precio: ${producto[2]:,}")
                print(f"   Stock: {producto[3]}")
                print(f"   Departamento: {producto[4]}")
                encontrado = True
                break
        if not encontrado:
            print(" No encontrado.")
    
    elif opcion == "4":  # MODIFICAR STOCK
        print("\n--- CAMBIAR STOCK ---")
        codigo = input("Código: ")
        nuevo_stock = int(input("Nuevo stock: "))
        encontrado = False
        for producto in inventario:
            if producto[0] == codigo:
                anterior = producto[3]
                producto[3] = nuevo_stock  # [3] = stock
                print(f"{producto[1]}: {anterior} → {nuevo_stock}")
                encontrado = True
                break
        if not encontrado:
            print("No encontrado.")
    
    elif opcion == "5":  # MOSTRAR TODO
        print("\n--- INVENTARIO COMPLETO ---")
        print(f"Total: {len(inventario)} productos | Stock total: {sum(p[3] for p in inventario)}")
        if len(inventario) == 0:
            print("Vacío.")
        else:
            print("-"*80)
            for i, producto in enumerate(inventario, 1):
                print(f"{i:2d}. {producto[0]:>3} | {producto[1]:<22} | ${producto[2]:>6,} | Stock: {producto[3]:>3} | Departamento: {producto[4]:<22} ")
            print("-"*80)
    
    elif opcion == "6":
        print("\n Programa terminado!")
        print(f"Artículos finales: {len(inventario)}")
        break
    
    else:
        print("Opción inválida")

print("Teminar")