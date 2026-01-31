# Programa para calcular sueldo liquido de empleados
# con descuento de impuestos y bono por rangos

print("=== CALCULADORA DE SUELDO LIQUIDO ===")
moneda = "$"

while True:
    # Pedir sueldo bruto al usuario
    sueldo_bruto = float(input("Ingrese el sueldo bruto: " + moneda))
    
    # Calcular descuento de impuestos: 21.5%
    descuento = sueldo_bruto * 0.215
    sueldo_despues_impuestos = sueldo_bruto - descuento
    
    # Calcular bono segun rangos
    if sueldo_bruto < 600000:
        bono = 20000
        print("Bono aplicado: ",moneda ,"20000 (sueldo < 600000)")
    elif sueldo_bruto >= 600000 and sueldo_bruto <= 900000:
        bono = 25000
        print("Bono aplicado: ",moneda,"25000 (600000-900000)")
    else:
        bono = 30000
        print("Bono aplicado: ",moneda," 30000 (sueldo > 900000)")
    
    # Sueldo liquido final
    sueldo_liquido = sueldo_despues_impuestos + bono
    
    # Mostrar resultado
    print("Sueldo bruto: " , moneda, sueldo_bruto)
    print("Descuento impuestos: ", moneda, round(descuento, 2))
    print("Bono: ", moneda, bono)
    print("SUELDO LIQUIDO FINAL: ", moneda, round(sueldo_liquido, 2))
    print("-----------------------------------")
    
    # Preguntar si continuar
    continuar = input("¿Procesar otro empleado? (s/n): ")
    if continuar.lower() != 's':
        print("Programa terminado.")
        break

