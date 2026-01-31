# Ejercicio Tarea:
# determinar el promedio de las N notas de un estudiante. Las notas deben almacenarse 
# en una lista y el programa debe soportar las operaciones: agregar nota, quitar notas, 
# mostrar notas y mostrar promedio

# 1 - Agregar nota
# 2 - Quitar nota
# 3 - Mostrar notas
# 4 - Mostrar promedio
# 5 - Terminar

 # Programa para manejar notas de un estudiante
# Usamos una lista vacía para guardar las notas
notas = []  # Lista empieza vacía

# El bucle while se repite hasta que el usuario elija salir
while True:  # True significa "siempre verdadero", se repite infinitamente hasta break
    print("=== MENÚ DE NOTAS ===")
    print("1 - Agregar nota")
    print("2 - Quitar nota")
    print("3 - Mostrar notas")
    print("4 - Mostrar promedio")
    print("5 - Terminar")
    
    opcion = input("¿Qué quieres hacer? Elige 1,2,3,4 o 5: ")  # Leer lo que escribe el usuario
    
    if opcion == "1":  # Si elige 1
        nota_nueva = float(input("Escribe la nota: "))  # Convierte texto a número
        notas.append(nota_nueva)  # Agrega al FINAL de la lista
        print("¡Nota agregada!")  # Confirma
        
    elif opcion == "2":  # Si elige 2
        if len(notas) == 0:  # len() cuenta elementos
            print("No hay notas para quitar.")
        else:
            # Muestra las notas con sus posiciones (índices)
            print("Tus notas:")
            for i in range(len(notas)):  # range crea números
                print(f"  Posición {i}: {notas[i]}")
            indice = int(input("¿Posición a quitar?: "))
            if 0 <= indice < len(notas):  # Verifica que sea válido
                nota_quitada = notas.pop(indice)  # Quita y guarda la nota
                print(f"Quitaste la nota {nota_quitada}")
            else:
                print("Posición inválida.")
                
    elif opcion == "3":  # Si elige 3
        if len(notas) == 0:
            print("No hay notas.")
        else:
            print("Lista de notas:", notas)  # Imprime toda la lista
            
    elif opcion == "4":  # Si elige 4
        if len(notas) == 0:
            print("No hay notas para promediar.")
        else:
            suma = 0
            for nota in notas:  # Recorre cada nota
                suma = suma + nota  # Suma todas
            promedio = suma / len(notas)  # Divide por cantidad
            print("Promedio:", round(promedio, 2))  # round da 2 decimales
            
    elif opcion == "5":  # Si elige 5
        print("Terminar")
        break  # Sale del while
        
    else:  # Si escribe algo equivocado
        print("Opción no válida")