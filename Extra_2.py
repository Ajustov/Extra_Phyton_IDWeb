def promedio_modificado(*notas):
    mayor = max(notas)
    menor = min(notas)

    suma = sum(notas) - menor + mayor
    promedio = suma / len(notas)

    return promedio
