import math

def area_triangulo(base, altura):
    """
    Calcula el área de un triángulo dado su base y altura.
    Fórmula: (base * altura) / 2
    """
    return (base * altura) / 2

def area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.
    Fórmula: π * radio²
    """
    return math.pi * (radio ** 2)

# Programa principal
while True:
    print("\nOpciones:")
    print("1 - Calcular area de triángulo")
    print("2 - Calcular area de círculo")
    print("3 - Salir")
    
    opcion = input("Selecciona una opción: ").strip()
    
    if opcion == "1":
        print("Calculando area de triangulo")
        base = float(input("Ingresa la base: "))
        altura = float(input("Ingresa la altura: "))
        area = area_triangulo(base, altura)
        print(f"Área del triángulo: {area:.2f}")
    elif opcion == "2":
        print("Calculando area de circulo")
        radio = float(input("Ingresa el radio: "))
        area = area_circulo(radio)
        print(f"Área del círculo: {area:.2f}")
    elif opcion == "3":
        print("Finalizado")
        break
    else:
        print("Opción inválida")