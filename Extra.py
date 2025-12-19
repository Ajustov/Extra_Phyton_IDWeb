def crear_correo(datos):
    print(datos[0], "@", datos[1], sep="")

datos = []
datos.append(input("Ingrese el nombre de usuario: "))
datos.append(input("Ingrese el dominio: "))

crear_correo(datos)
