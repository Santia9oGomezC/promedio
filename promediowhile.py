def cacularpromediodeedad():
    cantidad_alumnos=int(input("digite lq cantidad de alumnos "))
    i=1
    suma_edades=0
    while i < (cantidad_alumnos+1):
        edad=int(input("digite la edad del alumno "))
        suma_edades=suma_edades+edad
        i=i+1

        promedio_edad=suma_edades/cantidad_alumnos 
        print(promedio_edad)

        calcularpromediodeedad()
        