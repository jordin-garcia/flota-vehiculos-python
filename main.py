from flota_vehiculos import FlotaVehiculos
from vehiculo import Vehiculo
from mantenimiento import Mantenimiento

import os

flota_vehiculos = FlotaVehiculos()

def limpiar_consola():
    # Para Windows
    if os.name == 'nt':
        os.system('cls')
    # Para macOS y Linux
    else:
        os.system('clear')

def presionar_tecla():
    input("\nPresione [Enter] para regresar...")

print("----- BIENVENIDO -----")
while True:
    print("--- Menú Principal ---")
    print("1. Registrar vehículo")
    print("2. Buscar vehículo")
    print("3. Lista de vehículos")
    print("4. Agregar mantenimiento a un vehículo")
    print("5. Consultar historial de mantenimiento de un vehículo")
    print("6. Eliminar vehículo")
    print("7. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        limpiar_consola()
        try:
            print("--- Agregar Vehículo ---")
            placa = input("\nIngrese la placa (Debe ser un número de 7 dígitos): ")
            marca = input("Ingrese la marca: ")
            modelo = input("Ingrese el modelo: ")
            año = input("Ingrese el año: ")
            kilometraje = float(input("Ingrese el kilometraje: "))

            nuevo_vehiculo = Vehiculo(placa, marca, modelo, año, kilometraje)
            flota_vehiculos.append(nuevo_vehiculo)      
            print("\n***** Vehículo Agregado Exitosamente *****")

        except Exception as e:
            print("\n(*) Error al registrar vehículo: ", e)
        presionar_tecla()

    elif opcion == "2":
        limpiar_consola()
        if flota_vehiculos.is_empty():
            print("(*) No hay vehículos registrados.")
        else:
            print("--- Buscar Vehículo ---")
            placa = input("\nIngrese la placa del vehículo: ")
            vehiculo_buscado = flota_vehiculos.search(placa)
            if vehiculo_buscado:
                print("\n***** Vehículo Encontrado *****")
                print(f"\nPlaca: {vehiculo_buscado.placa}")
                print(f"Marca: {vehiculo_buscado.marca}")
                print(f"Modelo: {vehiculo_buscado.modelo}")
                print(f"Año: {vehiculo_buscado.año}")
                print(f"Kilometraje: {vehiculo_buscado.kilometraje}")
            else:
                print("\n(*) Vehículo no encontrado.")  
        presionar_tecla()

    elif opcion == "3":
        limpiar_consola()
        if flota_vehiculos.is_empty():
            print("\n(*) No hay vehículos registrados.")
        else:
            print("--- Lista de Vehículos ---")
            flota_vehiculos.print_list()
        presionar_tecla()

    elif opcion == "4":
        limpiar_consola()
        if flota_vehiculos.is_empty():
            print("(*) No hay vehículos registrados.")
        else:
            print("--- Agregar Mantenimiento ---")
            placa = input("\nIngrese la placa del vehículo: ")
            vehiculo_buscado = flota_vehiculos.search(placa)
            if vehiculo_buscado:
                try:
                    fecha = input("Ingrese la fecha del mantenimiento (dd/mm/yyyy): ")
                    descripcion = input("Ingrese la descripción del mantenimiento: ")
                    costo = input("Ingrese el costo del mantenimiento: ")

                    mantenimiento = Mantenimiento(fecha, descripcion, costo)
                    vehiculo_buscado.agregar_mantenimiento(mantenimiento)
                    print("\n***** Mantenimiento Agregado Exitosamente *****")

                except Exception as e:
                    print("\n(*) Error al agregar mantenimiento: ", e)    
            else:
                print("\n(*) Vehículo no encontrado.")
        presionar_tecla()

    elif opcion == "5":
        limpiar_consola()
        if flota_vehiculos.is_empty():
            print("(*) No hay vehículos registrados.")
        else:
            print("--- Consultar Historial de Mantenimiento ---")
            placa = input("\nIngrese la placa del vehículo: ")

            vehiculo_buscado = flota_vehiculos.search(placa)
            if vehiculo_buscado:
                if vehiculo_buscado.calcular_costo_total_mantenimiento() == 0:
                    print("\n(*) No hay mantenimientos registrados para este vehículo")
                else:
                    print("\nHistorial de Mantenimiento:")
                    vehiculo_buscado.consultar_historial_mantenimiento()
            else:
                print("\n(*) Vehículo no encontrado.")
        presionar_tecla()

    elif opcion == "6":
        limpiar_consola()
        if flota_vehiculos.is_empty():
            print("(*) No hay vehículos registrados.")
        else:
            print("--- Eliminar Vehículo ---")
            placa = input("\nIngrese la placa del vehículo: ")
            vehiculo_buscado = flota_vehiculos.search(placa)
            if vehiculo_buscado:
                print("\nDatos del vehículo:")
                print(f"\nPlaca: {vehiculo_buscado.placa}")
                print(f"Marca: {vehiculo_buscado.marca}")
                print(f"Modelo: {vehiculo_buscado.modelo}")
                print(f"Año: {vehiculo_buscado.año}")
                print(f"Kilometraje: {vehiculo_buscado.kilometraje}")       
                print("\n¿Está seguro que desea remover este vehículo?")
                confirmacion = input("Ingrese 's' para confirmar o 'n' para cancelar: ")
                if confirmacion == "s":
                    flota_vehiculos.remove(placa)
                    print("\n***** Vehículo Removido Exitosamente *****")
                elif confirmacion == "n":
                    print("\n(*) Operación cancelada")
                else:
                    print("\n(*) Opción inválida")
            else:
                print("\n(*) Vehiculo no encontrado")
        presionar_tecla()

    elif opcion == "7":
        limpiar_consola()
        print("--- ¡Hasta Pronto! ---")
        break

    else:
        input("\n(*) Opción inválida. Intente nuevamente...")

    limpiar_consola()