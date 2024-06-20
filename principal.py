import prueba_funciones as fn
pedidos = []

while True:
    print("      MENU      ")
    print("****************")
    print("1. Registrar pedido")
    print("2. Listar pedido")
    print("3. Imprimir pedidos")
    print("4. Salir")

    try:
        opc = int(input("Ingrese la opcion que desea: "))
        if opc==1:
            fn.registrar_pedido(pedidos)
        elif opc==2:
            fn.listar_pedidos(pedidos)
        elif opc==3:
            fn.imprimir_hoja_ruta(pedidos)
        elif opc==4:
            break
        else:
            print("Opcion fuera de rango")
    except ValueError:
        print("Error: Opcion invalida")