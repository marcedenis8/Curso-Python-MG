# Ingreso de notas 

nota1= float(input("Ingrese la nota 1 :"))
nota2= float(input("Ingrese la nota 2 :"))
nota3= float(input("Ingrese la nota 3 :"))
promedio = (nota1 + nota2 + nota3)/ 3 
print(f"El promedio es: {promedio}")

# Evaluación del resultado
if promedio >= 5.0:
    print(f"Promediofinal: {promedio:.2f}")
    print("¡Aprobado!")

elif promedio >= 4.0:
    print(f"Promediofinal: {promedio:.2f}")
    print("¡Va a examen!")

else:
    print(f"Promedio final:{promedio:.2f}")
    print("¡Reprobado!")