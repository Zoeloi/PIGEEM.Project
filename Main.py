from Finanzas import finanzas

def menu_principal():
    while True:
        print("\n--- PIGEEM Plataforma Integral ---")
        print("1. Finanzas y Contabilidad")
        print("2. Inventario y Pedidos")
        print("3. Gestión de Clientes y Empleados")
        print("4. Panel General")
        print("5. Salir")
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            finanzas.menu_finanzas()
        elif opcion == "2":
            print("Inventario y Pedidos (en desarrollo)")
        elif opcion == "3":
            print("Gestión de Clientes y Empleados (en desarrollo)")
        elif opcion == "4":
            print("Panel General (en desarrollo)")
        elif opcion == "5":
            print("Saliendo de PIGEEM...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")





if __name__ == "__main__":
    menu_principal()
