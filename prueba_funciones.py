sectores = ["norte","centro","sur"]

def registrar_pedido(pedidos):
    
    while True:
        pequeno = 0
        mediano = 0
        grande = 0
        nombre_cliente = input("Ingrese su nombre y apellido: ")
        if not nombre_cliente.isnumeric() and nombre_cliente.strip():
            break
        else:
            print("Nombre no pueden ser solo valores numericos o solo espacios en blanco")

    while True:
        direccion_cliente = input("Ingrese su direccion: ")
        if not direccion_cliente.isnumeric() and direccion_cliente.strip():
            break
        else:
            print("Direccion no puede ser solo numeros o solo espacios vacios")


    while True:
        sector_cliente = input("Ingrese el sector de la direccion(NORTE/CENTRO/SUR): ").lower()
        if sector_cliente in sectores:
            break
        else:
            print("Sector invalido")

    while True:
        print("       DETALLE DE PEDIDO      ")
        print("1. Paquete pequeño")
        print("2. Paquete mediano")
        print("3. Paquete grande")
        print("4. Salir")

        try:
            opc=int(input("Ingrese opcion deseada: "))
            if opc==1:
                pequeno +=1
                print("Paquete registrado")
            elif opc==2:
                mediano +=1
                print("Paquete registrado")
            elif opc==3:
                grande +=1
                print("Paquete registrado")
            elif opc==4:
                print("Pedido registrado con exito")
                break
            else:
                print("Tamaño de paquete invalido")

        except ValueError:
            print("Error: opcion invalida")
    
    pedidos.append({
        "Cliente":nombre_cliente,
        "Direccion":direccion_cliente,
        "Sector":sector_cliente,
        "Paquete pequeño":pequeno,
        "Paquete mediano":mediano,
        "Paquete grande":grande
    })

def listar_pedidos(pedidos):
    if not pedidos:
        print("No hay pedidos registrados, vuelve cuando los haya")
    else:
        claves = list(pedidos[0].keys())
        for clave in claves:
            print(f"{clave:<18}",end="")
        print()

        for pedido in pedidos:
            for clave in claves:
                print(f"{pedido[clave]:<18}",end="")
            print()

def imprimir_hoja_ruta(pedidos):
    if not pedidos:
        print("No hay pedidos registrados aun, vuelva cuando los haya")
    else:
        ruta_imprimir = input("Ingrese la ruta que desea imprimir (NORTE/CENTRO/SUR), esta opcion vacia imprimira todas las rutas: ")
        if ruta_imprimir == "":
            imprimir = pedidos
            nombre_archivo = "Todas las rutas.txt"
        elif ruta_imprimir in sectores:
            imprimir = []
            for diccionarios in pedidos:
                if diccionarios["Sector"] == ruta_imprimir:
                    imprimir.append(diccionarios)
                    nombre_archivo = f"Ruta {ruta_imprimir}.txt"

    with open (nombre_archivo,"w") as archivo:
        for diccionarios in imprimir:
            archivo.write(f"Cliente:{diccionarios["Cliente"]}\n")
            archivo.write(f"Direccion:{diccionarios["Direccion"]}\n")
            archivo.write(f"Sector:{diccionarios["Sector"]}\n")
            archivo.write(f"Paquete pequeño:{diccionarios["Paquete pequeño"]}\n")
            archivo.write(f"Paquete mediano:{diccionarios["Paquete mediano"]}\n")
            archivo.write(f"Paquete grande:{diccionarios["Paquete grande"]}\n")
            archivo.write("\n")