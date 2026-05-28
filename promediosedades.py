def calcularpromedioedades():
    cantidad_salones=int(input("digite la cantida de salones "))
    suma_edades=0
    for j in range(1,cantidad_salones+1):
        cantidad_alumnos=int(input("digite la cantidad de alumnos "))
        for i in range(1,cantidad_alumnos+1):
            edad=float(input("digite la edad del alumnos "))
            suma_edades=suma_edades+edad

    promedio_edad=suma_edades/cantidad_alumnos
    print(promedio_edad)

calcularpromediodeedad()
